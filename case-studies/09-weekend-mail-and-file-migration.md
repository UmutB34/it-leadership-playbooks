# Method note 9: A weekend migration of mail and files between suites

*Written from my own experience of moving a group of users from one hosted mail and file suite to another. No organization, supplier, user or date is described.*

## The situation

A group of users on one hosted suite had to move to the company's main Microsoft 365 tenant. Mail, calendars and personal files all moved. The business gave one fixed rule: the cutover happens over a single weekend, and nobody loses mail or files.

## What I wrote down first

Before any tool was installed I put the requirements in one short message to everyone involved, so that "done" meant the same thing to all of us:

1. **No lost mail, and as little interruption as possible** while the domain moves from the old suite to the new one.
2. **Calendars.** Will they move with the mailbox? Find out before the weekend, not on Monday.
3. **No lost files.** Personal drive content lands in a per-person folder structure on the company file server, not in a flat dump.
4. **Teams between the two domains** behaves like one organization (people can find and message each other), while shared mail resources wait for the later server upgrade.
5. **The date and the hour.** Friday evening start, everything finished before the working week.

Note the decision in item 3: the personal drive content went to the file server, not to cloud storage. That was deliberate, and the announcement to users said so plainly, including that old sharing links would stop working.

## The shape of the schedule

| Block | What happens |
|---|---|
| About four days before | Roadmap meetings with the supplier and the project team; user lists agreed; test accounts created |
| Friday evening | Migration tool installed, domain moved, DNS records changed, mail synchronization started |
| Saturday and Sunday | Mail catches up; users get new sign-in details; desktop setup requests are scheduled through the ticket system |
| The following week | Personal drive content copied to the file server in per-person folders; daily list of what is done and what is left |
| Closing | A short written summary to everyone, kept by every party |

One shared migration table (user, mailbox status, drive status, device status, open problem) was the single source of truth. It replaced a lot of "where are we?" messages.

## What surprised us, and what I would check earlier

- **Archive mailbox limits.** One heavy user's mailbox was close to the cloud limit just as mail started to flow. Look at the largest mailboxes before the weekend and decide whether archiving, and its auto-expansion, is switched on.
- **Test data in the tenant.** The migration tests leave data behind in test cloud storage. Delete it when the project ends.
- **Provider notifications.** The platform sends administrators a stream of service notices. Tell the support desk what they are, so nobody reports a "failure" that is only a notice.
- **Users' sharing.** Shares disappear in the move. The advance notice and a help desk that can re-create them saved a lot of calls.

## When this is part of a company separation

The same weekend pattern shows up when a business unit is split off. Two extra items belong in that plan from the start, and I added them late:

- **A domain name** for the new entity, registered early.
- **A wildcard certificate** bought and applied to the servers and the services that face the internet.

## The lesson we wrote down at the end

Test every realistic scenario for real before the cutover, and write down what to do when each problem appears. Problems that come as a surprise cost a weekend. Problems we already know about, and have a note for, cost a few minutes.

## Checklist

- [ ] Requirements written in one message and confirmed by all parties
- [ ] Calendars and shared mailboxes: decision made
- [ ] Largest mailboxes and archive limits checked
- [ ] User list and device list in one migration table
- [ ] Users told: window, what is unavailable, what they must do, what breaks
- [ ] Domain, DNS and certificate steps in the runbook, with owners
- [ ] Test data removed from the tenant afterwards
- [ ] Closing summary sent to everyone
