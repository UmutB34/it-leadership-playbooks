# Standardizing IT across several sites

*How to bring three campuses or offices onto one way of working. Anonymized method from a multi-campus environment.*

## Goal

One standard stack, one directory, one backup approach and one support model across sites, so that people, spares and skills are interchangeable.

## Method

1. **Benchmark your own sites.** Compare them in numbers: servers, clients, concurrent users, storage, backup method, wireless, firewall features. A comparison between sites you already run is the cheapest benchmark you can get.
2. **Define the target stack.** Virtualization with clustering, shared storage, disk-based backup, managed wireless, one firewall family with logging.
3. **Rank by risk reduced.** Start where one change removes the most risk or cost.
4. **Join identities.** Bring user accounts into one domain structure so access, policy and support are uniform.
5. **Standardize operations.** Common naming, documentation, update rules, backup checks and support routines.
6. **Frame each change as a benefit.** Faster access for teachers, fewer outages, simpler support; not a technology list.

## Reference stack (illustrative)

| Layer | Standard |
|---|---|
| Servers | Clustered virtualization, host failure without outage |
| Storage | Shared storage with snapshots |
| Backup | Disk-based, tested restores, offsite copy |
| Wireless | Centrally managed, sized for concurrent users |
| Edge | Next-generation firewall with logging that meets local law |
| Identity | One directory and policy set |
| Remote access | VPN with a second factor, staff work from outside as if inside |

## Law and logging

Where national law requires internet-access logs with a trusted time stamp, the firewall, guest network and log store are designed together. Guest access is an identity problem: who is allowed, who is recorded, who is responsible.

## Practices that helped

- Describe the current state in numbers before recommending anything.
- Compare offers on total cost over the licence period, including how high-availability licensing works.
- Put installation and configuration scope into the offer so the price covers the work, not only the equipment.
- Hand over with documentation and a short training session.

## Measures

- Share of sites on the standard stack.
- Incidents per site and mean time to restore.
- Time to onboard a new user or device.
- Support effort per user.

## Checklist

- [ ] Inventory: servers, roles, clients, load
- [ ] Single points of failure and plan to remove them
- [ ] Backup method and last restore test
- [ ] Edge features: bought vs assumed
- [ ] Comparison table across sites
- [ ] Recommendations ranked by risk reduced
