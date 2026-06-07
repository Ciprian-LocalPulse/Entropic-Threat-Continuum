# Plesca Taxonomy — Reference Guide

> **From:** *From Cipher to Shadow*, Chapter 10 (Plesca, 2024)  
> Copyright (c) 2024 Ciprian Stefan Plesca. Released under the MIT License.

The Plesca Taxonomy organizes attack primitives along two orthogonal dimensions:
the **ETC axis targeted** and the **systemic level of the attack**.

---

## Taxonomy Structure

```
3 ETC Axes  ×  4 Systemic Levels  =  12 primary cells
Each cell subdivided by attack complexity tier (Low / Medium / High / Nation-State)
Total: 847 discrete attack primitive types
```

---

## Systemic Levels

| Level | Definition | Example domain |
|-------|-----------|----------------|
| **Physical** | Attacks requiring physical access to hardware or physical infrastructure | Hardware implants, electromagnetic emanation attacks |
| **Logical** | Attacks operating through software, network protocols, or cryptographic interfaces | SQL injection, credential stuffing, man-in-the-middle |
| **Social** | Attacks exploiting human cognitive biases and organizational social norms | Phishing, pretexting, help desk manipulation |
| **Combinatorial** | Attacks that simultaneously exploit multiple levels — not reducible to any single level | Supply chain compromise, nation-state APT operations |

---

## Primary Taxonomy Matrix

### CEA — Confidentiality-Exposure Axis Attacks
*Objective: Obtain information that should not be available to the adversary*

#### Physical Level (CEA-P)
| Code | Attack Primitive | Complexity | Primary Defense |
|------|-----------------|------------|-----------------|
| CEA-P-01 | TEMPEST / electromagnetic emanation interception | High | RF shielding, EMSEC standards |
| CEA-P-02 | Acoustic cryptanalysis (processor sound recovery) | High | Acoustic isolation, randomized computation |
| CEA-P-03 | Cold boot attack (RAM key recovery) | Medium | Full memory encryption, rapid key erasure on power loss |
| CEA-P-04 | Power analysis (SPA / DPA) | High | Constant-time implementations, power line filtering |
| CEA-P-05 | Optical emanation (monitor light recovery) | High | Physical shielding |
| CEA-P-06 | Dumpster diving (physical document recovery) | Low | Shredding policies, secure disposal |
| CEA-P-07 | Direct physical storage access (device theft) | Low | Full-disk encryption, remote wipe capability |

#### Logical Level (CEA-L)
| Code | Attack Primitive | Complexity | Primary Defense |
|------|-----------------|------------|-----------------|
| CEA-L-01 | Network eavesdropping (passive interception) | Low | End-to-end encryption |
| CEA-L-02 | Man-in-the-middle (MITM) interception | Medium | Certificate pinning, HSTS, mutual TLS |
| CEA-L-03 | Traffic analysis (metadata inference) | High | Traffic shaping, padding, mix networks |
| CEA-L-04 | Timing side-channel attack | High | Constant-time cryptographic implementations |
| CEA-L-05 | Cache side-channel (Spectre/Meltdown class) | High | Microarchitectural mitigations, process isolation |
| CEA-L-06 | SQL injection (data exfiltration variant) | Medium | Parameterized queries, least-privilege DB accounts |
| CEA-L-07 | Directory traversal / path injection | Medium | Input validation, sandboxing |
| CEA-L-08 | API key / credential exfiltration | Medium | Secrets management, credential scanning |
| CEA-L-09 | Unencrypted data at rest (opportunistic access) | Low | Storage encryption |
| CEA-L-10 | Log injection / log disclosure | Low | Log access controls, sensitive data scrubbing |

#### Social Level (CEA-S)
| Code | Attack Primitive | Complexity | Primary Defense |
|------|-----------------|------------|-----------------|
| CEA-S-01 | Phishing (credential / data harvest) | Low | MFA, security awareness training, email filtering |
| CEA-S-02 | Pretexting (impersonation for disclosure) | Medium | Verification protocols, callback procedures |
| CEA-S-03 | Shoulder surfing | Low | Privacy screens, clear desk policy |
| CEA-S-04 | Tailgating / piggybacking | Low | Mantraps, badge-only access |
| CEA-S-05 | OSINT aggregation (passive reconnaissance) | Low | Data minimization, privacy engineering |
| CEA-S-06 | Social media profiling | Low | Employee social media awareness policy |

#### Combinatorial Level (CEA-C)
| Code | Attack Primitive | Complexity | Primary Defense |
|------|-----------------|------------|-----------------|
| CEA-C-01 | Supply chain compromise (hardware) | Nation-State | Trusted hardware supply chain, component verification |
| CEA-C-02 | Supply chain compromise (software) | Nation-State | SBOM, code signing, reproducible builds |
| CEA-C-03 | Insider threat (authorized + malicious) | High | Least privilege, behavior monitoring, separation of duties |
| CEA-C-04 | Advanced persistent threat (APT) exfiltration | Nation-State | Defense in depth, EDR, network monitoring |

---

### AIA — Authentication-Impersonation Axis Attacks
*Objective: Subvert mechanisms by which systems and users verify identity*

#### Physical Level (AIA-P)
| Code | Attack Primitive | Complexity | Primary Defense |
|------|-----------------|------------|-----------------|
| AIA-P-01 | Biometric spoofing (fingerprint / face) | Medium | Liveness detection, multi-modal biometrics |
| AIA-P-02 | RFID cloning | Low | Cryptographic RFID, NFC with challenge-response |
| AIA-P-03 | Keycard / access badge copying | Low | Cryptographic badges, frequent key rotation |
| AIA-P-04 | Hardware token theft | Low | PIN-protected tokens, remote invalidation |

#### Logical Level (AIA-L)
| Code | Attack Primitive | Complexity | Primary Defense |
|------|-----------------|------------|-----------------|
| AIA-L-01 | Password brute force | Low | Account lockout, strong password policy |
| AIA-L-02 | Dictionary attack | Low | Salted hashing (Argon2id / bcrypt), MFA |
| AIA-L-03 | Credential stuffing | Medium | MFA, breach credential monitoring |
| AIA-L-04 | Password spraying | Medium | Account lockout, behavioral analytics |
| AIA-L-05 | Session hijacking (cookie theft) | Medium | Secure/HttpOnly cookies, session binding |
| AIA-L-06 | Cross-site request forgery (CSRF) | Medium | CSRF tokens, SameSite cookies |
| AIA-L-07 | OAuth token abuse | Medium | Token scoping, short-lived tokens, rotation |
| AIA-L-08 | SAML injection / assertion forgery | High | Signature verification, strict SAML parsing |
| AIA-L-09 | Kerberos ticket forgery (Golden/Silver ticket) | High | Protected Users group, Privileged Access Workstations |
| AIA-L-10 | JWT manipulation (algorithm confusion) | Medium | Strict algorithm validation, key isolation |
| AIA-L-11 | Replay attack | Medium | Nonce / timestamp validation, short token TTL |
| AIA-L-12 | Pass-the-hash | High | Credential Guard, network authentication restrictions |

#### Social Level (AIA-S)
| Code | Attack Primitive | Complexity | Primary Defense |
|------|-----------------|------------|-----------------|
| AIA-S-01 | Help desk impersonation | Low | Callback verification, knowledge-based challenges |
| AIA-S-02 | Spear-phishing (credential harvest) | Medium | MFA, anti-phishing training |
| AIA-S-03 | Vishing (voice phishing) | Medium | Verification protocols, staff training |
| AIA-S-04 | SIM swapping | Medium | Account PINs, SIM lock, hardware tokens |
| AIA-S-05 | Executive impersonation (BEC) | High | Out-of-band verification for financial requests |
| AIA-S-06 | Identity document fraud | High | Document verification services |

#### Combinatorial Level (AIA-C)
| Code | Attack Primitive | Complexity | Primary Defense |
|------|-----------------|------------|-----------------|
| AIA-C-01 | Certificate authority compromise (DigiNotar pattern) | Nation-State | CAA records, CT monitoring, multi-path validation |
| AIA-C-02 | Hardware token seed theft (RSA SecurID 2011 pattern) | Nation-State | Air-gapped seed storage, post-compromise rotation |
| AIA-C-03 | Authentication infrastructure supply chain attack | Nation-State | Hardware attestation, trusted supply chain |

---

### ICA — Integrity-Corruption Axis Attacks
*Objective: Introduce false information or corrupt existing information*

#### Physical Level (ICA-P)
| Code | Attack Primitive | Complexity | Primary Defense |
|------|-----------------|------------|-----------------|
| ICA-P-01 | Hardware implant (persistent firmware modification) | Nation-State | Firmware attestation, secure boot, supply chain security |
| ICA-P-02 | Physical record modification | Low | Physical security, tamper-evident media |
| ICA-P-03 | Storage media corruption (degaussing / physical damage) | Low | Redundancy, immutable backups |

#### Logical Level (ICA-L)
| Code | Attack Primitive | Complexity | Primary Defense |
|------|-----------------|------------|-----------------|
| ICA-L-01 | SQL injection (data modification) | Medium | Parameterized queries, WAF, DB integrity checks |
| ICA-L-02 | Cross-site scripting (XSS) | Medium | CSP, output encoding, input validation |
| ICA-L-03 | XML External Entity (XXE) injection | Medium | Disable external entity processing |
| ICA-L-04 | DNS poisoning / cache poisoning | High | DNSSEC, DNS-over-HTTPS/TLS |
| ICA-L-05 | BGP hijacking | High | RPKI, BGPsec, route monitoring |
| ICA-L-06 | Software update mechanism compromise | High | Code signing, update integrity verification |
| ICA-L-07 | Log tampering / deletion | Medium | Write-once logs, remote log shipping |
| ICA-L-08 | Man-in-the-middle data modification | Medium | End-to-end integrity (MACs, digital signatures) |

#### Social Level (ICA-S)
| Code | Attack Primitive | Complexity | Primary Defense |
|------|-----------------|------------|-----------------|
| ICA-S-01 | Deliberate misinformation campaigns | Medium | Source verification, information governance |
| ICA-S-02 | Fraudulent certification / false documentation | Medium | Independent verification, trusted registries |
| ICA-S-03 | Insider data manipulation | Medium | Separation of duties, audit logs, integrity monitoring |

#### Combinatorial Level (ICA-C)
| Code | Attack Primitive | Complexity | Primary Defense |
|------|-----------------|------------|-----------------|
| ICA-C-01 | Software supply chain attack (SolarWinds pattern) | Nation-State | SBOM, build integrity, network monitoring for anomalous traffic |
| ICA-C-02 | Cryptographic standard subversion (BULLRUN/Dual_EC pattern) | Nation-State | Open standards, cryptographic agility, diverse implementations |
| ICA-C-03 | AI training data poisoning | High | Training data provenance, adversarial robustness testing |

---

## Theoretical Value of the Plesca Taxonomy

Unlike taxonomies organized by attack stage (reconnaissance → initial access → execution,
per MITRE ATT&CK), the Plesca Taxonomy makes **structural relationships visible**:

A phishing attack (AIA-S), a man-in-the-middle attack (AIA-L), and a seal-tampering
attack (AIA-P) are all Authentication-Impersonation axis attacks. They share a common
**defensive logic** despite technical dissimilarity: all are defended by strengthening
the authentication mechanism at the appropriate systemic level.

This cross-level structural insight is the primary theoretical contribution of the
taxonomy over existing frameworks.

---

*Full definitions of all 847 attack primitive types are available in the supplementary*
*technical report. The summary table above covers the primary cells at the*
*Low-through-High complexity tiers. Nation-State tier primitives are defined but*
*not exhaustively listed here.*

*Copyright (c) 2024 Ciprian Stefan Plesca. Released under the MIT License.*
