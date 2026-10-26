# Method note 5: Reviewing the cost of a managed-services model

*Written from my own experience. Supplier names, amounts and service lists are left out on purpose.*

## The situation

When most of the infrastructure runs through a managed-services provider, daily work gets lighter but cost gets harder to see. There are many small lines, each one reasonable, and together they add up to a large number. They are priced per unit: per server, per bandwidth tier, per user, per terabyte.

## Typical problems

- Units accumulate over years: servers for projects that ended, capacity tiers sized for old needs, test systems nobody turned off.
- Cost is mostly fixed per service, so it does not fall when the organization shrinks.
- There is no independent view of whether the architecture is larger than the business needs.

## What I do

1. **Build a per-service view.** I list every service line with its unit, quantity and owner. The question then changes from "is the bill too high?" to "do we still need this unit?"
2. **Track one simple ratio.** IT software and service cost per employee per month, year over year. It exposes fixed costs that grow while the organization does not.
3. **Get an independent review.** A reviewer with no stake in the provider's revenue examines the architecture and the bill.
4. **Compare price, but weigh operations.** A price study of alternatives is possible. Often the operational burden of leaving costs more than the saving, so the realistic move is to renegotiate unit prices and remove units you no longer need.
5. **Link every cost to a recovery or security reason**, so removals do not weaken continuity.

## What an independent review usually suggests

- Review the server estate against actual need.
- Quantify the licence and service saving of retiring tiers that are not needed.
- Review network capacity against real use.
- Reduce special-purpose access hosts where operations allow.
- Quantify the saving of removing development and test systems that are not in use.
- Keep the provider for hosting if the service is good, but negotiate unit prices and service lines.

## Lessons

1. In a managed model, cost control is inventory control: units, owners, review dates.
2. Always have an exit-cost estimate. It makes the negotiation honest.
3. Do not trade resilience for savings without saying so in writing.
4. An outside reviewer lowers the temperature of an internal argument.
5. Report one ratio the board understands, not many line items.

## Checklist

- [ ] Service-line inventory with unit, quantity, owner and purpose
- [ ] A removal candidate list, with the risk of removing each
- [ ] Cost per employee per month, tracked yearly
- [ ] Independent review at least every two years
- [ ] Exit-cost estimate and the cost of switching
- [ ] Renegotiation calendar, before the budget cycle, not after
