# Method note 4: Responding to an external IT audit

*Written from my own experience with external audits. Names, findings, ratings and numbers are left out on purpose.*

## The situation

An external audit ends with a report: a list of recommendations ranked by priority, usually opening with the things you do well. What happens next depends on how IT answers. The report can become a plan, or it can become months of friction.

## What usually goes wrong

- Defending the current state instead of agreeing on what to change.
- Promising everything with no owner, no date and no cost.
- Answering each recommendation alone when several share one root cause.
- Letting the response live in e-mails, so months later nobody knows what was agreed.

## What I do

I put the whole report into **one tracking sheet**, one row per recommendation. The auditor's columns stay as they are, and mine sit next to them:

| Auditor's columns | Our columns |
|---|---|
| Finding, rating, current state, risk, recommendation, responsible units | Responsible person (named) |
| | Action plan and comments |
| | Internal or external resource |
| | Notes on the solution actually applied |
| | Cost and currency, or "decision needed" |
| | Duration |
| | Target date, actual completion date |
| | Status: OK, NOT OK, waiting for a decision |

Rules:

1. **One owner per row.** A shared owner is no owner.
2. **Link recommendations to work that already exists.** Where one matches a planned project, the audit supports existing work instead of creating new work.
3. **Say "not yet" with a date.** Where a control does not exist, give the plan, the dependency and the decision needed from senior management.
4. **Price the expensive ones honestly.** If it needs spending outside the yearly budget, say so and ask for a decision.
5. **Separate policy gaps from tool gaps.** Classification, risk ownership and approval rules are ownership questions, not purchases.
6. **Keep every claim verifiable:** a date, a record, a screenshot.

## Typical response patterns (generic)

| Recommendation area | Pattern |
|---|---|
| Awareness | Often "you do it but cannot prove it": automate assignment and completion tracking |
| Change management with external developers | Written change types and approval, testing on a test system, approval by the requesting business unit, change records in the service desk |
| Privileged access | Reviews on a fixed cadence, vendors through a controlled access path with a second factor, naming standards for service accounts |
| Continuity | A real recovery test first, then targets derived from measured recovery times |
| Suppliers | Documented selection criteria beyond price, and a periodic supplier evaluation |

## Lessons

1. Treat the report as a project plan, not a verdict.
2. Connect recommendations to work that already has a sponsor and budget.
3. A recommendation often means "you do this but cannot prove it".
4. Review the sheet monthly. The closing date is the metric an auditor trusts.

## Template

```text
Finding / rating / risk (copied from the report)
Owner (one named person)
Action (what exactly will change)
Resource: internal or external
Cost and currency (or "decision needed")
Target date / actual date
Evidence that will prove it
Status: OK / NOT OK / waiting for decision
```
