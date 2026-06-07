# Glossary of Key Terms and Notation

> **From:** *From Cipher to Shadow* (Plesca, 2024)  
> © 2024 Ciprian Stefan Plesca. All Rights Reserved.

Terms are defined as used in the ETC framework. Where a term has a standard
definition in the prior literature that this dissertation adopts without
modification, the original source is noted.

---

## A

**Adversarial Capability Set (A):** The complete set of operations available to
potential attackers in a given threat model. A component of the ETC five-tuple.

**Adversarial Entropy Gradient (AEG):** Original construct (Plesca, 2024). The rate
at which adversarial effort reduces the adversary's uncertainty about the security
state of a target system. Formally: `G(s,t) = −dH(s|O_t)/dE_t`. High AEG indicates
weak security; low AEG indicates strong security.

**AEG-secure:** A system in state `s` at time `t` such that `G(s,t) < ε` for some small
threshold `ε > 0`. Additional adversarial effort yields negligible information.

**AEG-insecure:** A system in state `s` at time `t` such that `G(s,t) > δ` for some
threshold `δ > 0`. Adversarial effort efficiently reduces uncertainty.

**Algebraic connectivity:** The second-smallest eigenvalue `λ₂` of the graph Laplacian
`L(G)`. A graph-theoretic measure of network connectivity and resilience. Central to
the Dark Topology Conjecture.

**Anonymity set:** (Reiter & Rubin, 1998) The set of users who are indistinguishable
from the perspective of an adversary. Perfect anonymity corresponds to an anonymity
set equal to the entire user population.

**Authentication-Impersonation Axis (AIA):** The second of the three ETC axes.
Measures the reliability with which identity claims are verified within a system.
Score ∈ [0,1]; score 1 = reliable verification; score 0 = no reliable verification.

---

## B

**Breach factor `f(B(c,t))`:** Component of the Trust Decay Function capturing
discontinuous trust reductions caused by security breach events. `f = 1` in the
absence of known breaches; `f < 1` following breach events affecting credential `c`.

**Byzantine Generals Problem:** (Lamport, Shostak & Pease, 1982) The problem of
achieving reliable agreement in a distributed system with potentially traitorous
participants. Establishes that `3f+1` participants are required to tolerate `f` traitors.
Foundational to the Minimal Trust Principle.

---

## C

**Carrier Principle:** (Plesca, 2024) Any medium that can carry observable variation
can, in principle, carry covert information. Foundational to steganographic theory and
covert channel analysis.

**CEA:** See *Confidentiality-Exposure Axis*.

**Computational security:** Security that holds against adversaries limited to
polynomial-time computation (as opposed to information-theoretic security, which
holds against computationally unbounded adversaries).

**Confidentiality-Exposure Axis (CEA):** The first of the three ETC axes. Measures
the degree to which information that should be secret is protected from unauthorized
disclosure. Score ∈ [0,1].

**Contextual Exposure Principle (CEP):** (Plesca, 2024) The security value of a piece
of information is not an intrinsic property but a function of the informational context
in which it is embedded and the capabilities of potential adversaries. Formally:
`V(I, C, A) ≥ s(I)` with equality only when `I` is informationally independent of all
context items.

**Coupling function `F`:** Component of the ETC Security Functional capturing
security-degrading interactions between axis failures. Ranges from weak coupling
(strongly segmented systems) to strong coupling (tightly integrated systems).

---

## D

**Dark Topology Conjecture (DTC):** (Plesca, 2024) The conjecture that the minimum
achievable anonymity set size in an anonymous overlay network `G` is bounded below
by a function of `G`'s algebraic connectivity `λ₂(G)`. Status: unproved; simulation
evidence supports the conjecture (see Chapter 22 and Appendix B).

**Dark Web:** Content accessible only through overlay networks designed to provide
user anonymity, particularly Tor onion services. Distinct from (and largely
independent of) the "deep web."

**Deep web:** Web content not indexed by standard search engines. A much larger
category than the Dark Web; most deep web content is legitimate (databases, academic
journals, intranets).

**Defense in depth:** The principle that security should be implemented as a series of
independent layers, so that failure of any single layer does not result in total
compromise. Formally justified by the multiplicative structure of the AEG.

**Diffusion:** (Shannon, 1949) A cipher design principle: spreading the influence of
individual plaintext bits throughout the ciphertext.

---

## E

**Effort function `E: A → ℝ⁺`:** Component of the ETC five-tuple. Maps each
adversarial action to the computational, temporal, financial, or operational effort
required to execute it.

**ETC:** See *Entropic Threat Continuum*.

**Entropic Threat Continuum (ETC):** (Plesca, 2024) The unified theoretical framework
for information security proposed in this dissertation. Formally: a five-tuple
`(S, A, T, D, E)` governing a security state space over three invariant axes (CEA, AIA,
ICA).

**ETC Security Functional `𝒮(s)`:** The overall security posture of a system:
`𝒮(s) = min(CEA, AIA, ICA) · F(CEA, AIA, ICA)`. Not an average; failure on any
axis can produce catastrophic overall failure.

---

## F–H

**Frequency analysis:** (al-Kindi, ca. 850 CE) The use of statistical properties of
natural language (letter frequency distributions) to attack substitution ciphers without
knowledge of the key. The first documented systematic cryptanalytic method.

**Going dark:** Policy debate term for the claimed reduction in law enforcement
investigative capability caused by widespread strong encryption.

**Graph Laplacian `L(G)`:** For graph `G = (V, E)`, the matrix `L = D − A` where
`D` is the degree matrix and `A` is the adjacency matrix. Its eigenvalues characterize
connectivity properties central to the DTC.

---

## I–K

**ICA:** See *Integrity-Corruption Axis*.

**Index of coincidence:** (Friedman, 1922) A statistical measure of the probability
that two randomly selected letters from a ciphertext are identical. Provides a
quantitative tool for characterizing ciphertext without knowledge of plaintext or key.

**Information (security context):** (Plesca, 2024) Any pattern that, when received by
an agent, alters that agent's capacity for action. Encompasses (1) semantic information,
(2) structural/metadata information, and (3) inferential information.

**Integrity-Corruption Axis (ICA):** The third of the three ETC axes. Measures the
degree to which information is protected from unauthorized modification.

**Intentionality Principle of Secrecy (IPS):** (Plesca, 2024) A secret is constituted
not merely by an excluded party's non-possession of information, but by the intentional
acts of an including party directed at preventing the excluded party from obtaining it.
Security is always an active process, never a passive state.

**k-anonymity `k-anon(G, α)`:** The minimum anonymity set size achievable in network
`G` for a target user, where `α` is the fraction of relays under adversary observation.

**Kasiski test:** (Kasiski, 1863; independently Babbage, ca. 1854) A method for
determining the keyword length of a Vigenère cipher by analyzing the distances between
repeated trigrams in the ciphertext.

**Kerckhoffs's principle:** A secure system should remain secure even if everything
about the system, except the key, is public knowledge.

---

## L–O

**LAS:** See *Layered Anonymity Stack*.

**Layered Anonymity Stack (LAS):** (Plesca, 2024) A formal six-layer protocol stack
for anonymous overlay networks: (6) Identity Management, (5) Application,
(4) Routing, (3) Circuit Construction, (2) Link Encryption, (1) Physical Connectivity.

**Minimal Trust Principle (MTP):** (Plesca, 2024) The security of a system is
maximized by reducing the scope and duration of trust relationships to the minimum
necessary for system function. Operationalized in zero trust architecture.

**Mix network:** (Chaum, 1981) A network of servers that collect batches of encrypted
messages, rearrange them, and forward them to the next server, destroying the
correspondence between incoming and outgoing messages.

**Onion routing:** A technique for anonymous communication in which messages are
encrypted in layers (one per routing hop), with each node decrypting one layer to
reveal the next destination. Conceptually descended from Chaum (1981); developed at
the Naval Research Laboratory (Goldschlag, Reed & Syverson, 1999).

**Opacity Migration Theorem (OMT):** (Plesca, 2024) When opacity is removed from
one component of a system, the security properties that depended on that opacity
migrate to other components — typically those with less formal specification and less
rigorous security analysis.

---

## P–S

**Paradox of Transparent Opacity:** (Plesca, 2024) In systems with maximum
algorithmic transparency (per Kerckhoffs), security properties are not eliminated
but redistributed to layers (implementation, key management, operational security)
that are far less amenable to formal analysis.

**Perfect secrecy:** (Shannon, 1949) A cryptographic system provides perfect secrecy
iff the ciphertext provides absolutely no information about the plaintext, regardless
of adversary computational resources. Achieved only by the one-time pad (under its
conditions of use).

**Plesca Taxonomy:** (Plesca, 2024) An attack classification system organized by ETC
axis (CEA, AIA, ICA) and systemic level (physical, logical, social, combinatorial),
comprising 847 discrete attack primitive types.

**Post-quantum cryptography:** Cryptographic algorithms believed to be resistant to
attacks by both classical and quantum computers. NIST standardization selections
(2022) include CRYSTALS-Kyber (key encapsulation), CRYSTALS-Dilithium and
FALCON (digital signatures), and SPHINCS+ (hash-based signatures).

**Security measurement function `D: S → [0,1]³`:** Component of the ETC five-tuple.
Maps each security state to its three-dimensional coordinate on the ETC axes.

**Security state space (S):** The set of all possible configurations of an information
system with respect to its three security axes. Component of the ETC five-tuple.

---

## T–Z

**TDF:** See *Trust Decay Function*.

**Threat transition function `T: S × A → S`:** Component of the ETC five-tuple.
Maps each (state, adversarial action) pair to the resulting security state.

**Three-tier stratification:** (Plesca, 2024) The original functional analysis of Dark
Web infrastructure: Tier 1 (Infrastructure Services: relay network, directory
authorities, pluggable transports), Tier 2 (Platform Services: hosting environments,
messaging infrastructure), Tier 3 (Application Services: specific services accessible
through the dark web).

**Threat Surface Integral (TSI):** (Plesca, 2024) A unified metric for organizational
security exposure: `TSI = ∫_A V(a) · P(a) · I(a) da`, integrating adversarial value,
success probability, and independence weighting across all attack vectors.

**Traffic analysis:** The extraction of information from observable communication
properties (timing, volume, direction, frequency) without decrypting content.
The primary technical threat to onion routing systems.

**Trust Decay Function (TDF):** (Plesca, 2024) A model of authentication credential
reliability degradation: `T(c,t) = T(c,0) · exp(−λ(c)·t) · f(B(c,t))`.

**Unicity distance:** (Shannon, 1949) The minimum ciphertext length required for a
cipher to have a unique decryption. For key entropy `K` bits and plaintext entropy
rate `H` bits per character: unicity distance ≈ `K/H`.

**Zero trust architecture:** A network security model (Kindervag, 2010) based on the
principle "never trust, always verify." Operationalizes the Minimal Trust Principle
(MTP) through continuous authentication, least-privilege access, micro-segmentation,
and comprehensive logging.

---

*© 2024 Ciprian Stefan Plesca. All Rights Reserved.*
