"""Shared utilities for ETC simulations."""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Iterable, Mapping

import networkx as nx
import numpy as np


def load_json(path: str | Path) -> dict:
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_csv(path: str | Path, rows: Iterable[Mapping[str, object]]) -> None:
    rows = list(rows)
    if not rows:
        raise ValueError("cannot write an empty CSV without field names")
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def graph_summary(graph: nx.Graph) -> dict[str, float]:
    undirected = graph.to_undirected()
    connected = nx.is_connected(undirected) if undirected.number_of_nodes() else False
    density = nx.density(undirected)
    avg_degree = float(np.mean([degree for _, degree in undirected.degree()])) if undirected.number_of_nodes() else 0.0
    return {
        "nodes": float(undirected.number_of_nodes()),
        "edges": float(undirected.number_of_edges()),
        "density": float(density),
        "average_degree": avg_degree,
        "connected": float(connected),
    }


def min_max_normalize(values: Iterable[float]) -> list[float]:
    array = np.array(list(values), dtype=float)
    if array.size == 0:
        return []
    lower = float(np.min(array))
    upper = float(np.max(array))
    if upper == lower:
        return [0.0 for _ in array]
    return [float((value - lower) / (upper - lower)) for value in array]
