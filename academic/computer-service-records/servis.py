#!/usr/bin/env python3
"""Records for a neighbourhood computer repair shop.

Customers, devices, repair jobs, parts with photos and warranty, payments,
stock and a few daily reports. Standard library only (sqlite3).

    python servis.py demo            # fill a sample database with made-up data
    python servis.py --help
"""
import argparse
import calendar
import os
import shutil
import sqlite3
import sys
from datetime import date, datetime, timedelta
from decimal import Decimal, InvalidOperation
from pathlib import Path

HERE = Path(__file__).resolve().parent

FLOW = {
    "received": {"diagnosing", "cancelled"},
    "diagnosing": {"waiting_approval", "repairing", "ready", "cancelled"},
    "waiting_approval": {"diagnosing", "repairing", "waiting_part", "cancelled"},
    "waiting_part": {"repairing", "cancelled"},
    "repairing": {"waiting_part", "ready", "cancelled"},
    "ready": {"repairing", "delivered", "cancelled"},
    "delivered": set(),
    "cancelled": set(),
}
OPEN_STATES = tuple(s for s in FLOW if s not in ("delivered", "cancelled"))


class ShopError(Exception):
    """A rule of the shop was broken (shown to the user, not a crash)."""


def money(text):
    """'125.50' -> 12550 (integer minor units)."""
    try:
        value = (Decimal(str(text).replace(",", ".")) * 100).to_integral_value()
    except InvalidOperation:
        raise ShopError(f"not a valid amount: {text!r}")
    if value < 0:
        raise ShopError("amount cannot be negative")
    return int(value)


def fmt(minor):
    return f"{minor / 100:,.2f}"


def add_months(d, months):
    index = d.month - 1 + months
    year, month = d.year + index // 12, index % 12 + 1
    return date(year, month, min(d.day, calendar.monthrange(year, month)[1]))


def parse_date(text):
    try:
        return datetime.strptime(text, "%Y-%m-%d").date()
    except (TypeError, ValueError):
        raise ShopError(f"date must look like 2025-03-31, got {text!r}")


class Shop:
    def __init__(self, db_path, today=None):
        self.db_path = Path(db_path)
        self.photo_dir = self.db_path.parent / "photos"
        self.today = today or date.today
        self.db = sqlite3.connect(self.db_path)
        self.db.row_factory = sqlite3.Row
        self.db.execute("PRAGMA foreign_keys = ON")
        self.db.executescript((HERE / "schema.sql").read_text(encoding="utf-8"))

    # ---- customers and devices -------------------------------------------
    def add_customer(self, name, phone, address=None, note=None):
        phone = "".join(ch for ch in phone if ch.isdigit() or ch == "+")
        if len(phone) < 7:
            raise ShopError("phone number looks too short")
        try:
            cur = self.db.execute(
                "INSERT INTO customers(name, phone, address, note) VALUES (?,?,?,?)",
                (name.strip(), phone, address, note))
        except sqlite3.IntegrityError:
            raise ShopError(f"a customer with phone {phone} already exists")
        self.db.commit()
        return cur.lastrowid

    def customer_by_phone(self, phone):
        phone = "".join(ch for ch in phone if ch.isdigit() or ch == "+")
        row = self.db.execute("SELECT * FROM customers WHERE phone=?", (phone,)).fetchone()
        if not row:
            raise ShopError(f"no customer with phone {phone}")
        return row

    def find_customers(self, text):
        like = f"%{text}%"
        return self.db.execute(
            "SELECT * FROM customers WHERE name LIKE ? OR phone LIKE ? ORDER BY name",
            (like, like)).fetchall()

    def add_device(self, phone, kind, brand=None, model=None, serial=None, accessories=None):
        customer = self.customer_by_phone(phone)
        try:
            cur = self.db.execute(
                "INSERT INTO devices(customer_id, kind, brand, model, serial_no, accessories)"
                " VALUES (?,?,?,?,?,?)",
                (customer["id"], kind, brand, model, serial, accessories))
        except sqlite3.IntegrityError:
            raise ShopError("this customer already has a device with that serial number")
        self.db.commit()
        return cur.lastrowid

    # ---- parts and stock --------------------------------------------------
    def add_part(self, code, name, buy, sell, stock=0, min_stock=0):
        try:
            cur = self.db.execute(
                "INSERT INTO parts(code, name, buy_price, sell_price, stock, min_stock)"
                " VALUES (?,?,?,?,?,?)", (code.upper(), name, buy, sell, stock, min_stock))
        except sqlite3.IntegrityError:
            raise ShopError(f"part code {code.upper()} already exists")
        self.db.commit()
        return cur.lastrowid

    def part(self, code):
        row = self.db.execute("SELECT * FROM parts WHERE code=?", (code.upper(),)).fetchone()
        if not row:
            raise ShopError(f"unknown part code {code.upper()}")
        return row

    def restock(self, code, qty):
        if qty <= 0:
            raise ShopError("quantity must be positive")
        part = self.part(code)
        self.db.execute("UPDATE parts SET stock = stock + ? WHERE id=?", (qty, part["id"]))
        self.db.commit()

    def low_stock(self):
        return self.db.execute(
            "SELECT * FROM parts WHERE stock <= min_stock ORDER BY stock, code").fetchall()

    # ---- jobs -------------------------------------------------------------
    def job(self, job_id):
        row = self.db.execute("SELECT * FROM jobs WHERE id=?", (job_id,)).fetchone()
        if not row:
            raise ShopError(f"no job number {job_id}")
        return row

    def open_job(self, device_id, complaint, promised=None, technician=None):
        if not self.db.execute("SELECT 1 FROM devices WHERE id=?", (device_id,)).fetchone():
            raise ShopError(f"no device number {device_id}")
        if promised:
            promised = parse_date(promised).isoformat()
        cur = self.db.execute(
            "INSERT INTO jobs(device_id, received_at, promised_at, complaint, technician)"
            " VALUES (?,?,?,?,?)",
            (device_id, self.today().isoformat(), promised, complaint, technician))
        self._log(cur.lastrowid, None, "received", "job opened")
        self.db.commit()
        return cur.lastrowid

    def _log(self, job_id, old, new, note=None):
        self.db.execute("INSERT INTO status_log(job_id, at, old, new, note) VALUES (?,?,?,?,?)",
                        (job_id, datetime.now().isoformat(timespec="seconds"), old, new, note))

    def set_status(self, job_id, new, note=None):
        job = self.job(job_id)
        old = job["status"]
        if new not in FLOW:
            raise ShopError(f"unknown status {new!r}; choose from {', '.join(FLOW)}")
        if new not in FLOW[old]:
            allowed = ", ".join(sorted(FLOW[old])) or "none (job is closed)"
            raise ShopError(f"cannot go from {old} to {new}; allowed: {allowed}")
        if new == "delivered":
            raise ShopError("use the 'deliver' command so payment and warranty are handled")
        if new == "cancelled":
            self._return_parts(job_id)
        self.db.execute("UPDATE jobs SET status=? WHERE id=?", (new, job_id))
        self._log(job_id, old, new, note)
        self.db.commit()

    def _return_parts(self, job_id):
        for row in self.db.execute("SELECT part_id, qty FROM job_parts WHERE job_id=?", (job_id,)):
            self.db.execute("UPDATE parts SET stock = stock + ? WHERE id=?",
                            (row["qty"], row["part_id"]))
        self.db.execute("DELETE FROM job_parts WHERE job_id=?", (job_id,))

    def diagnose(self, job_id, text, labor=None):
        job = self.job(job_id)
        if job["status"] not in OPEN_STATES:
            raise ShopError("job is closed")
        self.db.execute("UPDATE jobs SET diagnosis=?, labor_fee=COALESCE(?, labor_fee) WHERE id=?",
                        (text, labor, job_id))
        self.db.commit()

    def add_job_part(self, job_id, code, qty=1, price=None, warranty_months=0,
                     serial=None, photo=None):
        job = self.job(job_id)
        if job["status"] not in ("diagnosing", "waiting_approval", "waiting_part", "repairing"):
            raise ShopError(f"parts cannot be added while the job is {job['status']}")
        part = self.part(code)
        if qty <= 0:
            raise ShopError("quantity must be positive")
        if part["stock"] < qty:
            raise ShopError(f"only {part['stock']} of {part['code']} in stock; "
                            "restock or set the job to waiting_part")
        stored = None
        if photo:
            src = Path(photo)
            if not src.is_file():
                raise ShopError(f"photo file not found: {photo}")
            self.photo_dir.mkdir(exist_ok=True)
            n = self.db.execute("SELECT COUNT(*) FROM job_parts WHERE job_id=?",
                                (job_id,)).fetchone()[0] + 1
            target = self.photo_dir / f"job{job_id}-{part['code']}-{n}{src.suffix.lower()}"
            shutil.copyfile(src, target)
            stored = f"photos/{target.name}"
        self.db.execute(
            "INSERT INTO job_parts(job_id, part_id, qty, unit_price, unit_cost,"
            " warranty_months, part_serial, photo_path) VALUES (?,?,?,?,?,?,?,?)",
            (job_id, part["id"], qty, part["sell_price"] if price is None else price,
             part["buy_price"], warranty_months, serial, stored))
        self.db.execute("UPDATE parts SET stock = stock - ? WHERE id=?", (qty, part["id"]))
        self.db.commit()

    def totals(self, job_id):
        job = self.job(job_id)
        parts = self.db.execute(
            "SELECT COALESCE(SUM(qty*unit_price),0) FROM job_parts WHERE job_id=?",
            (job_id,)).fetchone()[0]
        paid = self.db.execute("SELECT COALESCE(SUM(amount),0) FROM payments WHERE job_id=?",
                               (job_id,)).fetchone()[0]
        total = parts + job["labor_fee"]
        return {"parts": parts, "labor": job["labor_fee"], "total": total,
                "paid": paid, "balance": total - paid}

    def pay(self, job_id, amount, method="cash"):
        self.job(job_id)
        if amount <= 0:
            raise ShopError("payment must be more than zero")
        balance = self.totals(job_id)["balance"]
        if amount > balance:
            raise ShopError(f"payment {fmt(amount)} is more than the balance {fmt(balance)}")
        self.db.execute("INSERT INTO payments(job_id, paid_at, amount, method) VALUES (?,?,?,?)",
                        (job_id, self.today().isoformat(), amount, method))
        self.db.commit()

    def deliver(self, job_id, allow_debt=False):
        job = self.job(job_id)
        if job["status"] != "ready":
            raise ShopError(f"only a 'ready' job can be delivered (this one is {job['status']})")
        balance = self.totals(job_id)["balance"]
        if balance > 0 and not allow_debt:
            raise ShopError(f"balance of {fmt(balance)} is unpaid; take payment or use --allow-debt")
        self.db.execute("UPDATE jobs SET status='delivered', delivered_at=? WHERE id=?",
                        (self.today().isoformat(), job_id))
        self._log(job_id, "ready", "delivered", f"balance left {fmt(balance)}")
        self.db.commit()

    # ---- questions the counter asks all day --------------------------------
    def list_jobs(self, status=None, overdue=False):
        sql = ("SELECT j.id, j.status, j.received_at, j.promised_at, c.name, c.phone,"
               " d.kind, d.brand, d.model FROM jobs j JOIN devices d ON d.id=j.device_id"
               " JOIN customers c ON c.id=d.customer_id WHERE 1=1")
        args = []
        if status:
            sql += " AND j.status=?"
            args.append(status)
        else:
            sql += f" AND j.status IN ({','.join('?' * len(OPEN_STATES))})"
            args += OPEN_STATES
        if overdue:
            sql += " AND j.promised_at IS NOT NULL AND j.promised_at < ?"
            args.append(self.today().isoformat())
        return self.db.execute(sql + " ORDER BY j.promised_at IS NULL, j.promised_at, j.id", args).fetchall()

    def warranty(self, who):
        """Parts still under warranty, found by phone number or device serial."""
        digits = "".join(ch for ch in who if ch.isdigit() or ch == "+")
        rows = self.db.execute(
            "SELECT jp.*, p.code, p.name, j.id AS job_id, j.delivered_at, c.name AS customer,"
            " d.kind, d.brand, d.model FROM job_parts jp JOIN parts p ON p.id=jp.part_id"
            " JOIN jobs j ON j.id=jp.job_id JOIN devices d ON d.id=j.device_id"
            " JOIN customers c ON c.id=d.customer_id"
            " WHERE jp.warranty_months > 0 AND (c.phone=? OR d.serial_no=? OR jp.part_serial=?)"
            " ORDER BY j.id", (digits, who, who)).fetchall()
        today, out = self.today(), []
        for r in rows:
            if not r["delivered_at"]:
                state, ends = "starts at delivery", None
            else:
                ends = add_months(parse_date(r["delivered_at"]), r["warranty_months"])
                state = "ACTIVE" if ends >= today else "expired"
            out.append({"job": r["job_id"], "customer": r["customer"], "device": f"{r['brand'] or ''} {r['model'] or r['kind']}".strip(),
                        "part": f"{r['code']} {r['name']}", "months": r["warranty_months"],
                        "ends": ends.isoformat() if ends else None, "state": state})
        return out

    def history(self, phone):
        customer = self.customer_by_phone(phone)
        return customer, self.db.execute(
            "SELECT j.id, j.received_at, j.status, j.complaint, d.kind, d.brand, d.model"
            " FROM jobs j JOIN devices d ON d.id=j.device_id WHERE d.customer_id=?"
            " ORDER BY j.id DESC", (customer["id"],)).fetchall()

    def daily_report(self, day=None):
        day = day or self.today().isoformat()
        q = lambda sql, *a: self.db.execute(sql, a).fetchall()
        return {
            "day": day,
            "received": q("SELECT COUNT(*) n FROM jobs WHERE received_at=?", day)[0]["n"],
            "delivered": q("SELECT COUNT(*) n FROM jobs WHERE delivered_at=?", day)[0]["n"],
            "takings": q("SELECT method, SUM(amount) total FROM payments WHERE paid_at=? "
                         "GROUP BY method ORDER BY method", day),
        }

    def parts_report(self, month):
        return self.db.execute(
            "SELECT p.code, p.name, SUM(jp.qty) qty, SUM(jp.qty*jp.unit_price) revenue,"
            " SUM(jp.qty*(jp.unit_price-jp.unit_cost)) margin FROM job_parts jp"
            " JOIN parts p ON p.id=jp.part_id JOIN jobs j ON j.id=jp.job_id"
            " WHERE substr(j.received_at,1,7)=? GROUP BY p.id ORDER BY revenue DESC",
            (month,)).fetchall()

    def receipt(self, job_id):
        job = self.job(job_id)
        d = self.db.execute("SELECT d.*, c.name, c.phone FROM devices d JOIN customers c"
                            " ON c.id=d.customer_id WHERE d.id=?", (job["device_id"],)).fetchone()
        lines = [f"SERVICE RECEIPT  #{job_id}", "-" * 44,
                 f"Customer : {d['name']} ({d['phone']})",
                 f"Device   : {d['kind']} {d['brand'] or ''} {d['model'] or ''}".rstrip(),
                 f"Serial   : {d['serial_no'] or '-'}",
                 f"Received : {job['received_at']}   Promised: {job['promised_at'] or '-'}",
                 f"Problem  : {job['complaint']}"]
        if job["diagnosis"]:
            lines.append(f"Finding  : {job['diagnosis']}")
        lines.append("-" * 44)
        for r in self.db.execute("SELECT jp.*, p.code, p.name FROM job_parts jp JOIN parts p"
                                 " ON p.id=jp.part_id WHERE jp.job_id=?", (job_id,)):
            warranty = f"  [{r['warranty_months']} mo warranty]" if r["warranty_months"] else ""
            lines.append(f"{r['qty']:>2} x {r['code']:<8} {r['name'][:18]:<18}"
                         f"{fmt(r['qty'] * r['unit_price']):>10}{warranty}")
        t = self.totals(job_id)
        lines += [f"Labour{fmt(t['labor']):>38}", f"Parts{fmt(t['parts']):>39}",
                  f"TOTAL{fmt(t['total']):>39}", f"Paid{fmt(t['paid']):>40}",
                  f"BALANCE{fmt(t['balance']):>37}", "-" * 44,
                  "Warranty starts on the delivery date and covers the listed parts only."]
        return "\n".join(lines)


# ---- sample data ---------------------------------------------------------------
def demo(shop):
    """Made-up customers and jobs so every command has something to show."""
    parts = [("RAM8", "DDR4 8GB laptop RAM", "850", "1100", 6, 2),
             ("SSD256", "SSD 256GB SATA", "900", "1250", 4, 2),
             ("SCR156", "Laptop screen 15.6 in", "2100", "2900", 2, 1),
             ("PSU450", "Power supply 450W", "700", "950", 3, 1),
             ("CHG65", "Laptop charger 65W", "320", "480", 1, 2),
             ("PASTE", "Thermal paste", "40", "90", 12, 3)]
    for code, name, buy, sell, stock, low in parts:
        shop.add_part(code, name, money(buy), money(sell), stock, low)
    ayse = shop.add_customer("Ayse Demir", "0532 111 22 33", "Elm street 4", "prefers phone calls")
    mehmet = shop.add_customer("Mehmet Kaya", "0533 222 33 44")
    bakery = shop.add_customer("Corner Bakery", "0212 555 66 77", note="till PC, urgent jobs")
    d1 = shop.add_device("0532 111 22 33", "laptop", "Acme", "A15", "AC15-0001", "charger")
    d2 = shop.add_device("0533 222 33 44", "desktop", "Self-built", "tower", "SB-77")
    d3 = shop.add_device("0212 555 66 77", "desktop", "Acme", "Till-PC", "TILL-9", "mouse, keyboard")
    day = lambda n: (shop.today() + timedelta(days=n)).isoformat()   # dates relative to today
    j1 = shop.open_job(d1, "Slow, hangs when opening many tabs", promised=day(3), technician="Ali")
    shop.set_status(j1, "diagnosing")
    shop.diagnose(j1, "Disk almost full and only 4GB RAM; recommend SSD and RAM upgrade",
                  labor=money("300"))
    shop.set_status(j1, "waiting_approval", "called customer, approved")
    shop.set_status(j1, "repairing")
    shop.add_job_part(j1, "SSD256", 1, warranty_months=24, serial="SSD-A1B2")
    shop.add_job_part(j1, "RAM8", 1, warranty_months=12)
    shop.set_status(j1, "ready")
    shop.pay(j1, money("1000"))
    j2 = shop.open_job(d2, "Does not power on", promised=day(0))
    shop.set_status(j2, "diagnosing")
    shop.diagnose(j2, "Power supply dead", labor=money("150"))
    shop.set_status(j2, "waiting_approval")
    shop.set_status(j2, "repairing")
    shop.add_job_part(j2, "PSU450", 1, warranty_months=12)
    shop.set_status(j2, "ready")
    shop.pay(j2, money("1100"))
    shop.deliver(j2)
    j3 = shop.open_job(d3, "Screen flickers, cashier cannot work", promised=day(-2), technician="Ali")
    shop.set_status(j3, "diagnosing")
    shop.set_status(j3, "waiting_approval")
    return {"jobs": [j1, j2, j3]}


# ---- command line ------------------------------------------------------------
def build_parser():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--db", default=os.environ.get("SERVIS_DB", "servis.db"), help="database file")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("init", help="create an empty database")
    sub.add_parser("demo", help="fill with sample data")
    c = sub.add_parser("customer", help="add or find customers")
    cs = c.add_subparsers(dest="sub", required=True)
    a = cs.add_parser("add"); a.add_argument("name"); a.add_argument("phone")
    a.add_argument("--address"); a.add_argument("--note")
    f = cs.add_parser("find"); f.add_argument("text")
    d = sub.add_parser("device", help="register a device for a customer")
    d.add_argument("phone"); d.add_argument("kind")
    for opt in ("brand", "model", "serial", "accessories"):
        d.add_argument(f"--{opt}")
    pt = sub.add_parser("part", help="parts catalogue and stock")
    ps = pt.add_subparsers(dest="sub", required=True)
    pa = ps.add_parser("add"); pa.add_argument("code"); pa.add_argument("name")
    pa.add_argument("--buy", required=True); pa.add_argument("--sell", required=True)
    pa.add_argument("--stock", type=int, default=0); pa.add_argument("--min", type=int, default=0)
    pr = ps.add_parser("restock"); pr.add_argument("code"); pr.add_argument("qty", type=int)
    j = sub.add_parser("job", help="repair jobs")
    js = j.add_subparsers(dest="sub", required=True)
    o = js.add_parser("open"); o.add_argument("device", type=int); o.add_argument("complaint")
    o.add_argument("--promised"); o.add_argument("--tech")
    s = js.add_parser("status"); s.add_argument("job", type=int); s.add_argument("status")
    s.add_argument("--note")
    g = js.add_parser("diagnose"); g.add_argument("job", type=int); g.add_argument("text")
    g.add_argument("--labor")
    ap = js.add_parser("add-part"); ap.add_argument("job", type=int); ap.add_argument("code")
    ap.add_argument("--qty", type=int, default=1); ap.add_argument("--price")
    ap.add_argument("--warranty-months", type=int, default=0); ap.add_argument("--serial")
    ap.add_argument("--photo")
    py = js.add_parser("pay"); py.add_argument("job", type=int); py.add_argument("amount")
    py.add_argument("--method", default="cash", choices=["cash", "card", "transfer"])
    dl = js.add_parser("deliver"); dl.add_argument("job", type=int)
    dl.add_argument("--allow-debt", action="store_true")
    sh = js.add_parser("show"); sh.add_argument("job", type=int)
    rc = js.add_parser("receipt"); rc.add_argument("job", type=int)
    ls = sub.add_parser("list", help="open jobs")
    ls.add_argument("--status"); ls.add_argument("--overdue", action="store_true")
    w = sub.add_parser("warranty", help="warranty check by phone or serial number")
    w.add_argument("who")
    h = sub.add_parser("history", help="all jobs of a customer"); h.add_argument("phone")
    st = sub.add_parser("stock", help="stock levels"); st.add_argument("--low", action="store_true")
    r = sub.add_parser("report", help="daily takings or part usage")
    rs = r.add_subparsers(dest="sub", required=True)
    rd = rs.add_parser("daily"); rd.add_argument("day", nargs="?")
    rp = rs.add_parser("parts"); rp.add_argument("month", help="YYYY-MM")
    return p


def run(args, out=print):
    shop = Shop(args.db)
    cmd, sub = args.cmd, getattr(args, "sub", None)
    if cmd == "init":
        out(f"database ready: {args.db}")
    elif cmd == "demo":
        info = demo(shop)
        out(f"sample data loaded; jobs {info['jobs']}. Try: list --overdue, warranty 05321112233, receipt 1")
    elif cmd == "customer" and sub == "add":
        out(f"customer #{shop.add_customer(args.name, args.phone, args.address, args.note)} added")
    elif cmd == "customer":
        for c in shop.find_customers(args.text):
            out(f"#{c['id']}  {c['name']}  {c['phone']}  {c['note'] or ''}")
    elif cmd == "device":
        out(f"device #{shop.add_device(args.phone, args.kind, args.brand, args.model, args.serial, args.accessories)} added")
    elif cmd == "part" and sub == "add":
        shop.add_part(args.code, args.name, money(args.buy), money(args.sell), args.stock, args.min)
        out(f"part {args.code.upper()} added")
    elif cmd == "part":
        shop.restock(args.code, args.qty)
        out(f"{args.code.upper()} stock is now {shop.part(args.code)['stock']}")
    elif cmd == "job" and sub == "open":
        out(f"job #{shop.open_job(args.device, args.complaint, args.promised, args.tech)} opened")
    elif cmd == "job" and sub == "status":
        shop.set_status(args.job, args.status, args.note); out(f"job {args.job}: {args.status}")
    elif cmd == "job" and sub == "diagnose":
        shop.diagnose(args.job, args.text, money(args.labor) if args.labor else None)
        out("diagnosis saved")
    elif cmd == "job" and sub == "add-part":
        shop.add_job_part(args.job, args.code, args.qty, money(args.price) if args.price else None,
                          args.warranty_months, args.serial, args.photo)
        out("part added to job")
    elif cmd == "job" and sub == "pay":
        shop.pay(args.job, money(args.amount), args.method)
        out(f"balance now {fmt(shop.totals(args.job)['balance'])}")
    elif cmd == "job" and sub == "deliver":
        shop.deliver(args.job, args.allow_debt); out(f"job {args.job} delivered")
    elif cmd == "job" and sub in ("show", "receipt"):
        out(shop.receipt(args.job))
    elif cmd == "list":
        rows = shop.list_jobs(args.status, args.overdue)
        for r in rows:
            device = f"{r['kind']} {r['brand'] or ''} {r['model'] or ''}".strip()
            out(f"#{r['id']:<4}{r['status']:<17}promised {r['promised_at'] or '-':<11}{r['name']} ({r['phone']}) - {device}")
        out(f"{len(rows)} job(s)")
    elif cmd == "warranty":
        rows = shop.warranty(args.who)
        for r in rows:
            out(f"job #{r['job']} {r['customer']} / {r['device']}: {r['part']} - {r['months']} mo, "
                f"{r['state']}{' until ' + r['ends'] if r['ends'] else ''}")
        if not rows:
            out("no parts with warranty found")
    elif cmd == "history":
        c, rows = shop.history(args.phone)
        out(f"{c['name']} ({c['phone']})")
        for r in rows:
            out(f"  #{r['id']} {r['received_at']} {r['status']:<10} {r['kind']} {r['model'] or ''} - {r['complaint']}")
    elif cmd == "stock":
        rows = shop.low_stock() if args.low else shop.db.execute("SELECT * FROM parts ORDER BY code").fetchall()
        for r in rows:
            flag = "  <-- reorder" if r["stock"] <= r["min_stock"] else ""
            out(f"{r['code']:<8}{r['name']:<26}stock {r['stock']:>3} (min {r['min_stock']}){flag}")
    elif cmd == "report" and sub == "daily":
        rep = shop.daily_report(args.day)
        out(f"{rep['day']}: {rep['received']} received, {rep['delivered']} delivered")
        for t in rep["takings"]:
            out(f"  {t['method']:<9}{fmt(t['total']):>12}")
    elif cmd == "report":
        for r in shop.parts_report(args.month):
            out(f"{r['code']:<8}{r['name']:<26}qty {r['qty']:>3}  revenue {fmt(r['revenue']):>10}  margin {fmt(r['margin']):>10}")


def main(argv=None):
    args = build_parser().parse_args(argv)
    try:
        run(args)
    except ShopError as err:
        print(f"Cannot do that: {err}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
