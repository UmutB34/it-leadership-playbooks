# Mail and collaboration platform migration

*A method note for moving users from one hosted mail and file suite to another. No organization, tenant, domain or date is described.*

## Shape of the project

- Mailboxes, calendars and contacts move.
- Personal cloud files move to a managed location owned by the company.
- Shared team files are re-organized by business unit.
- Mobile devices, remote access and desktop applications are reconfigured.
- Old sharing links stop working and must be re-created.

## Method

### 1. Decide what happens to each kind of data

| Data | Typical decision |
|---|---|
| Mailbox | Migrate; keep a rule for what is archived instead |
| Personal files | Move to a personal area on managed storage; users are told where |
| Shared files | Not lifted as is; rebuilt by unit with an owner (see [file-server-and-dfs-migration.md](file-server-and-dfs-migration.md)) |
| Sharing links, internal and external | Removed by the move; users re-share with IT help |
| Mobile access | Through the managed device application |

### 2. Tell users the truth early

Say plainly: the cutover window (for example Friday evening to Monday morning), what will be unavailable, that mail may be interrupted from time to time, what they should download beforehand, which sharing will need to be redone, how to sign in afterwards and where to ask for help. Ask them to book desktop application installs through the ticket system, so the load is spread.

### 3. Prepare in layers

1. Identity and licensing first: accounts, groups, licenses, sign-in method.
2. Domain and mail flow: records, transport rules, relay permissions for applications and devices that send mail.
3. Pilot mailboxes from IT and a tolerant unit.
4. Waves of mailboxes, with delta sync before the final switch.
5. Desktop and mobile configuration.

### 4. Cutover

Lower DNS record lifetimes beforehand. At the window: stop the old service for writes, final sync, switch mail routing, validate sending and receiving in both directions, validate the personal file area and remote access, publish the sign-in details to users through a separate channel.

### 5. After

Hypercare desk for the first week. A list of recurring problems (profile rebuilds, shared mailbox access, calendar permissions, application mail relays). Keep the old service available read-only for the agreed period, then close it.

## Tolerance notes

Units with heavy calendar use, field staff on mobile only, and executive assistants need a named contact for the window. They are poor pilot candidates and good candidates for a late wave with extra support.

## Evidence

Inventory of mailboxes and applications that send mail, communication sent, the runbook with actual times, validation results, issue list and closing review.
