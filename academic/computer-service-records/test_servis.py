import tempfile
import unittest
from datetime import date
from pathlib import Path

import servis
from servis import Shop, ShopError, money, add_months


class ShopTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.day = date(2025, 3, 1)
        self.shop = Shop(Path(self.tmp.name) / "t.db", today=lambda: self.day)
        s = self.shop
        s.add_part("RAM8", "RAM 8GB", money("8.50"), money("11"), stock=2, min_stock=1)
        s.add_customer("Test Customer", "0555 000 11 22")
        self.dev = s.add_device("05550001122", "laptop", "Acme", "X1", "SER-1")

    def tearDown(self):
        self.shop.db.close()
        self.tmp.cleanup()

    def ready_job(self):
        s = self.shop
        j = s.open_job(self.dev, "slow", promised="2025-03-05")
        s.set_status(j, "diagnosing")
        s.diagnose(j, "needs RAM", labor=money("10"))
        s.set_status(j, "repairing")
        s.add_job_part(j, "RAM8", 1, warranty_months=12)
        s.set_status(j, "ready")
        return j

    def test_money_is_exact(self):
        self.assertEqual(money("125.50"), 12550)
        self.assertEqual(money("0,1") + money("0,2"), money("0.3"))
        with self.assertRaises(ShopError):
            money("abc")

    def test_duplicate_phone_rejected(self):
        with self.assertRaises(ShopError):
            self.shop.add_customer("Other", "0555 000 11 22")

    def test_status_flow_enforced(self):
        j = self.shop.open_job(self.dev, "dead")
        with self.assertRaises(ShopError):
            self.shop.set_status(j, "ready")          # cannot skip diagnosis
        with self.assertRaises(ShopError):
            self.shop.set_status(j, "delivered")      # only via deliver()

    def test_stock_goes_down_and_blocks_oversell(self):
        j = self.ready_job()
        self.assertEqual(self.shop.part("RAM8")["stock"], 1)
        self.shop.set_status(j, "repairing")
        with self.assertRaises(ShopError):
            self.shop.add_job_part(j, "RAM8", 5)

    def test_totals_and_payment_limits(self):
        j = self.ready_job()
        t = self.shop.totals(j)
        self.assertEqual((t["parts"], t["labor"], t["total"]), (1100, 1000, 2100))
        self.shop.pay(j, 1000)
        self.assertEqual(self.shop.totals(j)["balance"], 1100)
        with self.assertRaises(ShopError):
            self.shop.pay(j, 5000)                    # more than owed

    def test_cannot_deliver_with_debt_unless_allowed(self):
        j = self.ready_job()
        with self.assertRaises(ShopError):
            self.shop.deliver(j)
        self.shop.deliver(j, allow_debt=True)
        self.assertEqual(self.shop.job(j)["status"], "delivered")

    def test_cancel_returns_parts_to_stock(self):
        s = self.shop
        j = s.open_job(self.dev, "dead")
        s.set_status(j, "diagnosing")
        s.set_status(j, "repairing")
        s.add_job_part(j, "RAM8", 2)
        self.assertEqual(s.part("RAM8")["stock"], 0)
        s.set_status(j, "cancelled")
        self.assertEqual(s.part("RAM8")["stock"], 2)

    def test_warranty_starts_at_delivery_and_expires(self):
        j = self.ready_job()
        self.shop.pay(j, self.shop.totals(j)["total"])
        before = self.shop.warranty("SER-1")
        self.assertEqual(before[0]["state"], "starts at delivery")
        self.shop.deliver(j)
        self.assertEqual(self.shop.warranty("0555 000 11 22")[0]["state"], "ACTIVE")
        self.day = date(2026, 3, 2)                   # one year and a day later
        self.assertEqual(self.shop.warranty("SER-1")[0]["state"], "expired")

    def test_overdue_list(self):
        self.ready_job()
        self.assertEqual(self.shop.list_jobs(overdue=True), [])
        self.day = date(2025, 3, 6)
        self.assertEqual(len(self.shop.list_jobs(overdue=True)), 1)

    def test_low_stock_and_reports(self):
        j = self.ready_job()
        self.assertEqual([p["code"] for p in self.shop.low_stock()], ["RAM8"])
        self.shop.pay(j, 500, "card")
        rep = self.shop.daily_report()
        self.assertEqual((rep["received"], rep["takings"][0]["total"]), (1, 500))
        row = self.shop.parts_report("2025-03")[0]
        self.assertEqual((row["qty"], row["margin"]), (1, 250))

    def test_add_months_clamps_end_of_month(self):
        self.assertEqual(add_months(date(2025, 1, 31), 1), date(2025, 2, 28))

    def test_demo_runs_and_shows_overdue(self):
        other = Shop(Path(self.tmp.name) / "demo.db", today=lambda: date(2025, 3, 8))
        try:
            servis.demo(other)
            overdue = other.list_jobs(overdue=True)
            self.assertEqual(len(overdue), 1)              # the till PC job
            self.assertEqual(overdue[0]["promised_at"], "2025-03-06")
            states = {w["part"].split()[0]: w["state"] for w in other.warranty("05321112233")}
            self.assertEqual(states, {"SSD256": "starts at delivery", "RAM8": "starts at delivery"})
            self.assertEqual(other.warranty("SB-77")[0]["state"], "ACTIVE")
        finally:
            other.db.close()

    def test_photo_is_copied_next_to_database(self):
        s = self.shop
        pic = Path(self.tmp.name) / "old.jpg"
        pic.write_bytes(b"x")
        j = s.open_job(self.dev, "dead")
        s.set_status(j, "diagnosing")
        s.set_status(j, "repairing")
        s.add_job_part(j, "RAM8", 1, photo=str(pic))
        stored = s.db.execute("SELECT photo_path FROM job_parts").fetchone()[0]
        self.assertTrue((Path(self.tmp.name) / stored).is_file())


if __name__ == "__main__":
    unittest.main()
