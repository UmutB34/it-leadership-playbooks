# Telephone system separation and cutover

*A method note for splitting a shared telephone system into two, or moving to a new platform. No numbers, sites or supplier names.*

## What makes it different

Telephony is visible to every user and to every caller. The cutover is short, but the preparation is long: numbers, announcements, gateways and integration with the collaboration platform all have to be ready on the same evening.

## Typical timeline

| Phase | Duration (typical) |
|---|---|
| Call-manager servers installed | a few days |
| Gateways and trunks installed | a couple of days |
| System, extension and phone configuration | about a day |
| Tests, including inbound and outbound calls from outside | a couple of days |
| Cutover and observation | one evening and the following day |

## Method

1. **Number plan.** List external numbers, extensions, groups, hunt lists, auto-attendants, fax lines and any numbers used by alarms or lifts. Decide which move and which are forwarded.
2. **Forward, then retire.** Keep the old main number forwarded to the new one for a period after the move so callers are not lost; plan when the forward ends.
3. **Announcements.** Prepare the welcome message text with the business owner in advance; the recording is part of the runbook, not an afterthought.
4. **Emergency and safety numbers.** Test them explicitly.
5. **Integration.** Plan the link to the collaboration platform as a separate step after the main cutover, with its own budget line.
6. **Test script.** Inbound from mobile and landline, outbound, transfer, voicemail, groups, call forwarding, conference.
7. **Cutover evening.** Switch trunks at the agreed time; run the test script; keep the old system powered, not removed, until the observation day passes.
8. **Hypercare.** A list of extensions that do not ring, and phones that need re-registration; fix daily.

## Tolerance notes

Reception, security desks and operations rooms have no tolerance for a dead main line. Give them a mobile fallback number for the window and call them first during testing.

## Evidence

Number plan before and after, test results, approvals for the announcement text, cutover record with times, and the date the forward was removed.
