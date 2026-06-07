# Security Policy

© 2024 Ciprian Stefan Plesca. All Rights Reserved.

---

## Scope of This Document

This SECURITY.md file addresses two distinct matters:

1. **Responsible disclosure policy** for any security vulnerabilities found
   in the simulation code or other software contained in this repository.
2. **Ethical use statement** regarding the security research content of the
   dissertation itself.

---

## Reporting Security Vulnerabilities in Repository Code

If you discover a security vulnerability in the simulation code (`src/`),
configuration files, or any other executable component of this repository,
please **do not open a public GitHub Issue**.

Instead, report it privately by:

1. Opening a GitHub Issue titled `[SECURITY] Private Disclosure Request`
2. Including only the minimum information needed to establish that a
   vulnerability exists
3. Awaiting contact from the repository maintainer to establish a secure
   channel for full disclosure

The author commits to:
- Acknowledging receipt of your report within 7 days
- Providing an assessment of the report within 30 days
- Crediting responsible disclosers in any subsequent security advisories
  (unless the reporter requests anonymity)

---

## Ethical Use Statement

This dissertation analyzes information security systems — including anonymous
overlay networks, cryptographic protocols, and attack taxonomies — from a
strictly academic perspective.

**The following uses of this work are inconsistent with its intent and are
explicitly disavowed by the author:**

- Using the Plesca Taxonomy or any attack analysis in this dissertation to
  plan, execute, or facilitate unauthorized access to computer systems.
- Using the Dark Web infrastructure analysis in Part VII to facilitate
  illegal markets, criminal communication, or any activity harmful to
  individuals or organizations.
- Using theoretical constructs (AEG, TDF, TSI) to optimize offensive
  operations against real systems without authorization.

Knowledge of how systems fail is inseparable from knowledge of how systems
are protected. This dissertation is written in that tradition — for defenders,
policymakers, and scholars — not for adversaries.

---

## No Operational Details Policy

Consistent with responsible security research norms, this dissertation does
not include:

- Functional exploit code
- Specific operational techniques for attacking production systems
- Configuration details for deploying illegal services
- Instructions for conducting traffic deanonymization against real users

Any future code contributions to this repository will be held to the same
standard.

---

*© 2024 Ciprian Stefan Plesca. All Rights Reserved.*
