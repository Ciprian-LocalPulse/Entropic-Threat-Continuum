"""
Dark Topology Conjecture (DTC) Simulation
==========================================
From: "From Cipher to Shadow" (Plesca, 2024), Chapter 22 and Appendix B

© 2024 Ciprian Stefan Plesca. All Rights Reserved.
See LICENSE in repository root for full copyright notice.

This module implements the discrete-event simulation described in Chapter 22
and Appendix B of the dissertation to provide empirical support for the
Dark Topology Conjecture.

The DTC conjectures that the minimum achievable anonymity set size in an
anonymous overlay network G is bounded below by a function of G's algebraic
connectivity (the second-smallest eigenvalue λ₂ of the graph Laplacian L(G)).

Usage:
    python dtc_simulation.py --n 500 --runs 1000 --alpha 0.20

Requirements: See requirements.txt
"""

import argparse
import logging
import random
from dataclasses import dataclass, field
from typing import Optional

import numpy as np
import networkx as nx
from scipy import stats

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

# Copyright notice (printed at runtime)
COPYRIGHT = (
    "\nFrom Cipher to Shadow — DTC Simulation\n"
    "© 2024 Ciprian Stefan Plesca. All Rights Reserved.\n"
    "Citation: Plesca, C. S. (2024). From cipher to shadow [Doctoral dissertation].\n"
    "See LICENSE for full copyright terms.\n"
)


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class SimulationConfig:
    """Configuration for a single simulation run."""
    n_nodes: int = 500          # Number of relay nodes
    n_runs: int = 1000          # Simulation runs per network configuration
    alpha: float = 0.20         # Fraction of relays under adversary observation
    n_configs: int = 100        # Number of network configurations to test
    seed: Optional[int] = 42    # Random seed for reproducibility
    model: str = "erdos_renyi"  # Graph generation model
    zipf_exponent: float = 1.1  # Exponent for destination selection (Zipf)


@dataclass
class SimulationResult:
    """Results from a single network configuration."""
    config_id: int
    model: str
    n_nodes: int
    algebraic_connectivity: float
    mean_anonymity_set_size: float
    std_anonymity_set_size: float
    alpha: float
    n_runs: int


@dataclass
class AggregateResult:
    """Aggregate results across all configurations."""
    n_configs: int
    alpha: float
    pearson_r: float
    p_value: float
    mean_k_anon: float
    std_k_anon: float
    results: list = field(default_factory=list)


# ---------------------------------------------------------------------------
# Graph generation
# ---------------------------------------------------------------------------

def generate_erdos_renyi(n: int, p: float, seed: int) -> nx.DiGraph:
    """Generate an Erdős–Rényi random graph."""
    G = nx.erdos_renyi_graph(n, p, seed=seed, directed=False)
    return nx.DiGraph(G)


def generate_barabasi_albert(n: int, m: int, seed: int) -> nx.DiGraph:
    """Generate a Barabási–Albert scale-free graph (for topology comparison)."""
    G = nx.barabasi_albert_graph(n, m, seed=seed)
    return nx.DiGraph(G)


def generate_constrained(n: int, target_lambda2: float, seed: int) -> nx.DiGraph:
    """
    Generate a graph with approximately the target algebraic connectivity.
    Uses iterative edge-addition to approach the target λ₂.
    """
    rng = np.random.default_rng(seed)
    # Start from a connected base graph
    G = nx.path_graph(n)
    G = nx.DiGraph(G)

    # Add edges until algebraic connectivity exceeds target or edge budget exhausted
    max_edges = min(n * (n - 1) // 2, n * 5)
    current_lambda2 = _algebraic_connectivity(G)

    iterations = 0
    while current_lambda2 < target_lambda2 and G.number_of_edges() < max_edges:
        u = int(rng.integers(0, n))
        v = int(rng.integers(0, n))
        if u != v and not G.has_edge(u, v):
            G.add_edge(u, v)
            G.add_edge(v, u)
            current_lambda2 = _algebraic_connectivity(G)
        iterations += 1
        if iterations > 10 * max_edges:
            break

    return G


def _algebraic_connectivity(G: nx.DiGraph) -> float:
    """
    Compute algebraic connectivity (λ₂ of Laplacian) for a directed graph.
    Uses the underlying undirected graph for symmetric Laplacian computation.
    """
    G_undirected = G.to_undirected()
    if not nx.is_connected(G_undirected):
        return 0.0
    L = nx.laplacian_matrix(G_undirected).toarray()
    eigenvalues = np.linalg.eigvalsh(L)
    eigenvalues_sorted = np.sort(eigenvalues)
    return float(eigenvalues_sorted[1])  # Second-smallest eigenvalue


# ---------------------------------------------------------------------------
# Adversary model
# ---------------------------------------------------------------------------

def select_adversary_nodes(G: nx.DiGraph, alpha: float, rng: np.random.Generator) -> set:
    """
    Select the set of relay nodes to monitor.
    Strategy: prioritize high-degree nodes (greedy maximization of traffic coverage).
    """
    n_monitor = max(1, int(alpha * G.number_of_nodes()))
    degrees = dict(G.degree())
    sorted_nodes = sorted(degrees, key=degrees.get, reverse=True)
    # Take top-degree nodes (greedy; optimal selection is NP-hard in general)
    return set(sorted_nodes[:n_monitor])


# ---------------------------------------------------------------------------
# Traffic simulation
# ---------------------------------------------------------------------------

def zipf_destination(n_nodes: int, exponent: float, rng: np.random.Generator) -> int:
    """Sample a destination node using Zipf distribution (mimics web traffic)."""
    # Zipf weights: rank 1 is most popular
    weights = np.array([1.0 / (i ** exponent) for i in range(1, n_nodes + 1)])
    weights /= weights.sum()
    return int(rng.choice(n_nodes, p=weights))


def simulate_anonymity_set(
    G: nx.DiGraph,
    adversary_nodes: set,
    n_sources: int,
    n_observations: int,
    rng: np.random.Generator,
    zipf_exponent: float = 1.1,
) -> float:
    """
    Simulate anonymity set size for one run.

    The adversary observes traffic at monitored relay nodes and attempts
    to link source nodes to destination nodes through timing correlation.

    Returns the mean number of source nodes indistinguishable to the adversary
    after n_observations observations.
    """
    n_nodes = G.number_of_nodes()
    nodes = list(G.nodes())

    # Compute shortest paths for routing (simplified routing model)
    # In practice, Tor uses 3-hop circuits; we use shortest paths as approximation
    paths = dict(nx.all_pairs_shortest_path(G, cutoff=5))

    observable_traffic: dict[tuple, int] = {}  # (source, dest) -> observation count

    for _ in range(n_observations):
        source = int(rng.choice(n_nodes))
        dest = zipf_destination(n_nodes, zipf_exponent, rng)
        if source == dest:
            continue

        if source not in paths or dest not in paths.get(source, {}):
            continue

        path = paths[source][dest]

        # Check if any node on the path (excluding source/dest) is monitored
        intermediate_nodes = set(path[1:-1])
        observed_entry = path[0] in adversary_nodes or (
            len(path) > 1 and path[1] in adversary_nodes
        )
        observed_exit = path[-1] in adversary_nodes or (
            len(path) > 1 and path[-2] in adversary_nodes
        )

        if observed_entry and observed_exit:
            # Both entry and exit visible: adversary can link source to dest
            observable_traffic[(source, dest)] = (
                observable_traffic.get((source, dest), 0) + 1
            )

    # Anonymity set size: number of sources the adversary cannot uniquely identify
    # (i.e., sources with no observed entry+exit correlation)
    identified_sources = set(s for (s, _) in observable_traffic.keys())
    unidentified_sources = n_nodes - len(identified_sources)
    return float(max(1, unidentified_sources))


# ---------------------------------------------------------------------------
# Main simulation
# ---------------------------------------------------------------------------

def run_simulation(config: SimulationConfig) -> AggregateResult:
    """Run the full DTC simulation across multiple network configurations."""
    if config.seed is not None:
        np.random.seed(config.seed)
        random.seed(config.seed)

    rng = np.random.default_rng(config.seed)
    results: list[SimulationResult] = []

    logger.info(
        f"Starting DTC simulation: n={config.n_nodes}, α={config.alpha}, "
        f"runs={config.n_runs}, configs={config.n_configs}"
    )

    for config_id in range(config.n_configs):
        # Generate network configuration
        seed_i = (config.seed or 0) + config_id * 37

        if config.model == "erdos_renyi":
            p = rng.uniform(0.02, 0.15)
            G = generate_erdos_renyi(config.n_nodes, p=p, seed=seed_i)
        elif config.model == "barabasi_albert":
            m = int(rng.integers(2, 8))
            G = generate_barabasi_albert(config.n_nodes, m=m, seed=seed_i)
        elif config.model == "constrained":
            target_lambda2 = rng.uniform(0.01, 2.0)
            G = generate_constrained(config.n_nodes, target_lambda2=target_lambda2, seed=seed_i)
        else:
            raise ValueError(f"Unknown graph model: {config.model}")

        # Ensure connectivity
        undirected = G.to_undirected()
        if not nx.is_connected(undirected):
            # Use largest connected component
            largest_cc = max(nx.connected_components(undirected), key=len)
            G = G.subgraph(largest_cc).copy()
            if G.number_of_nodes() < 10:
                logger.debug(f"Config {config_id}: graph too small after LCC, skipping.")
                continue

        # Compute algebraic connectivity
        lambda2 = _algebraic_connectivity(G)

        # Select adversary nodes
        adversary_nodes = select_adversary_nodes(G, config.alpha, rng)

        # Run simulation
        anonymity_set_sizes = []
        for _ in range(config.n_runs):
            k = simulate_anonymity_set(
                G=G,
                adversary_nodes=adversary_nodes,
                n_sources=G.number_of_nodes(),
                n_observations=50,
                rng=rng,
                zipf_exponent=config.zipf_exponent,
            )
            anonymity_set_sizes.append(k)

        mean_k = float(np.mean(anonymity_set_sizes))
        std_k = float(np.std(anonymity_set_sizes))

        result = SimulationResult(
            config_id=config_id,
            model=config.model,
            n_nodes=G.number_of_nodes(),
            algebraic_connectivity=lambda2,
            mean_anonymity_set_size=mean_k,
            std_anonymity_set_size=std_k,
            alpha=config.alpha,
            n_runs=config.n_runs,
        )
        results.append(result)

        if (config_id + 1) % 10 == 0:
            logger.info(f"  Completed {config_id + 1}/{config.n_configs} configurations.")

    # Compute correlation between algebraic connectivity and mean anonymity set size
    lambda2_values = [r.algebraic_connectivity for r in results]
    k_anon_values = [r.mean_anonymity_set_size for r in results]

    if len(results) < 3:
        logger.warning("Insufficient valid configurations for correlation analysis.")
        pearson_r, p_value = float("nan"), float("nan")
    else:
        pearson_r, p_value = stats.pearsonr(lambda2_values, k_anon_values)

    aggregate = AggregateResult(
        n_configs=len(results),
        alpha=config.alpha,
        pearson_r=float(pearson_r),
        p_value=float(p_value),
        mean_k_anon=float(np.mean(k_anon_values)) if k_anon_values else float("nan"),
        std_k_anon=float(np.std(k_anon_values)) if k_anon_values else float("nan"),
        results=results,
    )

    return aggregate


def print_results(aggregate: AggregateResult) -> None:
    """Print simulation results."""
    print("\n" + "=" * 60)
    print("DTC SIMULATION RESULTS")
    print("=" * 60)
    print(f"  Valid configurations analyzed : {aggregate.n_configs}")
    print(f"  Adversary observation fraction: α = {aggregate.alpha:.2f}")
    print(f"  Pearson r (λ₂ vs k-anon)     : {aggregate.pearson_r:.4f}")
    print(f"  p-value                       : {aggregate.p_value:.4e}")
    print(f"  Mean anonymity set size       : {aggregate.mean_k_anon:.2f} ± {aggregate.std_k_anon:.2f}")
    print("=" * 60)

    significance = "STATISTICALLY SIGNIFICANT" if aggregate.p_value < 0.001 else "not significant at p < 0.001"
    print(f"\nCorrelation is {significance}.")
    if aggregate.pearson_r > 0.5:
        print(
            "Positive correlation observed: networks with higher algebraic connectivity\n"
            "achieve larger anonymity sets — consistent with the Dark Topology Conjecture."
        )
    print()


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main() -> None:
    print(COPYRIGHT)

    parser = argparse.ArgumentParser(
        description="DTC Simulation — From Cipher to Shadow (Plesca, 2024)"
    )
    parser.add_argument("--n", type=int, default=100,
                        help="Number of relay nodes per configuration (default: 100)")
    parser.add_argument("--runs", type=int, default=100,
                        help="Simulation runs per configuration (default: 100)")
    parser.add_argument("--configs", type=int, default=50,
                        help="Number of network configurations to test (default: 50)")
    parser.add_argument("--alpha", type=float, default=0.20,
                        help="Adversary observation fraction (default: 0.20)")
    parser.add_argument("--model", type=str, default="erdos_renyi",
                        choices=["erdos_renyi", "barabasi_albert", "constrained"],
                        help="Graph generation model (default: erdos_renyi)")
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed for reproducibility (default: 42)")
    args = parser.parse_args()

    config = SimulationConfig(
        n_nodes=args.n,
        n_runs=args.runs,
        n_configs=args.configs,
        alpha=args.alpha,
        model=args.model,
        seed=args.seed,
    )

    aggregate = run_simulation(config)
    print_results(aggregate)


if __name__ == "__main__":
    main()
