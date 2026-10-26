# Infrastructure project work plan and team roster

*A method for running a multi-week infrastructure change (for example a network renewal) with a small team.*

## Goal

Make it clear every week who does what, where they work and who covers whom, so the change finishes on time without stressing the business.

## Work plan

| Phase | Typical content | Output |
|---|---|---|
| Preparation | Survey, design, order, staging, user communication | Approved design and schedule |
| Cut-over weeks | Installation, configuration, migration by area | Daily status |
| Acceptance | Tests per area against written criteria | Signed acceptance |
| Stabilization | Issue queue, tuning, documentation | Closing report |

## Weekly team roster

A simple table with the team down the side and each week across the top. For each cell mark one of:

- **Remote.** Works from home.
- **Hybrid.** Part on site, part remote.
- **Remote with on-site on demand.** Available to come in when needed.

The roster answers three questions at a glance: who is on site at the critical moments, who is the backup for each task, and when the team is thin.

## Principles

- One named owner per work package and one backup.
- Critical steps (the actual switch) always have an on-site lead.
- Remote work is planned, not accidental: connectivity and access are tested beforehand.
- A daily short status and a weekly written summary for management.
- Acceptance criteria written before the work starts.

## Risks to manage

- Single points of knowledge: the one person who understands a system.
- Overlapping leave during cut-over weeks.
- Remote access that fails when the office network is down: provide an independent path.

## Measures

- Work packages finished on plan.
- Issues found at acceptance versus after.
- Days with a gap in cover.
