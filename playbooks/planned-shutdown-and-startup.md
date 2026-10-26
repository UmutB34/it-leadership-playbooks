# Planned shutdown and startup

*A safe order for switching an IT environment off and on, for maintenance, power work, a move or a recovery exercise.*

## What I want out of it

Bring everything down without losing data. Then bring everything back up in an order where each service finds what it depends on.

## Principles

1. **Dependencies decide the order.** Shut down from the top (applications) to the bottom (storage and network). Start up in the reverse order.
2. **Write it down once, test it, keep it reachable.** The runbook has to live somewhere you can read it when systems are down.
3. **One owner and one communicator.** One person runs the steps and another tells the business.
4. **Check, don't assume.** Every step has a verification.

## Typical order

| Shutdown | Startup |
|---|---|
| 1. Announce, freeze changes, take a fresh backup | 1. Power, network core, storage |
| 2. Stop user-facing applications and queues | 2. Hypervisors and management |
| 3. Stop application servers and middleware | 3. Identity and name services |
| 4. Stop databases cleanly | 4. Databases |
| 5. Stop messaging and file services | 5. Application servers and middleware |
| 6. Stop identity and name services | 6. Messaging and file services |
| 7. Stop hypervisors, then storage | 7. User-facing applications |
| 8. Network and power last | 8. Health checks, then release to users |

## Checklists

**Before:** backup verified, contacts informed, change approved, runbook open, rollback decided.

**During:** each step confirmed, time recorded, issues logged.

**After:** service checks passed, monitoring green, users informed, notes updated.

## After a power event

Start only once storage and network are stable. Bring services up in the order above. Check data integrity before you open to users.

## Why bother

Most serious start-up problems come from the wrong order or a missing dependency note. A short, tested runbook turns a risky night into a routine one.
