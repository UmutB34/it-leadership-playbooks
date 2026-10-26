# Automating migration work and running it with AI at enterprise scale

*A design note. It describes principles and a division of labor between people, scripts and language models. No prompts, endpoints, keys, tenants or organization data.*

## The problem to solve

In a migration most of the effort is not technical. It is **human traffic**: asking owners for answers, chasing replies, sending the same announcement ten times, collecting approvals, answering "is it done yet?", and reconciling lists by hand. Automation should remove that traffic first, because it is cheaper and safer than automating the risky technical steps.

## 1. What to automate, in order

| Layer | Examples | Value | Risk |
|---|---|---|---|
| Intake and tracking | One request form; each unit's tolerance answers captured as structured data; a status board that updates itself | Fewer status questions | Low |
| Communication | Announcement drafted from the plan and sent per unit and wave; reminders on a schedule; escalation after a deadline | Less chasing | Low |
| Evidence | Permission exports, copy logs, comparison results, cutover timestamps collected automatically into one record | Audit trail for free | Low |
| Review workflows | Access review sent per owner with a simple response form; replies written back to the change record | Removes spreadsheets by email | Low to medium |
| Checks | Parity checklist run by script (certificates, names, ports, relay, jobs); post-cutover smoke tests | Fewer surprises | Medium |
| Execution | Copy, sync and switch steps as scripted, repeatable, idempotent actions with a dry-run mode | Fewer hands at night | Higher; keep a human at the go/no-go |

Rule: the higher the risk, the more the human stays at the **decision point**, not at the keyboard.

## 2. Principles for scripts

- Idempotent: running twice does no harm.
- Dry-run first, with output a person can read.
- Every action writes a line to the record: who or what, when, which object, result.
- Secrets live in a vault, never in scripts or tickets.
- The same script runs in rehearsal and in the real window.

## 3. Where a language model helps, and where it must not

**Good uses:**
- Drafting announcements and runbooks from structured plan data, in the reader's language and tone.
- Summarizing long threads and meeting notes into decisions, open questions and owners.
- Turning free-text replies from unit owners into proposed structured entries for a person to confirm.
- Explaining a failed check in plain words and proposing next diagnostic steps.
- Searching past projects and closing reviews for similar situations.
- Checking a plan against a checklist and listing gaps.

**Must not decide:**
- Security scoring and access decisions: these are deterministic rules.
- Go/no-go and rollback decisions: a named person decides.
- Anything that sends outside the organization, changes permissions or deletes data, without explicit human approval of that specific action.

## 4. Operating model for AI at enterprise scale

1. **Roles, procedures and knowledge kept apart.** Who does the work (agent roles and limits), how a repeatable task is done (procedures), and what is true (documents). Mixing them degrades all three.
2. **One front door.** People talk to one coordinating role that routes work; they do not manage ten assistants.
3. **Decision register.** Open questions carry an age and a status; nothing disappears silently.
4. **Evidence before claims.** A result is reported with the output that proves it.
5. **Gates only people can pass.** Release, approval of outward messages, permission changes.
6. **Cost modes.** Economy by default; deeper analysis only for incidents, releases and irreversible changes.
7. **Data protection by design.** Minimum data in prompts; no secrets; classification decides which model or environment may see the data; logs of what was sent and returned; retention set.
8. **Evaluation.** A small set of real, anonymized cases is re-run when a model, prompt or tool changes, and results are compared.
9. **Fallbacks.** If the model or service is unavailable, the manual path still works and is documented.
10. **Ownership.** A named owner for each automation and each agent, with a review date.

## 5. Measuring whether it works

| Measure | Direction |
|---|---|
| Messages and meetings per migration wave | down |
| Hours from request to owner reply | down |
| Share of access reviews completed on time | up |
| Manual steps in a cutover | down, while the human decision points stay |
| Incidents caused by automation | zero tolerance, reviewed |
| Time to prepare the closing review | down |

## 6. Honest limits

Automation moves effort; it does not remove accountability. A wrong announcement sent faster is still wrong. Start with the low-risk layers, prove them on one project, and widen only with evidence.
