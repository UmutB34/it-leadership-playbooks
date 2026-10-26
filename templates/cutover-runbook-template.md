# Cutover runbook

| Field | Entry |
|---|---|
| Service and wave | |
| Window (start - end) | |
| Strictest unit and tolerance | |
| Change approver / decision maker | |
| Incident lead / communications lead | |

## Entry criteria (all must be true)
- [ ] Parity checklist complete
- [ ] Rehearsal done and timed
- [ ] Final backup taken and restore point recorded
- [ ] Users informed twice; help channel staffed
- [ ] Rollback steps reviewed

## Steps

| # | Step | Owner | Planned start | Planned duration | Actual start | Actual end | Result |
|---|---|---|---|---|---|---|---|
| 1 | Announce start, freeze changes | | | | | | |
| 2 | Make source read-only / stop writes | | | | | | |
| 3 | Final synchronization | | | | | | |
| 4 | Verify counts, sizes, permissions | | | | | | |
| 5 | Switch (routing, namespace, DNS, trunks) | | | | | | |
| 6 | Smoke test with named users from several units | | | | | | |
| 7 | Go / no-go decision | | | | | | |

## Point of no return
Time: ______  Decision by: ______  Criteria: ______

## Rollback steps
1.
2.
3.

## After the window
- [ ] Hypercare staffed; first-day issue list owner named
- [ ] Old service kept read-only until: ______
- [ ] Review meeting scheduled
