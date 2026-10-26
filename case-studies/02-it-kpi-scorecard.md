# Building an IT scorecard on independent evidence

*A reusable method. No organization, amount or internal identifier is described. The table below is an illustrative structure.*

## Purpose

Give leadership a short, honest view of how IT is doing, built on evidence that IT does not control.

## Common ways an IT scorecard fails

1. **It counts activity, not outcome.** "Install the monitoring system" scores full marks even if nobody reads the alerts.
2. **It ignores availability.** The card looks good in a year with serious outages.
3. **The budget target punishes good decisions.** A "spend less" goal rewards putting off necessary work.

## Illustrative structure

| Perspective | Weight | Example KPIs |
|---|---|---|
| Financial | Small | Operating and capital budget within plan, from the accounting system |
| Stakeholder and supplier | Largest | Security operations running without interruption; a key resilience project delivered; business applications live; recovery capability improved and tested |
| Internal process | Small | Hours of unplanned downtime (target: zero) |
| Learning | Minimal | Training completion |

## Design rules

- **Evidence is independent of IT.** Use accounting records, system logs and the service-desk platform, not a self-reported spreadsheet.
- **Project KPIs are date-based and binary.** "Live by 31 December" is easy to verify. If partial scope counts, the note says exactly what counts.
- **Pair delivery with stability.** A downtime KPI next to the project KPIs stops one being bought at the cost of the other.
- **Cap scores,** so one excellent result cannot hide a failure elsewhere.
- **Give budget KPIs context.** Show the budget and the remaining amount, not a bare percentage.

## Trade-offs to watch

- Too many KPIs dilute attention. Keep the count small.
- If a KPI depends on a supplier's schedule, measure your own part (test and acceptance dates).
- Evidence kept in a spreadsheet can be disputed. Prefer logs, tickets and accounting records.
- A zero-downtime target needs a scoring rule that separates a 20-minute event from a 20-hour one.

## Lessons

1. A scorecard is an agreement about what to stop doing, not only what to start.
2. Prefer KPIs where the evidence is automatic.
3. Pair delivery KPIs with a stability KPI.
4. Write the scoring rule so a new manager understands it in one read.

## Template

    KPI name:
    Why it matters (one sentence):
    Owner:
    Source of evidence (independent of the owner):
    Measurement frequency:
    Target and scoring rule (one sentence):
    What is NOT counted:
    Review date:
