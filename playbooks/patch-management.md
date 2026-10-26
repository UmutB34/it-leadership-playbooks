# Patch management

*A repeatable cycle for keeping servers, endpoints and network devices current without breaking the business.*

## Goal

Close known weaknesses quickly and in a controlled way, and be able to prove it happened.

## The cycle

1. **Inventory.** You cannot patch what you do not know about. Keep an accurate list of systems, owners and software versions.
2. **Watch.** Subscribe to vendor advisories and track which ones affect your inventory.
3. **Assess.** Rate each fix by severity, exposure (internet-facing or internal) and business criticality.
4. **Test.** Try updates on a pilot group or a test copy first.
5. **Deploy.** Roll out in waves, with a maintenance window and a rollback plan.
6. **Verify.** Confirm the installation and service health, and record exceptions.
7. **Report.** Show compliance and open exceptions to management.

## Deployment rings

| Ring | Who | When |
|---|---|---|
| Pilot | IT staff and a few volunteers | Day 0 to 3 |
| Early | One representative group per department | Day 3 to 7 |
| Broad | Everyone else | Day 7 to 14 |
| Servers | By tier, in agreed windows | Per maintenance calendar |

Emergency fixes for actively exploited issues skip the rings, but they still get a recorded approval.

## Target times (illustrative)

| Severity | Internet-facing | Internal |
|---|---|---|
| Critical | 72 hours | 7 days |
| High | 7 days | 14 days |
| Medium | 30 days | 30 days |

## Exceptions

Some systems cannot be updated on time, because of vendor support or uptime needs. Each exception has an owner, a reason, a compensating control and an end date, and it appears in the report.

## Measures

- Patch compliance by ring and by tier.
- Time from release to installation.
- Number and age of open exceptions.
- Failed deployments and rollbacks.

## Evidence for auditors

The inventory, the target times, the monthly compliance reports and the exception register answer most audit questions without extra work.
