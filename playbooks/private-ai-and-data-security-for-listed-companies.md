# Private ("closed-circuit") AI and data security in listed companies

*A design note. It describes principles and options, not any organization's setup, vendor, system or finding.*

## Why listed companies are different

A listed company handles **inside information** (results before publication, transactions, board materials), is subject to disclosure and record-keeping duties, and answers to a capital-markets regulator, auditors and personal-data law at the same time. A leak is not only a privacy event; it can be a market event. Any AI assistant that reads company documents has to be designed with that in mind.

## 1. Start from data classes, not from tools

| Class | Examples | Rule for AI use |
|---|---|---|
| Public | Published reports, website content | Any approved tool |
| Internal | Procedures, general project documents | Approved tools inside the company boundary |
| Confidential | Contracts, budgets, personal data | Private environment only; minimum data; logged |
| Restricted / inside information | Pre-release results, board and transaction papers | No assistant, or a closed environment with named users and a documented need |

The class decides which environment may see the data. Label first, then allow.

## 2. Deployment options, from most to least closed

| Option | What it means | Fit |
|---|---|---|
| Air-gapped / on-premises model | Model runs on company hardware with no outbound connection | Restricted data; highest cost and maintenance |
| Private cloud tenant | Model hosted in an isolated tenant with contractual limits on retention and training | Confidential data |
| Managed service with zero-retention terms | Provider processes requests and does not store or train on them | Internal data, after legal review |
| Public consumer tools | Anyone's personal account | Not for company data |

Whatever the option: data residency stated in writing, subprocessors known, and an exit path.

## 3. Controls that matter

- **Identity and access:** single sign-on, role-based access, named users for restricted spaces, no shared accounts.
- **Data minimization:** send only what the task needs; remove names and numbers when they are not needed.
- **Data loss prevention:** block pasting of classified material into unapproved tools; monitor, do not only forbid.
- **Retrieval, not training:** let the assistant read approved documents at question time under the user's own permissions, instead of training a model on company data.
- **Permission-aware search:** the assistant must never show a user content that the user could not open directly.
- **Logging and retention:** record who asked what and which sources were used, under a retention rule agreed with legal; logs themselves are protected.
- **Output handling:** generated text is a draft; a person reviews before it leaves the company; no automatic external sending.
- **Prompt and tool safety:** treat document content as untrusted; no tool that can send, delete or change permissions without a human approving that exact action.
- **Secrets:** never in prompts, documents or logs.
- **Insider lists:** restricted spaces follow the same list of people as the inside-information process.

## 4. Governance

1. **Policy:** an AI acceptable-use policy in plain language, with the data classes above.
2. **Approval:** a short review (security, legal, data protection) before any new AI use case or tool.
3. **Inventory:** a register of AI systems, owners, data classes, model location and review date.
4. **Risk assessment:** for each use case, what can go wrong, who is affected and what the fallback is.
5. **Training:** short, practical, repeated; include "what not to paste".
6. **Audit evidence:** register, approvals, access lists, logs, test results and incident records, ready for auditors.
7. **Incident handling:** a defined path for suspected leakage, including who decides on disclosure obligations.

## 5. Testing

- Red-team the assistant with prompts that try to extract restricted content and to bypass permissions.
- Re-run a fixed set of anonymized cases after any model, prompt or index change.
- Verify deletion: when a document is removed or a person's rights change, the assistant stops using it.

## 6. Honest limits

No setup removes risk; it makes risk visible, bounded and owned. Legal and regulatory requirements differ by country and change over time: have legal counsel confirm the obligations that apply to your company before relying on this note.
