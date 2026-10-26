# Migration project catalog

*A catalog of the kinds of migration and upgrade projects an IT team in a multi-site organization runs over a few years, with the tolerance and window that usually fit. It is a planning aid, not a list of real projects.*

Tolerance tiers are defined in [project-migration-method.md](project-migration-method.md).

| Project type | What moves | Typical strictest tolerance | Usual window | Rollback idea | Watch for |
|---|---|---|---|---|---|
| File server and namespace | Shares, permissions | T2 | Evening or weekend per wave | Old target kept read-only | Hard-coded paths, permissions |
| Mail platform | Mailboxes, routing | T1 to T2 | Weekend | Routing switch back | Applications that send mail |
| Mail archive upgrade | Archive servers, indexes | T3 | Weekend | Snapshot before upgrade | Long index rebuild |
| Database high availability | Databases, listeners | T1 | Out of hours | Fall back to single node | Connection strings |
| Business application upgrade | Application and database | T2 | Weekend | Restore from snapshot | Customizations, integrations |
| Virtualization platform move | Virtual machines | T1 to T2 | Rolling | Move back | Licensing, drivers |
| Backup platform change | Jobs, repositories | T3 | Any | Keep old jobs until restore proven | Retention gaps during the switch |
| Network refresh | Switches, routing, wireless | T1 | Night | Config backup, old kit on shelf | Documented links, remote sites |
| Firewall and remote access | Rules, tunnels, clients | T1 | Night | Previous config | Rules with no owner |
| Telephone system | Numbers, extensions | T1 | One evening | Trunk switch back | Reception and security desks |
| Endpoint security product | Agents, policies | T3 | Rolling | Re-enable old agent | Conflicts between agents |
| Mobile device management | Enrolled devices | T3 | Rolling | Keep old profile | Re-enrollment effort |
| Identity and directory change | Accounts, groups, sync | T1 | Night | Previous sync state | Service accounts |
| Domain or tenant consolidation | Domains, tenants | T1 to T2 | Weekend | Mail routing switch | Shared names, licenses |
| Site separation (divested asset) | Everything for one site | T2 | Planned program | Per-component rollback | Shared services nobody listed |
| Disaster recovery site move | Replication, runbooks | T3 | Planned test | Return path tested | Failback never tested |
| Service desk and monitoring tools | Tickets, assets, alerts | T3 | Any | Keep export | History and reports |
| Document and quality systems | Content, workflows | T2 | Weekend | Restore | Approval hierarchies |
| Printing and scanning | Queues, scan-to-folder | T3 | Any | Old queues kept | Scan destinations |
| Certificate and domain name changes | Certificates, DNS | T1 | Out of hours | Previous certificate | Pinned or forgotten endpoints |

## How to use it

Start from the row closest to your project, copy the template files, and replace the tolerance entries with what your units tell you. Keep the closing review for each project, so the catalog improves.
