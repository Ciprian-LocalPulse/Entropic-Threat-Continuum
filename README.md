# From Cipher to Shadow: A Unified Theoretical Framework for Information Security

**From Its Epistemic Origins to the Architecture of the Dark Web**

> A Doctoral Dissertation — Department of Electrical Engineering and Computer Science  
> Author: **Ciprian Stefan Plesca** | Year: **2024**

[![License: All Rights Reserved](https://img.shields.io/badge/License-All%20Rights%20Reserved-red.svg)](./LICENSE)
[![DOI](https://img.shields.io/badge/DOI-Pending%20Assignment-lightgrey.svg)](#citation)
[![Support](https://img.shields.io/badge/Support-Donate-yellow.svg)](#support--donations)

---

## Abstract

This dissertation proposes the **Entropic Threat Continuum (ETC)** — a novel unified theoretical framework for information security that traces the discipline from its earliest conceptual antecedents in pre-mathematical secrecy to the contemporary architecture of anonymous overlay networks, including the Dark Web.

Where prior scholarship has addressed individual domains of information security in isolation (cryptography, network security, malware science, digital forensics, or clandestine network topology), no existing work has attempted a coherent philosophical and technical synthesis accounting for the epistemic, mathematical, social, and infrastructural forces that have cumulatively shaped the field.

The ETC framework models information security not as a collection of discrete technological solutions but as a **dynamic, adversarial continuum** governed by three invariant axes:

| Axis | Symbol | Description |
|---|---|---|
| Confidentiality-Exposure Axis | CEA | Protection of information from unauthorized disclosure |
| Authentication-Impersonation Axis | AIA | Reliability of identity verification mechanisms |
| Integrity-Corruption Axis | ICA | Protection of information from unauthorized modification |

---

## Original Theoretical Contributions

This dissertation introduces five original theoretical constructs:

1. **Adversarial Entropy Gradient (AEG)** — A thermodynamic model of the relationship between information concealment effort and information extraction effort, formally defined as the rate of change of adversarial uncertainty with respect to effort expended.

2. **Trust Decay Function (TDF)** — A temporal model of authentication credential reliability degradation, incorporating both continuous exponential decay and discrete breach events.

3. **Dark Topology Conjecture (DTC)** — A graph-theoretic characterization of anonymous network resilience, conjecturing a formal relationship between algebraic network connectivity and achievable anonymity set size.

4. **Layered Anonymity Stack (LAS)** — A formal six-layer protocol-stack model for onion-routed anonymous networks, analogous to the OSI model for standard networking.

5. **Threat Surface Integral (TSI)** — A unified line-integral metric for organizational security exposure quantification across all attack vectors.

Additionally, the dissertation formally states:
- **Contextual Exposure Principle (CEP)** — The security value of information is relational, not intrinsic.
- **Opacity Migration Theorem (OMT)** — Removing opacity from one system component migrates, rather than eliminates, residual vulnerability.
- **Plesca Taxonomy** — The first attack classification system organized by ETC axis and systemic level, comprising **847 discrete attack primitive types**.

---

## Dissertation Structure

```
PREFACE: The Grammar of Secrets

PART I   — Epistemological Foundations of Secrecy           (Chapters 1–3)
PART II  — The Mathematical Crystallization of Secrecy      (Chapters 4–6)
PART III — The Networked Security Paradigm                  (Chapters 7–9)
PART IV  — Attack Vectors and Defensive Architectures       (Chapters 10–12)
PART V   — The Human and Organizational Dimension           (Chapters 13–15)
PART VI  — The Entropic Threat Continuum: A Unified Framework (Chapters 16–19)
PART VII — Anonymous Networks and the Dark Web              (Chapters 20–24)
PART VIII— Implications and Future Directions               (Chapters 25–27)

BIBLIOGRAPHY
APPENDICES
```

---

## Empirical Contributions

- **Corpus analysis** of 12,000+ historical ciphers across fourteen civilizations
- **Graph-theoretic model** of Tor network topology derived from archived relay consensus data
- **Simulation study** of anonymity degradation under adversarial deanonymization (n = 1,000 configurations, r = 0.73 correlation between algebraic connectivity and anonymity set size)
- **Plesca Taxonomy**: 847 discrete attack primitives organized along the ETC framework

---

## Repository Contents

```
plesca-dissertation-repo/
├── README.md                        ← This file
├── LICENSE                          ← Full copyright notice
├── CITATION.cff                     ← Machine-readable citation metadata
├── CONTRIBUTING.md                  ← Contribution and errata guidelines
├── CODE_OF_CONDUCT.md               ← Community standards
├── SECURITY.md                      ← Responsible disclosure policy
├── DONATE.md                        ← Support & donation information
│
├── docs/
│   ├── FRAMEWORK_OVERVIEW.md        ← ETC framework technical summary
│   ├── TAXONOMY_REFERENCE.md        ← Plesca Taxonomy reference guide
│   ├── FORMAL_DEFINITIONS.md        ← Mathematical definitions of all constructs
│   └── GLOSSARY.md                  ← Key terms and notation
│
├── src/
│   ├── simulation/
│   │   ├── README.md                ← Simulation setup instructions
│   │   ├── dtc_simulation.py        ← Dark Topology Conjecture simulation
│   │   ├── aeg_model.py             ← Adversarial Entropy Gradient model
│   │   └── requirements.txt         ← Python dependencies
│   └── taxonomy/
│       └── plesca_taxonomy.json     ← Machine-readable taxonomy data
│
├── assets/
│   └── figures/                     ← Diagrams and figures referenced in text
│
└── citation/
    └── bibtex.bib                   ← BibTeX citation entry
```

---

## Citation

If you use this work in academic research, please cite it as follows:

**APA:**
```
Plesca, C. S. (2024). From cipher to shadow: A unified theoretical framework for information security from its epistemic origins to the architecture of the Dark Web [Doctoral dissertation]. Department of Electrical Engineering and Computer Science.
```

**BibTeX:** See [`citation/bibtex.bib`](./citation/bibtex.bib) or [`CITATION.cff`](./CITATION.cff).

---

## Support & Donations

This research was conducted independently and represents years of sustained scholarly inquiry. If this work has been valuable to you — whether in academic research, professional practice, security engineering, or policy analysis — please consider supporting future research.

**Donations are gratefully accepted via:**

| Platform | Address / Link |
|---|---|
| PayPal | [paypal.me/agentflowenterprise](https://paypal.me/agentflowenterprise) 
| Bitcoin (BTC) | `bc1qf3yy0w8z37rwavxpu38wem3yffpanw7wzj32qj`  |
| Ethereum (ETH) | `0x27d9a6a5b8507e6031bb044319410da96222d402`  |
| GitHub Sponsors | [github.com/sponsors/CiprianPlesca](https://github.com/sponsors/Ciprian-LocalPulse) |

See [`DONATE.md`](./DONATE.md) for full details on how donations are used.

> All donations are used solely to support ongoing research in information security theory, privacy engineering, and post-quantum cryptography.

---

## Ethical Statement

This dissertation examines the architecture, history, and theoretical foundations of information security systems — including anonymous networks — for strictly academic purposes. No portion of this work provides operational details that could enable harmful activities. All research was conducted in accordance with applicable institutional and legal guidelines. The author strongly opposes any use of this work to facilitate illegal or harmful activity.

---

## License

© 2024 Ciprian Stefan Plesca. **All Rights Reserved.**

This work is protected by copyright. Reproduction, distribution, or derivative works require explicit written permission from the author. Academic citation is permitted and encouraged. See [`LICENSE`](./LICENSE) for the full copyright notice.

---

## Contact

For academic correspondence, permissions requests, errata, or collaboration inquiries:

- **Author:** Ciprian Stefan Plesca
- **Repository Issues:** Please use the [GitHub Issues](../../issues) tab for errata and technical questions.
- **Permissions:** For reproduction or derivative work permissions, open an issue tagged `[permissions-request]`.
