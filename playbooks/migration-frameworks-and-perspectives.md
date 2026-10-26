# Migration practice against common frameworks, and from four viewpoints

*A reading aid, not a certification claim. It maps the migration method in this repository to the vocabulary of widely used frameworks, then asks what each viewpoint gains and what could be improved. No organization data.*

## 1. Where the method sits in common frameworks

| Step in the method | ITIL 4 practice | COBIT 2019 | PMBOK (project management) | CISSP domain | ISO/IEC 27001:2022 Annex A |
|---|---|---|---|---|---|
| Inventory and dependencies | Service configuration management | BAI10 Managed Configuration | Planning performance domain | Asset Security | 5.9 Inventory of assets |
| Unit tolerance questions | Relationship management, Business analysis | APO08 Managed Relationships | Stakeholder engagement | Security and Risk Management | 5.4 Management responsibilities |
| Tiers, waves and windows | Release management, Deployment management | BAI07 Managed IT Change Acceptance and Transitioning | Delivery and schedule planning | Security Operations | 8.32 Change management |
| Parity checklist and rehearsal | Service validation and testing | BAI07 | Quality and risk management | Security Assessment and Testing | 8.29 Security testing in development and acceptance |
| Runbook, go/no-go, rollback | Change enablement | BAI06 Managed IT Changes | Risk and uncertainty, change control | Security Operations | 8.32 |
| Announcements and hypercare | Organizational change management, Service desk | BAI05 Managed Organizational Change | Communications, stakeholder engagement | Security Operations | 6.3 Awareness and training |
| Access review by owner | Information security management | DSS05 Managed Security Services | Governance | Identity and Access Management | 5.15 Access control, 5.18 Access rights |
| Backup, restore proof, failback | Service continuity management | DSS04 Managed Continuity | Resilience | Security Operations | 8.13 Information backup, 5.30 ICT readiness for continuity |
| Closing review and catalog update | Continual improvement | MEA01 Managed Performance and Conformance Monitoring | Lessons learned | Security and Risk Management | 10.1 Continual improvement |

Reading the table: the method is a practical, day-to-day expression of change enablement, release and deployment management, organizational change and continuity. The frameworks add governance, evidence and vocabulary; the method adds the concrete questions and templates.

## 2. Four viewpoints

### The person doing the field operation
**Gains:** a runbook with times and owners, a rehearsal, a clear rollback point, fewer surprises from old-versus-new differences.
**Risks that remain:** night and weekend load on a small team; knowledge held in one head; rehearsal skipped under time pressure.
**Improve:** pair every cutover (one drives, one watches the clock and the checklist); record actual durations to make the next estimate honest; rotate who leads.

### The employer and the business units
**Gains:** disruption is negotiated, not imposed; each unit knows its window and its contact; owners confirm access instead of IT guessing; an audit trail exists.
**Risks that remain:** units under-state their peaks; "no reply" read as approval; migration benefits not tied to a business outcome.
**Improve:** put the unit's blackout dates in a shared calendar; state the business outcome of each project (cost, risk, speed) in one line at the start and check it at closure; use a defined default for non-replies.

### The security and audit view
**Gains:** change records, access review evidence, tested restore, decommission tickets.
**Risks that remain:** temporary exceptions that never expire; old data kept "just in case"; service accounts and certificates that nobody owns.
**Improve:** every exception has an expiry date; retention for old systems is decided at project start; each service account and certificate has a named owner.

### The whole-organization and future view
**Gains:** a repeatable method shortens later projects; a catalog turns separate projects into a portfolio; lessons feed templates.
**Risks that remain:** many small migrations create a patchwork; the catalog goes stale; people leave and the method goes with them.
**Improve:** review the portfolio yearly for consolidation and retirement; keep the templates under version control; write the closing review in two pages, not twenty; measure a few things consistently.

## 2b. Which lens for which question

No single framework covers a head of IT. Each one answers a different question, and trouble starts when one lens is used for all of them.

| Question | Lens that fits best | What it gives | What it does not give |
|---|---|---|---|
| How do we run this service day to day? | ITIL 4 | Practices for change, incident, release, continuity, improvement | Board-level accountability, deep security design |
| How do we show the board and auditors that IT is governed? | COBIT 2019 | Objectives, ownership, performance measures, evidence | Step-by-step operating method |
| Is the security decision sound? | CISSP vocabulary, ISO/IEC 27001 | Risk thinking, architecture, access, operations, a control catalog | Project scheduling or service operations detail |
| How do we deliver this as a project? | PMBOK or PRINCE2 | Stakeholders, schedule, risk, change control, closure | Technical correctness |

A workable habit: look at every significant job in the same four steps. (1) What business outcome does it serve? (2) What is the risk and who owns it? (3) What happens to the service while we do it, and how do we get back? (4) What evidence will exist afterwards?

## 2c. Where viewpoints usually disagree (gaps)

| Gap | Typical symptom | How to close it |
|---|---|---|
| Operations versus security | Security asks for a control that breaks a workflow; operations postpones it | Agree a tolerance tier and a date, with an owner for any exception |
| IT versus business unit | IT picks the window; the unit has a peak that week | Ask the five tolerance questions first |
| Project versus service | The project closes, nobody owns the new service | Name the service owner and runbook before go-live |
| Governance versus delivery | Reports show green while teams struggle | Add a few measured indicators, and review the closing report honestly |
| Framework versus practice | Processes exist on paper, nobody follows them | Fewer processes, each with an owner and a measured result |
| Short-term cost versus long-term risk | Cheapest option chosen, exit costs ignored | State the exit cost and the rollback cost in the decision paper |

## 2d. Standards to read first for this kind of role

- ITIL 4 (service management practices), for the operating vocabulary.
- COBIT 2019 (governance and management objectives), for board and audit conversations.
- ISO/IEC 27001 and 27002, as the usual security management reference for audits.
- NIST Cybersecurity Framework, as a common risk language, especially outside Turkey.
- PMBOK (or PRINCE2), for project delivery.
- CISSP common body of knowledge, as a broad security management reference even without the certificate.

## 3. A short measurement set

| Measure | Why |
|---|---|
| Planned versus actual cutover duration | Honest estimates |
| Rollbacks invoked, and why | Quality of preparation |
| Incidents in the first week per 100 users | Hypercare load |
| Share of access reviews answered on time | Ownership |
| Time from go-live to decommission of the old service | Cost and risk of leftovers |
| Lessons added to templates | The method improves |

## 4. Honest limits

This mapping is a vocabulary aid. It does not replace reading the frameworks, and it does not claim a certification or an assessment result. Framework identifiers are quoted from public documentation and should be checked against the current edition before use in a formal document.
