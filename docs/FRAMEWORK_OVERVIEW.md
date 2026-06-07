# ETC Framework — Technical Overview

> **From:** *From Cipher to Shadow* (Plesca, 2024)  
> © 2024 Ciprian Stefan Plesca. All Rights Reserved.

---

## 1. The Entropic Threat Continuum: Formal Definition

The Entropic Threat Continuum (ETC) is formally defined as a five-tuple:

```
ETC = (S, A, T, D, E)
```

| Symbol | Name | Definition |
|--------|------|------------|
| `S` | Security State Space | All possible configurations of an information system with respect to its three security axes |
| `A` | Adversarial Capability Set | The complete set of operations available to potential attackers |
| `T: S × A → S` | Threat Transition Function | Maps each (state, action) pair to a resulting security state |
| `D: S → [0,1]³` | Security Measurement Function | Maps each state to a three-dimensional vector on the ETC axes |
| `E: A → ℝ⁺` | Effort Function | Maps each adversarial action to the effort required to execute it |

---

## 2. The Three Invariant Axes

### 2.1 Confidentiality-Exposure Axis (CEA)
Measures the degree to which information that should be secret is protected from unauthorized disclosure.

- **Score = 1.0**: Perfect confidentiality; no information accessible to unauthorized parties
- **Score = 0.0**: Complete exposure; all protected information is accessible to adversaries
- **Key threats**: Eavesdropping, side-channel attacks, traffic analysis, TEMPEST, insider threats

### 2.2 Authentication-Impersonation Axis (AIA)
Measures the reliability with which identity claims within the system are verified.

- **Score = 1.0**: All identity claims are reliably verified; impersonation is infeasible
- **Score = 0.0**: No reliable identity verification; all claims are forgeable
- **Key threats**: Credential stuffing, session hijacking, social engineering of help desks, certificate authority compromise

### 2.3 Integrity-Corruption Axis (ICA)
Measures the degree to which information is protected from unauthorized modification.

- **Score = 1.0**: All information is tamper-evident and tamper-resistant
- **Score = 0.0**: Information is freely modifiable by adversaries without detection
- **Key threats**: SQL injection, BGP hijacking, supply chain compromise, DNS poisoning

---

## 3. The ETC Security Functional

The overall security posture of a system is not the average of its axis scores.
Security is **multiplicative** — catastrophic failure on any single axis can produce
overall system compromise regardless of performance on the other two.

```
S(x) = min(CEA(x), AIA(x), ICA(x)) × F(CEA(x), AIA(x), ICA(x))
```

Where `F` is a coupling function capturing security-degrading interactions between axes.
The form of `F` depends on system architecture:

- **Strongly segmented systems**: Weak coupling (F ≈ 1); axis failures have limited cross-axis effects
- **Tightly integrated systems**: Strong coupling (F < 1); failure on one axis degrades others significantly

---

## 4. Original Theoretical Constructs

### 4.1 Adversarial Entropy Gradient (AEG)

Formally defined as:

```
G(s, a) = dH(s) / dE(a)
```

Where:
- `H(s|O_t)` = conditional entropy of security state `s` given adversary observations at time `t`
- `E(a)` = cumulative effort expended in adversarial action `a`
- Sign convention: `G(s,t) = -dH(s|O_t)/dE_t` (positive when effort reduces uncertainty)

**Interpretation:**
- **High AEG**: Small adversarial effort yields large information gains → weak security posture
- **Low AEG**: Large effort yields diminishing returns → strong security posture

The AEG provides a unified account of the security value of defensive investments:
encryption, MFA, network segmentation, and threat intelligence sharing are all
investments that reshape the adversarial information landscape.

### 4.2 Trust Decay Function (TDF)

Models the degradation of authentication credential reliability over time:

```
T(c, t) = T(c, 0) × exp(−λ(c) × t) × f(B(c, t))
```

Where:
- `T(c, 0)` = initial trust value of credential `c`
- `λ(c)` = credential-specific decay constant
- `t` = time elapsed since credential creation
- `f(B(c, t))` = breach factor (captures discontinuous decay events from security incidents)

**Operational implications:**
- Password rotation intervals should be derived from `λ(c)` and current threat level, not arbitrary calendar schedules
- Systems must be designed for cryptographic agility, initiating transitions before `T(c, t)` falls below acceptable threshold

### 4.3 Threat Surface Integral (TSI)

A unified metric for organizational exposure, defined as:

```
TSI = ∫_A  V(a) × P(a) × I(a)  da
```

Where:
- `A` = set of all attack vectors available to adversaries
- `V(a)` = adversarial value of successfully executing attack `a`
- `P(a)` = probability that attack `a` succeeds given current defenses
- `I(a)` = independence normalization factor (correlated attacks discounted to avoid double-counting)

The TSI is a conceptual framework for directing security investment toward highest-exposure components,
consistent with risk-based approaches endorsed by NIST CSF and ISO 27001.

### 4.4 Layered Anonymity Stack (LAS)

A formal six-layer protocol stack for anonymous overlay networks:

| Layer | Name | Primary Function | Key Security Property |
|-------|------|------------------|-----------------------|
| 6 | Identity Management | Relates anonymized to real-world identities | Pseudonymity; linkability resistance |
| 5 | Application | Anonymized transport for application protocols | Application-layer traffic concealment |
| 4 | Routing | Selects paths providing anonymity properties | Traffic analysis resistance |
| 3 | Circuit Construction | Establishes end-to-end encrypted circuits | Forward secrecy; compartmentalization |
| 2 | Link Encryption | Per-link encryption and authentication | Hop-by-hop confidentiality |
| 1 | Physical Connectivity | Network connections between nodes | Physical infrastructure security |

Security failures at any layer can compromise anonymity properties intended to be provided by other layers.

### 4.5 Dark Topology Conjecture (DTC)

Let `G = (V, E)` be a directed graph representing an anonymous overlay network.
Let `k-anonymity(G)` denote the minimum anonymity set size achievable in `G` for a user
with a specific traffic pattern, over all possible adversary observation strategies.

**Conjecture:** `k-anonymity(G)` is bounded below by a function of the algebraic connectivity
of `G` (the second-smallest eigenvalue `λ₂` of the graph Laplacian `L(G)`), and this bound
is tight.

**Simulation support:** Across 1,000 network configurations with `n = 500` relay nodes:
- At `α = 0.20` (adversary monitoring 20% of relays): `r = 0.73`, `p < 0.001`
- At `α = 0.50` (nation-state adversary level): `r = 0.61`, `p < 0.001`
- Relationship is approximately log-linear: doubling algebraic connectivity → 1.8× increase in anonymity set size

**Status:** Conjecture; not yet formally proved for general graph families. Proof constitutes an important open problem.

---

## 5. Two Foundational Results

### 5.1 Contextual Exposure Principle (CEP)

The security value of a piece of information `i` is not intrinsic but relational:

```
V(I, C, A) = s(I) + Σⱼ δ(I, cⱼ, A)
```

Where `C = {c₁, c₂, ..., cₙ}` is the adversary's available context and `δ` is the inference
capacity increment from combining `I` with each context item `cⱼ`.

**Proof:** Since `δ(I, cⱼ, A) ≥ 0` for all `j` (information cannot decrease adversarial capacity),
`V(I, C, A) ≥ s(I)` with equality iff `I` is informationally independent of all context items. ∎

**Implication:** Existing information classification systems that assess sensitivity in isolation
systematically underestimate the security value of contextual information.

### 5.2 Opacity Migration Theorem (OMT)

For any system `S` composed of components `{C₁, C₂, ..., Cₙ}`: if opacity is removed
from component `Cᵢ` (e.g., by publishing its specification), the security properties
that depended on that opacity do not disappear — they **migrate** to other components,
typically those with less formal specification and less rigorous analysis.

**Instances:**
- Publication of cryptographic algorithms shifts vulnerability to implementation, key management, and operational layers
- Open-source software shifts opacity from code to build process, dependency chain, and deployment configuration
- As known vulnerabilities are patched, residual vulnerability migrates to the least-analyzed parts of the system

---

## 6. The Plesca Taxonomy: Structure Summary

The Plesca Taxonomy organizes attack primitives along two orthogonal dimensions:

| | Physical Level | Logical Level | Social Level | Combinatorial |
|---|---|---|---|---|
| **CEA** | TEMPEST, cold boot | Eavesdropping, side-channel | Phishing, shoulder surfing | Supply chain, insider threat |
| **AIA** | Biometric spoofing, RFID cloning | Credential stuffing, token forgery | Help desk manipulation | CA compromise, hardware implant |
| **ICA** | Hardware implants | SQL injection, BGP hijacking | Misinformation campaigns | Software supply chain (SolarWinds pattern) |

Full taxonomy: 847 discrete attack primitive types, each with associated defensive countermeasures.

---

*© 2024 Ciprian Stefan Plesca. All Rights Reserved. — Full dissertation available via repository.*
