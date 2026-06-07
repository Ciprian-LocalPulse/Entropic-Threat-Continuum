# Simulation Code — DTC Empirical Studies

> **From:** *From Cipher to Shadow*, Chapter 22 & Appendix B (Plesca, 2024)  
> © 2024 Ciprian Stefan Plesca. All Rights Reserved.

This directory contains the Python simulation used to provide empirical support
for the **Dark Topology Conjecture (DTC)** as described in Chapter 22 and Appendix B
of the dissertation.

---

## What This Simulation Does

The simulation tests the central claim of the DTC: that the minimum achievable
anonymity set size in an anonymous overlay network is positively correlated with
the network's **algebraic connectivity** (λ₂ — the second-smallest eigenvalue of
the graph Laplacian).

For each network configuration:
1. A relay network graph is generated with the specified topology model
2. An adversary selects the set of `α·n` relay nodes to monitor (greedy by degree)
3. Traffic is simulated using Zipf-distributed destination selection
4. Anonymity set size is measured as the number of source nodes the adversary
   cannot uniquely identify after n observations
5. Results are aggregated and Pearson correlation between λ₂ and anonymity set
   size is computed

---

## Setup

```bash
pip install -r requirements.txt
```

Requires Python 3.10+.

---

## Usage

```bash
# Quick test (small parameters)
python dtc_simulation.py --n 100 --runs 50 --configs 30 --alpha 0.20

# Replicate dissertation study (resource-intensive)
python dtc_simulation.py --n 500 --runs 1000 --configs 1000 --alpha 0.20

# Nation-state adversary scenario
python dtc_simulation.py --n 500 --runs 1000 --configs 1000 --alpha 0.50

# Scale-free (Barabási–Albert) topology comparison
python dtc_simulation.py --n 200 --runs 200 --configs 100 --model barabasi_albert

# Fixed seed for reproducibility
python dtc_simulation.py --n 100 --runs 100 --configs 50 --seed 42
```

### Arguments

| Argument | Default | Description |
|----------|---------|-------------|
| `--n` | 100 | Number of relay nodes per configuration |
| `--runs` | 100 | Simulation runs per network configuration |
| `--configs` | 50 | Number of distinct network configurations |
| `--alpha` | 0.20 | Adversary observation fraction (0 < α ≤ 1) |
| `--model` | `erdos_renyi` | Graph model: `erdos_renyi`, `barabasi_albert`, `constrained` |
| `--seed` | 42 | Random seed for reproducibility |

---

## Dissertation Results (Reference)

From the study reported in Chapter 22 (n=500 nodes, 1,000 configurations):

| α (adversary fraction) | Pearson r | p-value | Mean k-anon |
|------------------------|-----------|---------|-------------|
| 0.20 | 0.73 | < 0.001 | — |
| 0.50 | 0.61 | < 0.001 | 8.3 (top quartile networks) |

A positive, statistically significant correlation was found in all tested conditions,
consistent with the Dark Topology Conjecture.

---

## Limitations

This simulation is a **simplified model** of Tor-like anonymous network behavior:

- Routing uses shortest-path rather than Tor's actual circuit selection algorithm
- Adversary selection is greedy by degree rather than optimally computed
- Traffic patterns are Zipf-distributed (consistent with empirical web traffic) but
  do not capture full behavioral variation
- The simulation does not model guard selection, bandwidth weighting, or Tor's
  actual consensus mechanism

Results are suitable for exploring the structural relationship between algebraic
connectivity and anonymity set size as a property of network topology. They are
not predictions of real-world Tor anonymity against specific adversaries.

---

## Citation

If you use or extend this simulation, please cite:

```bibtex
@phdthesis{plesca2024ciphershadow,
  author = {Plesca, Ciprian Stefan},
  title  = {From Cipher to Shadow: A Unified Theoretical Framework for
             Information Security from Its Epistemic Origins to the
             Architecture of the Dark Web},
  school = {Department of Electrical Engineering and Computer Science},
  year   = {2024},
  type   = {Doctoral Dissertation},
}
```

---

*© 2024 Ciprian Stefan Plesca. All Rights Reserved.*
