# Method note 8: Comparing sites to set an infrastructure baseline

*How I compare sites. No organization, site, model, address or count is described.*

## The idea

If an organization runs several sites, the cheapest benchmark is the comparison between the sites you already own. One consistent assessment shows where each site differs from the others, and what a common baseline should look like.

## Method

1. **Define the dimensions once** and apply them to every site:

| Dimension | Questions |
|---|---|
| Compute | Physical or virtual, roles, capacity, lifecycle |
| Storage | Local or shared, capacity growth |
| Resilience | Single points of failure, failover, how a host failure is handled |
| Backup | Method, target, last restore test |
| Network edge | Capabilities licensed versus assumed; remote access |
| Wireless and switching | Coverage, capacity, growth headroom |
| Identity and access | Directory, remote access, authentication |
| Operations | Monitoring, documentation, who can maintain it |

2. **Describe the current state in numbers inside your own records** (servers, clients, concurrent users) before recommending anything. Do not publish the numbers outside the organization.
3. **Build one comparison table across sites.** Differences become visible without argument.
4. **Frame each recommendation as a problem it solves** for staff or users, not as a technology.
5. **Rank by risk reduced** and by effort, then agree a common baseline and a migration order.
6. **Re-run the comparison yearly.** The baseline moves.

## Typical recommendation themes

- Virtualize where it is not done, so new systems are cheap and fast to build.
- Use clustered hosts and shared storage so a host failure is not an outage.
- Move backups from legacy media to disk-based targets with tested restores.
- Align the network core capacity with real traffic.
- Provide secure remote access with proper authentication for people who work outside.

## Lessons

- Start with what you already own; you do not need an external benchmark to see the gap.
- A site-by-site table ends many arguments.
- Standardization is the quiet result: each later site converges on the baseline.

## Checklist

- [ ] Same assessment dimensions for every site
- [ ] Single points of failure listed per site
- [ ] Backup method and last restore test per site
- [ ] Network edge: licences actually bought versus features assumed
- [ ] One comparison table
- [ ] Recommendations ranked by risk reduced
