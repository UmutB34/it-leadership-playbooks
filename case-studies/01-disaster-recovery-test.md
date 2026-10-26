# Running a full disaster recovery test: method and checklist

*A reusable method. No organization, supplier or system is described; the examples are generic.*

## Why test

"We replicate, so we can recover" is only a belief until you have run the whole environment from the recovery site and brought it back. A full test shows dependencies that single-system tests hide. It also gives the recovery targets (RTO and RPO) real inputs instead of assumptions.

## What a full test proves

- Which applications look independent but share a login, a license or a network rule.
- That network routing and name resolution work from the recovery site, in both directions.
- That services are reachable by the people who need them, not just running.
- That users, business owners and auditors can see evidence, not only engineers.

## Options

| Option | Assessment |
|---|---|
| Table-top exercise | Cheap, useful for roles and communication, proves nothing technical |
| Test one system at a time | Hides cross-system dependencies |
| Full planned failover, then fail back | Best evidence of real recovery time and dependencies |

## Method

1. **Scope.** List every system in scope with its owner, its dependencies and its start-up order.
2. **Define "working".** Before the test, write down for each system the check that proves it works for a user.
3. **Prepare the plan.** Order of steps, people on the call, communication plan, stop criteria and a rollback decision point.
4. **Prepare the network.** Review beforehand the routing and firewall changes needed at the recovery site.
5. **Run the failover** in a controlled order, with a timekeeper and a log.
6. **Verify each system** against its definition of working, and capture evidence as you go.
7. **Fail back** and verify again. Allow time for data resynchronization.
8. **Report the same day,** then issue an action list with owners.

## Dependency categories to inventory

These are common sources of surprises in any environment:

- Service accounts and shared database logins.
- License servers and activation.
- Network routes, firewall rules and name services.
- Identity services and second-factor integrations.
- File paths and aliases that users actually rely on.
- Monitoring and logging that must follow the workload.

## Roles

Incident-style roles keep a long day under control: a test lead, technical leads per area, supplier contacts, verifiers from the business, a timekeeper and a communicator.

## Evidence

For every system, record the time, the result, the verifier and a screenshot or log. Reconstructing evidence later rarely works.

## The report

Give management one page: scope, what was confirmed, how long it took and what will be improved. Put the details for engineers in an appendix. Include a recommendation for the test cycle.

## Lessons for any team

1. Test with everyone in the room: suppliers, business verifiers and the person who decides to stop.
2. Write down what "working" means before the test.
3. Collect evidence while testing.
4. Count the dependencies you cannot see.
5. Treat the report as a product.

## Reusable checklist

- [ ] System list with owner, dependencies and start-up order
- [ ] Definition of working and verification step per system
- [ ] Routing and firewall change list, prepared and reviewed
- [ ] Service accounts and licenses inventory
- [ ] Communication plan and stop criteria
- [ ] Evidence template (screenshot, time, verifier)
- [ ] Fail-back plan with data resynchronization time estimated
- [ ] Same-day report, then an action list with owners
