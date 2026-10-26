# IT separation for a divested asset

*How to rebuild the IT of a business unit or plant as a standalone environment when it is sold, and hand it over turnkey. No company, buyer or system names.*

## Situation

A unit is being sold. The buyer wants the IT to work on its own from day one, often as a close copy of what the seller runs today. It must not depend on the seller's systems, and it must not carry the seller's data.

## Approach

1. **Scope and inventory.** List every service the unit uses: identity and mail, ERP and workflow, HR, document management, remote access, telephony, printing, endpoints, network, security tooling and contracts.
2. **Decide per service.** Copy it, rebuild it, keep it in transition for a while, or retire it. Record the decision and the owner.
3. **Design the standalone environment.** New identity and domain, new mail and certificates, new servers and licences, new remote access and security services, and new contracts in the unit's own name.
4. **Build in parallel.** Build and test the new environment while the old one keeps running.
5. **Plan the cutover.** Freeze changes. Keep the window short. Have a task list with owners, a rollback decision point and a communication plan for users.
6. **Move and separate data.** Filter the unit's data out of shared databases, migrate it, verify it, then remove the seller's copies.
7. **Handle in-flight business.** Complete or restart open workflows so none are left half-processed at the switch.
8. **Support after go-live.** Run a short transition period under a service agreement, with named people and an end date.
9. **Close.** Review and remove access, transfer contracts, hand over documentation and write a closing report with lessons.

## Controls that matter

- Agree an approval matrix and an access matrix for the new environment before any access is created.
- Issue third-party access by name, with an end date.
- Where the seller needs read-only access, limit it in time and then remove it.
- Buy licences for the new environment. Don't carry them over silently.
- Keep a written list of what was copied, what was rebuilt and what was retired.

## Risks and how they are handled

| Risk | Handling |
|---|---|
| Data left in the old environment | Verified deletion step with sign-off |
| Users cut off at the switch | Rehearsal, temporary access path, support desk on standby |
| Workflows half-completed | Freeze and completion rule before cutover |
| Contract gaps | Contract inventory with transfer dates |
| Scope creep | Decisions logged per service; changes need approval |

## What to measure

- Services separated versus services in scope.
- Cutover duration against plan.
- Incidents in the first two weeks.
- Open items at closing.

## Lessons

- Inventory the contracts as carefully as the systems.
- Rehearse the cutover with the people who will use the system.
- Keep the old and new environments clearly separated, in time and in access.
