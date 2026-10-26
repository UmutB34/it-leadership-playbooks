# Security hardening baseline

*A layered set of controls for a company of a few hundred people. Generic and vendor-neutral.*

The aim is simple: make the common attacks fail, or at least make them visible, using controls a small team can run every day.

## Layers

| Layer | Baseline control |
|---|---|
| Identity | Multi-factor authentication for everyone; separate admin accounts; privileged access through a controlled path; joiner, mover, leaver process |
| Endpoint | Disk encryption, managed devices, endpoint protection, update rings, local admin rights removed |
| E-mail | Sender authentication (SPF, DKIM, DMARC), a mail gateway, attachment and link protection, a report-phishing button |
| Network | Segmentation, default-deny between zones, VPN with a second factor, guest isolation, DNS filtering |
| Applications | Web application and denial-of-service protection for internet-facing services, secure configuration, regular patching |
| Data | Classification, data loss prevention for the most sensitive data, encrypted backups with an offline copy |
| Mobile | Device management for mail and files, remote wipe |
| Monitoring | Central logging, alerts reviewed daily, log retention per legal requirement |
| People | Short yearly awareness training, first-week training for new joiners, regular phishing simulations |
| Response | A written incident plan with contacts, a decision tree and an exercise each year |

## How to roll it out

1. Measure first. Find out which controls exist and where the gaps are.
2. Pick the top five by risk reduced for effort spent.
3. Change one thing at a time, with a pilot group and a rollback.
4. Tell people why, in plain language, before the change.
5. Measure again and report the movement.

## What good looks like

- Every control has an owner and a check.
- Exceptions have an end date.
- The baseline is reviewed after each test or incident, and updated.

## Measures

- Multi-factor coverage.
- Encrypted device share.
- Mean time to patch critical issues.
- Phishing report rate and click rate over time.
- Open findings by age.

## Compliance links

The baseline maps to common frameworks (ISO/IEC 27001 controls, NIST Cybersecurity Framework, CIS Controls) and to national data protection requirements. That way one set of evidence serves several reviews.
