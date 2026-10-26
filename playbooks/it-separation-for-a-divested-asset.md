# IT separation for a divested asset

*A method for rebuilding the IT of a business unit or plant as a standalone environment when it is sold, and handing it over turnkey. No company, buyer or system names.*

## Situation

A unit is being sold. The buyer wants the IT environment to work independently on day one, often as a close copy of what the seller runs today, without dependence on the seller's systems and without leaving the seller's data behind.

## Approach

1. **Scope and inventory.** List every service the unit uses: identity and mail, ERP and workflow, HR, document management, remote access, telephony, printing, endpoints, network, security tooling, contracts.
2. **Decide per service.** Copy, rebuild, transition for a time, or retire. Record the decision and the owner.
3. **Design the standalone environment.** New identity and domain, new mail and certificates, new servers and licences, new remote access and security services, new contracts in the unit's own name.
4. **Build in parallel.** The new environment is built and tested while the old one keeps running.
5. **Plan the cutover.** A freeze on changes, a short window, a task list with owners, a rollback decision point, and a communication plan for users.
6. **Move and separate data.** Filter the unit's data from shared databases, migrate it, verify it, then remove the seller's copies.
7. **Handle in-flight business.** Complete or restart open workflows so none are left half-processed at the switch.
8. **Support after go-live.** A short transition period under a service agreement, with named people and an end date.
9. **Close.** Access reviewed and removed, contracts transferred, documentation handed over, a closing report with lessons.

## Controls that matter

- An approval matrix and an access matrix for the new environment, agreed before access is created.
- Third-party access issued by name, with an end date.
- Read-only access for the seller where needed for a limited time, then removed.
- Licences bought for the new environment, not carried over silently.
- A written list of what was copied, what was rebuilt and what was retired.

## Risks and how they are handled

| Risk | Handling |
|---|---|
| Data left in the old environment | Verified deletion step with sign-off |
| Users cut off at the switch | Rehearsal, temporary access path, support desk on standby |
| Workflows half-completed | Freeze and completion rule before cutover |
| Contract gaps | Contract inventory with transfer dates |
| Scope creep | Decisions logged per service; changes need approval |

## What to measure

- Services separated vs services in scope.
- Cutover duration against plan.
- Incidents in the first two weeks.
- Open items at closing.

## Lessons

- Inventory the contracts as carefully as the systems.
- Rehearse the cutover with the people who will use the system.
- Keep the old and new environments clearly separated in time and in access.
