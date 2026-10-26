-- Computer repair shop records: customers, devices, jobs, parts, payments.
-- Money is stored as integer minor units (kurus) to avoid rounding errors.

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS customers (
    id          INTEGER PRIMARY KEY,
    name        TEXT NOT NULL,
    phone       TEXT NOT NULL UNIQUE,
    address     TEXT,
    note        TEXT,
    created_at  TEXT NOT NULL DEFAULT (date('now'))
);

CREATE TABLE IF NOT EXISTS devices (
    id           INTEGER PRIMARY KEY,
    customer_id  INTEGER NOT NULL REFERENCES customers(id),
    kind         TEXT NOT NULL,              -- laptop, desktop, printer, phone ...
    brand        TEXT,
    model        TEXT,
    serial_no    TEXT,
    accessories  TEXT,                       -- charger, bag, ... as handed in
    UNIQUE (customer_id, serial_no)
);

CREATE TABLE IF NOT EXISTS parts (
    id          INTEGER PRIMARY KEY,
    code        TEXT NOT NULL UNIQUE,
    name        TEXT NOT NULL,
    buy_price   INTEGER NOT NULL DEFAULT 0,
    sell_price  INTEGER NOT NULL DEFAULT 0,
    stock       INTEGER NOT NULL DEFAULT 0,
    min_stock   INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS jobs (
    id           INTEGER PRIMARY KEY,
    device_id    INTEGER NOT NULL REFERENCES devices(id),
    received_at  TEXT NOT NULL,
    promised_at  TEXT,
    complaint    TEXT NOT NULL,
    diagnosis    TEXT,
    status       TEXT NOT NULL DEFAULT 'received'
                 CHECK (status IN ('received','diagnosing','waiting_approval',
                                   'waiting_part','repairing','ready',
                                   'delivered','cancelled')),
    labor_fee    INTEGER NOT NULL DEFAULT 0,
    delivered_at TEXT,
    technician   TEXT
);

CREATE TABLE IF NOT EXISTS job_parts (
    id              INTEGER PRIMARY KEY,
    job_id          INTEGER NOT NULL REFERENCES jobs(id),
    part_id         INTEGER NOT NULL REFERENCES parts(id),
    qty             INTEGER NOT NULL CHECK (qty > 0),
    unit_price      INTEGER NOT NULL,        -- price charged, may differ from list
    unit_cost       INTEGER NOT NULL DEFAULT 0,  -- what the part cost us at the time
    warranty_months INTEGER NOT NULL DEFAULT 0,
    part_serial     TEXT,
    photo_path      TEXT                     -- photo of the part taken out / put in
);

CREATE TABLE IF NOT EXISTS payments (
    id       INTEGER PRIMARY KEY,
    job_id   INTEGER NOT NULL REFERENCES jobs(id),
    paid_at  TEXT NOT NULL,
    amount   INTEGER NOT NULL CHECK (amount > 0),
    method   TEXT NOT NULL DEFAULT 'cash'
);

CREATE TABLE IF NOT EXISTS status_log (
    id        INTEGER PRIMARY KEY,
    job_id    INTEGER NOT NULL REFERENCES jobs(id),
    at        TEXT NOT NULL,
    old       TEXT,
    new       TEXT NOT NULL,
    note      TEXT
);

CREATE INDEX IF NOT EXISTS idx_jobs_status ON jobs(status);
CREATE INDEX IF NOT EXISTS idx_devices_customer ON devices(customer_id);
CREATE INDEX IF NOT EXISTS idx_job_parts_job ON job_parts(job_id);
