# Computer repair shop records

A field note from a course project at Sakarya University. The system kept the records of a computer repair service in a Microsoft Access database. Everything was typed in by hand at the counter: customer details, the device, photos of the parts, the warranty period, and the price of each part.

This folder holds a runnable version of that design, so you can try the logic without Access. It uses SQLite and the Python standard library only. All names and numbers in the sample data are made up.

## What the counter needs to answer

A small repair shop is run from a few questions that come up all day:

- Whose laptop is this, and what did they hand in with it?
- What is wrong, who is working on it, and when did we promise it?
- Which jobs are late?
- What parts went in, what did we charge, and what is still unpaid?
- The customer is back: is the part I replaced last spring still under warranty?
- What is running low on the shelf?

Each of these is one command in the program, and each one comes from a plain table, not from a report somebody has to build.

## How the data is laid out

| Table | What it holds |
|---|---|
| customers | Name, phone (unique), address, notes |
| devices | Belongs to a customer: kind, brand, model, serial number, what was handed in |
| jobs | One repair: complaint, finding, promised date, status, labour fee, technician |
| parts | The shelf: code, name, buy price, sell price, stock, minimum stock |
| job_parts | Parts used on a job: quantity, price charged, cost at that time, warranty months, serial, photo |
| payments | Money received per job, with the method |
| status_log | Every status change with its time |

A few decisions that mattered:

- **Devices are separate from customers.** One person brings a laptop today and a printer next year. The history belongs to the device and to the person.
- **Price and cost are copied onto the job line.** Prices change. A repair from last year must still show what we charged and what the part cost us.
- **Warranty starts on the delivery date, not on the repair date.** A part that sits in a finished laptop for two weeks should not lose two weeks of cover.
- **A job moves through fixed steps:** received, diagnosing, waiting for approval, waiting for a part, repairing, ready, delivered (or cancelled). Skipping steps is refused, so "ready" always means something.
- **A cancelled job puts its parts back on the shelf.**
- **A job is not handed over with an unpaid balance** unless the person at the counter says so explicitly.
- **Money is stored as whole units of the smallest coin,** not as decimals, so totals never drift by a cent.
- **Photos are files next to the database;** the table stores the file name. The database stays small.

## Try it

```text
python servis.py demo                     # sample customers, jobs and parts
python servis.py list                     # open jobs, oldest promise first
python servis.py list --overdue           # jobs past their promised date
python servis.py warranty 05321112233     # by phone number or serial number
python servis.py job receipt 1            # printable receipt with balance
python servis.py stock --low              # what to reorder
python servis.py report daily             # takings by payment method
python servis.py --help                   # everything else
```

A typical day, with your own data:

```text
python servis.py part add SSD256 "SSD 256GB SATA" --buy 900 --sell 1250 --stock 4 --min 2
python servis.py customer add "Ayse Demir" 05321112233
python servis.py device 05321112233 laptop --brand Acme --model A15 --serial AC15-0001
python servis.py job open 1 "Slow, hangs with many tabs" --promised 2025-03-10 --tech Ali
python servis.py job status 1 diagnosing
python servis.py job diagnose 1 "Disk almost full, 4GB RAM" --labor 300
python servis.py job status 1 repairing
python servis.py job add-part 1 SSD256 --warranty-months 24 --photo old_disk.jpg
python servis.py job status 1 ready
python servis.py job pay 1 1550
python servis.py job deliver 1
```

The database file is `servis.db` in the current folder, or whatever you set with `--db` or the `SERVIS_DB` environment variable.

## Tests

```text
python -m unittest -v
```

The tests cover the rules that cost money when they are wrong: status order, stock and overselling, payment limits, delivery with debt, warranty dates, cancelled jobs, and exact money arithmetic.

## What I would change today

- Let the customer approve a quote by SMS or e-mail instead of a phone call written in the notes.
- Add a label with a QR code for each device, so the job opens with one scan.
- Back up the database file every night, and test that the backup opens.
- Keep a short list of common faults and their usual parts, so a quote takes seconds.
