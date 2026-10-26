# Daily IT operations checklist

*A tool-neutral routine for a small IT team. Each line says what to look at, what to do and who to involve.*

## Goal

Catch small problems early, keep a record that the checks happened, and make hand-over between people easy.

## How to run it

- One owner per row, and one backup.
- Do it each working day at a fixed time. Findings go into the ticket system, not into memory.
- Sign off with initials and time, so the routine can be audited.

## Checklist

| Area | What to check | If something is wrong |
|---|---|---|
| Security alerts | Alerts from the security operations service and monitoring tools; unacknowledged items | Open a ticket for the provider team and escalate to the security owner |
| E-mail gateway | Quarantine and other disposition states; unusual senders or volumes | Release or block with the security team; note the reason |
| Cloud mail protection | Quarantined items in the productivity suite | Review, release or report |
| Vulnerability scan results | New reports, split by owner or supplier | Assign each item an owner and due date |
| Endpoint management console | Dashboard tabs, detections, update packages, agent versions | Fix failed installs; plan updates |
| Endpoint protection console | Detections, encryption status, outdated agents | Confirm with the user for user-based alerts; check quarantine for server alerts |
| Directory audit logs | Mass deletions, privileged changes, failed sign-ins | Verify with the change record or escalate |
| Mobile device management | Versions and connection status of managed phones | Re-enrol or repair; remove lost devices |
| Service desk | Open and ageing tickets, asset hand-overs and returns | Chase owners; update assignments |
| Backups and replication | Job success, last restore test date | Re-run failed jobs; ticket for the provider |
| Peripherals | Printer consumables below threshold | Replace and log |
| Monitoring dashboards | Key service graphs (availability, capacity) | Investigate trends before they alert |

## Weekly additions

- Review the exception list and the ageing of open findings.
- Check licence and certificate expiry dates.
- Skim the change calendar for the next two weeks.

## Measures

- Share of days the routine was completed.
- Time from alert to ticket.
- Findings found by the routine versus found by users.

## Why it helps

A written routine turns individual habits into a service. It is also the cheapest evidence an auditor can ask for.
