# Migrating services by business-unit tolerance

*A method note. No organization, supplier, system name, count or date is described. It is how I plan any migration where several business units depend on the same service.*

## The idea

A migration plan fails less often when it starts from **what each business unit can tolerate**, not from what the technology team finds convenient. The same service (a file share, a mail platform, a telephone system) is used by units with very different tolerance for interruption. The plan is built around the strictest unit that shares the service, and the order of waves is set by tolerance and by willingness to pilot.

## Step 1: Inventory what moves and who depends on it

For each service in scope record: owner, users and units, dependencies (other systems, integrations, scheduled jobs, printers, scanners, mobile devices, remote access), data size, and where the service is referenced by name (scripts, group policy, shortcuts, application settings, documents with links).

## Step 2: Ask each unit the same five questions

| Question | Why it matters |
|---|---|
| How long can you be without it before work stops? | Sets the maximum outage window |
| Can you work read-only for a while? | Allows a freeze instead of an outage |
| When are your fixed peaks (closing, payroll, audits, field operations)? | Sets blackout dates |
| What is the worst thing that could go wrong for you? | Sets rollback criteria |
| Who decides for your unit during the window? | Names the approver and the contact |

Put the answers in one table (see `templates/business-unit-tolerance-matrix.csv`).

## Step 3: Turn answers into tiers

| Tier | Tolerance | Typical handling |
|---|---|---|
| T0 | No interruption | Parallel run, staged switch, no cutover window; move last |
| T1 | Minutes | Switch inside a short, announced slot with instant rollback |
| T2 | Hours, out of hours | Evening or night window |
| T3 | A day or more | Weekend window; good candidates for the pilot wave |

## Step 4: Plan waves

1. **Pilot** with a tolerant, cooperative unit and the IT team itself.
2. **Waves** of similar tolerance, so one outage window serves a whole wave.
3. **Strict units last**, after the method has been proven twice.

Choose the cutover window by the strictest unit in the wave, then check it against the blackout calendar.

## Step 5: Prepare before the window

- Build the new service and **check parity with the old one**: certificates and keys, service accounts, authentication settings, network address translation and firewall rules, mail relay permissions, names and aliases (`templates/parity-checklist.md`). Most surprises come from small differences between old and new.
- Rehearse the cutover once with real data volumes and time it.
- Write the runbook with an owner and a clock for every step (`templates/cutover-runbook-template.md`).
- Decide rollback criteria and a **point of no return** with a time, before the window starts.
- Announce early and twice, in plain language: what changes, when, what users must do beforehand, what will be unavailable, and where to get help (`templates/user-announcement-template.md`).

## Step 6: Cutover

- Freeze changes. Take a final backup and record the starting state.
- Run the runbook step by step; record the actual time of each step.
- At each go/no-go point, one named person decides. If the criterion is missed, roll back; do not extend hoping.
- Smoke-test with named test users from several units, not only from IT.

## Step 7: Hypercare

- A visible help channel for the first days, staffed by people who know the plan.
- Daily list of issues with owner and status; repeat patterns become a fix, not a hundred tickets.
- Keep the old service **read-only and intact** for an agreed period, then decommission it with a ticket and a final backup.

## Step 8: Close

Write a short review: planned versus actual times, what surprised us, what the checklist must gain. Update the template, not only your memory.

## Common mistakes

- One window for everyone, chosen for IT convenience.
- Treating the migration as a data copy and forgetting names, certificates, integrations and scheduled jobs.
- No point of no return, so the rollback decision is made late and under pressure.
- Telling users after the fact.
- Decommissioning the old service the day the new one works.
