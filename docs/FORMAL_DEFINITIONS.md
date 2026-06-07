# Formal Definitions — ETC Framework Mathematical Reference

> **From:** *From Cipher to Shadow* (Plesca, 2024)  
> Copyright (c) 2024 Ciprian Stefan Plesca. Released under the MIT License.

This document provides precise mathematical definitions of all original
theoretical constructs introduced in the dissertation. Proofs of selected
results are given in full; others are referenced to Appendix A of the
dissertation.

---

## Notation

| Symbol | Meaning |
|--------|---------|
| `H(X)` | Shannon entropy of random variable X: `−Σ p(x) log₂ p(x)` |
| `H(X|Y)` | Conditional entropy of X given Y |
| `G = (V, E)` | Directed graph with vertex set V and edge set E |
| `L(G)` | Graph Laplacian matrix of G |
| `λ₂(G)` | Second-smallest eigenvalue of L(G) (algebraic connectivity) |
| `[0,1]` | The closed unit interval |
| `ℝ⁺` | The positive real numbers |

---

## Definition 1: The ETC Five-Tuple

The **Entropic Threat Continuum** is the five-tuple `(S, A, T, D, E)` where:

- `S` is the **security state space**: the set of all possible configurations of an
  information system with respect to its three security axes
- `A` is the **adversarial capability set**: the complete set of operations available
  to potential attackers
- `T: S × A → S` is the **threat transition function**: for each pair `(s, a) ∈ S × A`,
  `T(s, a)` gives the security state resulting from adversary executing action `a`
  when the system is in state `s`
- `D: S → [0,1]³` is the **security measurement function**: `D(s) = (CEA(s), AIA(s), ICA(s))`
  maps each state to its coordinates on the three ETC axes
- `E: A → ℝ⁺` is the **effort function**: `E(a)` is the computational, temporal, financial,
  or operational effort required to execute action `a`

---

## Definition 2: The Three ETC Axes

For any state `s ∈ S`, the security measurement `D(s) = (CEA(s), AIA(s), ICA(s)) ∈ [0,1]³` where:

- **CEA(s) ∈ [0,1]**: Confidentiality-Exposure Axis score. Value 1 indicates perfect protection
  of all information that should be secret; value 0 indicates complete exposure.
- **AIA(s) ∈ [0,1]**: Authentication-Impersonation Axis score. Value 1 indicates all identity
  claims are reliably verified; value 0 indicates no reliable verification.
- **ICA(s) ∈ [0,1]**: Integrity-Corruption Axis score. Value 1 indicates all information is
  tamper-evident and tamper-resistant; value 0 indicates information is freely modifiable.

---

## Definition 3: The ETC Security Functional

The **overall security posture** of a system in state `s` is:

```
𝒮(s) = min(CEA(s), AIA(s), ICA(s)) · F(CEA(s), AIA(s), ICA(s))
```

Where `F: [0,1]³ → [0,1]` is the **coupling function** satisfying:
1. `F(1,1,1) = 1` (perfect security on all axes → no degradation)
2. `F` is monotone non-increasing in each argument deviation from 1
3. `F` → 0 as any argument → 0 (total failure on any axis catastrophically degrades the functional)

The specific form of `F` is system-dependent and reflects the degree of interdependence
between security axes in the architectural design.

---

## Definition 4: Adversarial Entropy Gradient (AEG)

Let `O_t` denote the adversary's observations through time `t`, and let `E_t` denote cumulative
effort through time `t`.

The **Adversarial Entropy Gradient** at time `t` is:

```
G(s, t) = −dH(s | O_t) / dE_t
```

(The negative sign ensures G ≥ 0: reducing uncertainty corresponds to positive gradient.)

**Interpretation:**
- `G(s,t) < ε` for small `ε > 0`: system is **AEG-secure** at time `t`
  (additional effort yields negligible information about security state)
- `G(s,t) > δ` for threshold `δ > 0`: system is **AEG-insecure** at time `t`
  (adversarial effort efficiently reduces uncertainty)

**Note:** The AEG is a theoretical model. Adversarial knowledge states are not directly
observable; the AEG provides conceptual structure rather than a computable formula.

---

## Definition 5: Trust Decay Function (TDF)

The **trust value** of credential `c` at time `t` is:

```
T(c, t) = T(c, 0) · exp(−λ(c) · t) · f(B(c, t))
```

Where:
- `T(c, 0) ∈ [0,1]`: initial trust value at credential creation
- `λ(c) > 0`: credential-specific decay constant (determined by credential type, threat environment)
- `t ≥ 0`: time elapsed since credential creation (in appropriate units)
- `B(c, t)`: the breach history of credential `c` through time `t`
- `f: [0,1] → [0,1]`: breach factor function, satisfying `f(∅) = 1` (no breaches → no additional decay)
  and `f(B) < 1` when B contains breach events (breaches cause discontinuous trust reduction)

**Rotation criterion:** A credential `c` should be rotated when `T(c, t) < τ` for some
acceptable trust threshold `τ` established by organizational security policy.

---

## Definition 6: Threat Surface Integral (TSI)

The **threat surface** of an organization is:

```
TSI = ∫_A  V(a) · P(a) · I(a)  da
```

Where `A` is the space of all attack vectors and:
- `V(a) ∈ ℝ⁺`: adversarial value (expected harm) of successfully executing attack `a`
- `P(a) ∈ [0,1]`: probability that attack `a` succeeds given current defenses
- `I(a) ∈ [0,1]`: independence factor for attack `a` (correlated attacks receive `I(a) < 1`
  to prevent double-counting)

For finite attack taxonomies (e.g., the Plesca Taxonomy), the integral reduces to a sum:

```
TSI = Σₐ  V(a) · P(a) · I(a)
```

**Usage:** TSI decomposition by attack vector identifies highest-exposure components,
enabling risk-proportional security investment allocation.

---

## Definition 7: The Layered Anonymity Stack (LAS)

The LAS defines six functional layers for anonymous overlay networks:

```
Layer 6 — Identity Management Layer
Layer 5 — Application Layer
Layer 4 — Routing Layer
Layer 3 — Circuit Construction Layer
Layer 2 — Link Encryption Layer
Layer 1 — Physical Connectivity Layer
```

A system `Σ` is **LAS-secure at layer k** if an adversary with complete knowledge of
layers `{1, ..., k−1}` cannot violate the anonymity properties guaranteed by layer `k`.

**Layer independence theorem (informal):** Security failures at layer `k` propagate to
higher layers; security at layer `k` does not compensate for failures at layer `k−1`.
This mirrors the OSI model's analogous property for standard network security.

---

## Conjecture 1: Dark Topology Conjecture (DTC)

Let `G = (V, E)` be a directed graph representing an anonymous overlay network.
Let `k-anon(G, α)` denote the minimum anonymity set size achievable for a target user,
where `α ∈ [0,1]` is the fraction of relays under adversary observation.

**DTC:** There exists a monotone function `φ: ℝ⁺ → ℕ` such that for all `G`:

```
k-anon(G, α) ≥ φ(λ₂(G), α, n)
```

Where `λ₂(G)` is the algebraic connectivity of `G` and `n = |V|`, and this bound is tight:
there exist adversary strategies achieving the bound for graphs with minimum `λ₂`.

**Status:** Unproved for general graph families. Simulation evidence (n = 1,000 configurations,
r = 0.73 at α = 0.20, p < 0.001) supports the conjecture. Formal proof is an open problem.

**Corollary (practical):** Anonymous overlay networks should be designed to maximize `λ₂(G)`.
This favors uniform degree distribution over power-law (hub-and-spoke) topologies.

---

## Theorem 1: Contextual Exposure Principle (CEP) — Formal Statement and Proof

**Statement:** For any information item `I`, adversary `A`, and context set `C = {c₁, ..., cₙ}`:

```
V(I, C, A) = s(I) + Σⱼ δ(I, cⱼ, A)  ≥  s(I)
```

Where `s(I)` is the intrinsic sensitivity of `I` assessed in isolation and `δ(I, cⱼ, A) ≥ 0`
is the inference capacity increment from combining `I` with context item `cⱼ`.

**Proof:** By definition of adversarial inference capacity, adding information to an
adversary's information set cannot decrease their inference capacity in a well-defined
inference setting (information is monotone with respect to adversarial capability under
standard assumptions of rational adversarial behavior). Therefore `δ(I, cⱼ, A) ≥ 0` for all `j`.

It follows immediately that `V(I, C, A) = s(I) + Σⱼ δ(I, cⱼ, A) ≥ s(I)`.

Equality holds iff `δ(I, cⱼ, A) = 0` for all `j` — that is, iff `I` provides no
inference advantage in combination with any element of `C` under adversary `A`. ∎

---

## Theorem 2: Opacity Migration Theorem (OMT) — Informal Statement

**Statement:** For system `S = {C₁, ..., Cₙ}` with interfaces `{I₁₂, I₂₃, ..., I(n−1)n}`:
if opacity is reduced in component `Cᵢ` (i.e., more of `Cᵢ`'s behavior is formally specified
and publicly known), then the security properties that depended on `Cᵢ`'s opacity are not
eliminated. They migrate to other components — specifically, to those with the least formal
specification and least rigorous security analysis.

**Formal treatment:** See Dissertation Appendix A.

---

*Copyright (c) 2024 Ciprian Stefan Plesca. Released under the MIT License.*  
*Citation: Plesca, C. S. (2024). From cipher to shadow [Doctoral dissertation].*
