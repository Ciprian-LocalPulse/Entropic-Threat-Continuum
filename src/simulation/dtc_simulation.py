"""Dark Topology Conjecture (DTC) simulation.

From: "From Cipher to Shadow" (Plesca, 2024), Chapter 22 and Appendix B.
Repository license: MIT.

The DTC conjectures that the minimum achievable anonymity set size in an
anonymous overlay network G is bounded below by a function of G's algebraic
connectivity, the second-smallest eigenvalue lambda_2 of the graph Laplacian.
"""

from __future__ import annotations

import argparse
import logging
import random
from dataclasses import dataclass, field
from typing import Optional

import networkx as nx
import numpy as np
from scipy import stats

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

COPYRIGHT = (
    "\nFrom Cipher to Shadow - DTC Simulation\n"
    "Copyright (c) 2024 Ciprian Stefan Plesca. Released under the MIT License.\n"
    "Citation: Plesca, C. S. (2024). From cipher to shadow [Doctoral dissertation].\n"
)


@dataclass
class SimulationConfig:
    """Configuration for a DTC simulation batch."""

    n_nodes: int = 500
    n_runs: int = 1000
    alpha: float = 0.20
    n_configs: int = 100
    seed: Optional[int] = 42
    model: str = "erdos_renyi"
    zipf_exponent: float = 1.1
    n_observations: int = 50


@dataclass
class SimulationResult:
    """Results from one network configuration."""

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
    """Aggregate results across all valid configurations."""

    n_configs: int
    alpha: float
    pearson_r: float
    p_value: float
    mean_k_anon: float
    std_k_anon: float
    results: list[SimulationResult] = field(default_factory=list)


def generate_erdos_renyi(n: int, p: float, seed: int) -> nx.DiGraph:
    """Generate an Erdos-Renyi random graph."""

    return nx.DiGraph(nx.erdos_renyi_graph(n, p, seed=seed, directed=False))


def generate_barabasi_albert(n: int, m: int, seed: int) -> nx.DiGraph:
    """Generate a Barabasi-Albert scale-free graph."""

    return nx.DiGraph(nx.barabasi_albert_graph(n, m, seed=seed))


def generate_constrained(n: int, target_lambda2: float, seed: int) -> nx.DiGraph:
    """Generate a graph with approximately the target algebraic connectivity."""

    rng = np.random.default_rng(seed)
    graph = nx.DiGraph(nx.path_graph(n))
    max_edges = min(n * (n - 1) // 2, n * 5)
    current_lambda2 = _algebraic_connectivity(graph)
    iterations = 0

    while current_lambda2 < target_lambda2 and graph.number_of_edges() < max_edges:
        u = int(rng.integers(0, n))
        v = int(rng.integers(0, n))
        if u != v and not graph.has_edge(u, v):
            graph.add_edge(u, v)
            graph.add_edge(v, u)
            current_lambda2 = _algebraic_connectivity(graph)
        iterations += 1
        if iterations > 10 * max_edges:
            break

    return graph


def _algebraic_connectivity(graph: nx.DiGraph) -> float:
    """Compute lambda_2 of the undirected graph Laplacian."""

    undirected = graph.to_undirected()
    if undirected.number_of_nodes() < 2 or not nx.is_connected(undirected):
        return 0.0
    laplacian = nx.laplacian_matrix(undirected).toarray()
    eigenvalues = np.linalg.eigvalsh(laplacian)
    return float(np.sort(eigenvalues)[1])


def select_adversary_nodes(graph: nx.DiGraph, alpha: float, rng: np.random.Generator) -> set[int]:
    """Select monitored relay nodes using a high-degree greedy strategy."""

    del rng
    n_monitor = max(1, int(alpha * graph.number_of_nodes()))
    degrees = dict(graph.degree())
    return set(sorted(degrees, key=degrees.get, reverse=True)[:n_monitor])


def zipf_destination(n_nodes: int, exponent: float, rng: np.random.Generator) -> int:
    """Sample a destination node using a Zipf-like popularity distribution."""

    weights = np.array([1.0 / (i**exponent) for i in range(1, n_nodes + 1)])
    weights /= weights.sum()
    return int(rng.choice(n_nodes, p=weights))


def simulate_anonymity_set(
    graph: nx.DiGraph,
    adversary_nodes: set[int],
    n_sources: int,
    n_observations: int,
    rng: np.random.Generator,
    zipf_exponent: float = 1.1,
) -> float:
    """Simulate one anonymity-set observation batch."""

    del n_sources
    n_nodes = graph.number_of_nodes()
    paths = dict(nx.all_pairs_shortest_path(graph, cutoff=5))
    observable_traffic: dict[tuple[int, int], int] = {}

    for _ in range(n_observations):
        source = int(rng.choice(n_nodes))
        dest = zipf_destination(n_nodes, zipf_exponent, rng)
        if source == dest or source not in paths or dest not in paths.get(source, {}):
            continue

        path = paths[source][dest]
        observed_entry = path[0] in adversary_nodes or (len(path) > 1 and path[1] in adversary_nodes)
        observed_exit = path[-1] in adversary_nodes or (len(path) > 1 and path[-2] in adversary_nodes)

        if observed_entry and observed_exit:
            observable_traffic[(source, dest)] = observable_traffic.get((source, dest), 0) + 1

    identified_sources = {source for source, _ in observable_traffic}
    return float(max(1, n_nodes - len(identified_sources)))


def run_simulation(config: SimulationConfig) -> AggregateResult:
    """Run the DTC simulation across multiple network configurations."""

    if config.seed is not None:
        np.random.seed(config.seed)
        random.seed(config.seed)

    rng = np.random.default_rng(config.seed)
    results: list[SimulationResult] = []
    logger.info(
        "Starting DTC simulation: n=%s, alpha=%.2f, runs=%s, configs=%s",
        config.n_nodes,
        config.alpha,
        config.n_runs,
        config.n_configs,
    )

    for config_id in range(config.n_configs):
        seed_i = (config.seed or 0) + config_id * 37
        if config.model == "erdos_renyi":
            graph = generate_erdos_renyi(config.n_nodes, p=float(rng.uniform(0.02, 0.15)), seed=seed_i)
        elif config.model == "barabasi_albert":
            graph = generate_barabasi_albert(config.n_nodes, m=int(rng.integers(2, 8)), seed=seed_i)
        elif config.model == "constrained":
            graph = generate_constrained(
                config.n_nodes,
                target_lambda2=float(rng.uniform(0.01, 2.0)),
                seed=seed_i,
            )
        else:
            raise ValueError(f"Unknown graph model: {config.model}")

        undirected = graph.to_undirected()
        if not nx.is_connected(undirected):
            largest_cc = max(nx.connected_components(undirected), key=len)
            graph = graph.subgraph(largest_cc).copy()
            if graph.number_of_nodes() < 10:
                continue

        lambda2 = _algebraic_connectivity(graph)
        adversary_nodes = select_adversary_nodes(graph, config.alpha, rng)
        anonymity_set_sizes = [
            simulate_anonymity_set(
                graph=graph,
                adversary_nodes=adversary_nodes,
                n_sources=graph.number_of_nodes(),
                n_observations=config.n_observations,
                rng=rng,
                zipf_exponent=config.zipf_exponent,
            )
            for _ in range(config.n_runs)
        ]

        results.append(
            SimulationResult(
                config_id=config_id,
                model=config.model,
                n_nodes=graph.number_of_nodes(),
                algebraic_connectivity=lambda2,
                mean_anonymity_set_size=float(np.mean(anonymity_set_sizes)),
                std_anonymity_set_size=float(np.std(anonymity_set_sizes)),
                alpha=config.alpha,
                n_runs=config.n_runs,
            )
        )

    lambda2_values = [result.algebraic_connectivity for result in results]
    k_anon_values = [result.mean_anonymity_set_size for result in results]
    if len(results) < 3 or len(set(lambda2_values)) < 2 or len(set(k_anon_values)) < 2:
        pearson_r, p_value = float("nan"), float("nan")
    else:
        pearson_r, p_value = stats.pearsonr(lambda2_values, k_anon_values)

    return AggregateResult(
        n_configs=len(results),
        alpha=config.alpha,
        pearson_r=float(pearson_r),
        p_value=float(p_value),
        mean_k_anon=float(np.mean(k_anon_values)) if k_anon_values else float("nan"),
        std_k_anon=float(np.std(k_anon_values)) if k_anon_values else float("nan"),
        results=results,
    )


def print_results(aggregate: AggregateResult) -> None:
    """Print simulation results."""

    print("\n" + "=" * 60)
    print("DTC SIMULATION RESULTS")
    print("=" * 60)
    print(f"  Valid configurations analyzed : {aggregate.n_configs}")
    print(f"  Adversary observation fraction: alpha = {aggregate.alpha:.2f}")
    print(f"  Pearson r (lambda_2 vs k-anon): {aggregate.pearson_r:.4f}")
    print(f"  p-value                       : {aggregate.p_value:.4e}")
    print(f"  Mean anonymity set size       : {aggregate.mean_k_anon:.2f} +/- {aggregate.std_k_anon:.2f}")
    print("=" * 60)


def main() -> None:
    print(COPYRIGHT)
    parser = argparse.ArgumentParser(description="DTC Simulation - From Cipher to Shadow (Plesca, 2024)")
    parser.add_argument("--n", type=int, default=100, help="Number of relay nodes per configuration")
    parser.add_argument("--runs", type=int, default=100, help="Simulation runs per configuration")
    parser.add_argument("--configs", type=int, default=50, help="Number of network configurations")
    parser.add_argument("--alpha", type=float, default=0.20, help="Adversary observation fraction")
    parser.add_argument(
        "--model",
        type=str,
        default="erdos_renyi",
        choices=["erdos_renyi", "barabasi_albert", "constrained"],
        help="Graph generation model",
    )
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    args = parser.parse_args()
    aggregate = run_simulation(
        SimulationConfig(
            n_nodes=args.n,
            n_runs=args.runs,
            n_configs=args.configs,
            alpha=args.alpha,
            model=args.model,
            seed=args.seed,
        )
    )
    print_results(aggregate)


if __name__ == "__main__":
    main()
