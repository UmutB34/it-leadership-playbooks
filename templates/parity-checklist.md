# Old versus new parity checklist

Compare the old and the new service point by point before the window. Differences found here are cheap; differences found at cutover are not.

| Area | Check | Old | New | Same? |
|---|---|---|---|---|
| Certificates | Same names, private keys imported, chain complete | | | |
| Service accounts | Same rights; passwords known and stored | | | |
| Authentication | Application pool or service identity, delegation, name aliases | | | |
| Names | Server names, aliases and their service principal names | | | |
| Network | Address translation, firewall rules, routing, load balancer targets | | | |
| Traffic proof | After repointing, real traffic reaches the new service (not the old) | | | |
| Mail | Relay permissions, send connectors, restrictions on the old mail server | | | |
| Integrations | Applications and devices that call the service | | | |
| Scheduled jobs | Tasks, backups, reports, scripts | | | |
| Monitoring | Alerts and dashboards point to the new service | | | |
| Backup | Job exists, restore tested | | | |
| Security | Antivirus exclusions, logging, access control | | | |
| Documentation | Diagram, runbook and contact list updated | | | |
