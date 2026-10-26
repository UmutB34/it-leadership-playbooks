# File server and DFS namespace migration

*A method note. No organization names, server names, paths or counts.*

## Goal

Move shared folders to new storage or a new server without users noticing more than a short, announced interruption, and use the move to put access control on a footing that business owners can actually review.

## Use a namespace, not server names

Users and applications should reach shares through a namespace path (for example a domain-based DFS namespace) instead of a server name. A migration then becomes: add the new location as a folder target, synchronize, switch which target users are sent to, retire the old target. Nobody remaps a drive.

Where namespaces were never used, introduce them first, as a separate low-risk change, before moving any data.

## Plan by unit tolerance

Group shares by owning unit and rate each unit with the tolerance questions in [project-migration-method.md](project-migration-method.md). Move shares in waves; the cutover window of a wave is set by its strictest unit. Units with month-end or audit peaks are scheduled around them.

## Steps

1. **Inventory shares:** owner, size, file count, largest and deepest paths, open-file patterns, quotas, shadow copy and backup settings.
2. **Clean before you move:** agree with owners what can be archived or deleted. Moving less is the cheapest optimization.
3. **Find hard-coded references:** logon scripts, group policy drive maps, shortcuts, application configuration, documents and spreadsheets with links, scheduled jobs, scanners that save to a share, printers and multifunction devices.
4. **Prepare the target:** same or larger capacity, permissions model decided, antivirus exclusions, backup job, monitoring and quotas ready.
5. **Seed the data** ahead of time with a copy tool that preserves timestamps and permissions, and keep the log.
6. **Synchronize deltas** until the last pass takes minutes.
7. **Cutover window:** announce a freeze; make the source read-only; run the final delta; compare file counts, sizes and a sample of checksums; compare permission exports of source and target; add the new folder target and disable the old one; test as users from several units.
8. **Keep the old data** read-only for an agreed period, then archive and remove it with a ticket.

## Permissions during the move

Do not copy years of accumulated, per-person permissions blindly. Move to **groups per folder and role** (for example read and modify groups per top-level folder), owned by the business unit, and use the migration to run an owner review ([file-access-review-by-owner.md](file-access-review-by-owner.md)). Keep share-level permissions simple and put control in the file-system permissions.

## Rollback

Because the old target is still intact and read-only, rollback is: re-enable the old target, make it writable, and copy back changes made on the new one since the switch. Decide in advance up to what time this is acceptable and who calls it.

## Checks that catch most problems

- Long paths and special characters copied correctly.
- Ownership, inheritance and explicit permissions identical where intended.
- Files that were open during the final copy.
- Name-based access still working for tools that bypass the namespace: keep a DNS alias to the new server for a transition period, and make sure the alias works with the authentication method in use.
- Backup jobs and restore tests point to the new location, and a restore has actually been tried.
- Previous versions, quotas and search behave as before.

## Evidence to keep

Inventory, owner approvals, copy logs, comparison results, permission exports before and after, the cutover record with actual times, and the decommission ticket.
