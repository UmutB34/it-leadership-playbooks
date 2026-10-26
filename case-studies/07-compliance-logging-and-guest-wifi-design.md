# Method note 7: Designing a firewall, logging and guest Wi-Fi setup under a logging law

*How I approach this kind of design. No organization, supplier or price is described.*

## The situation

A site with many users needs a new internet edge: a firewall with web filtering, guest Wi-Fi that identifies who is connecting, and a log store. In Turkey the log store has to follow Law 5651, which requires internet-access logs to be kept with a trusted timestamp.

## Requirements

- A next-generation firewall: gateway antivirus, intrusion prevention, content filtering, deep inspection, bandwidth shaping, directory integration and VLAN support.
- High availability: a second device in a cluster, because internet and directory services must not stop during working hours.
- Guest Wi-Fi with identity checks (for example SMS and national-ID verification) and separate networks for staff, guests and, where approved, other groups.
- A log server that stores records in a compliant form and holds them for the required period.

## Comparing proposals

Collect several proposals and compare them on the same dimensions:

| Dimension | Why it matters |
|---|---|
| Licence model | Per-user or per-device pricing changes the cost curve as the site grows |
| HA licensing | Whether the second device needs its own subscription |
| Logging integration | Native logs versus a separate compliant log server |
| Support | Local support and response time |
| Total cost | Over the licence period, not the first-year price |

## Design

- Two firewalls in an active/passive cluster with a multi-year security subscription.
- A separate logging system sized for the expected events per second, writing timestamped records that satisfy the law.
- A hotspot system with identity checks, a limit on simultaneous guests, and separate SSIDs per group.
- A written installation and configuration scope, so the price covers the work and not only the hardware.

## Lessons

1. Compliance requirements shape the design more than speed does. Read the law's logging requirements before choosing a firewall.
2. High availability doubles hardware but not always licences. Ask early.
3. Guest Wi-Fi is an identity problem: who is allowed, who is recorded, who is responsible.
4. Compare total cost over the licence period.
5. Write the installation scope into the offer.

## Checklist

- [ ] Legal logging requirements written down
- [ ] Features required versus nice to have
- [ ] HA design and its licensing
- [ ] Logging and time-stamping design
- [ ] Guest identity and network separation
- [ ] Vendor comparison on total cost
- [ ] Installation scope and acceptance test
