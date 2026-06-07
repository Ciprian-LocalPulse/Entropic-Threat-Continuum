"""Run compact reproducibility simulations for the ETC repository."""

from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from simulation.dtc_simulation import SimulationConfig, run_simulation


def main() -> int:
    output = ROOT / "assets" / "data" / "generated_dtc_summary.csv"
    output.parent.mkdir(parents=True, exist_ok=True)
    aggregate = run_simulation(SimulationConfig(n_nodes=60, n_runs=5, n_configs=8, seed=42))
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "config_id",
                "model",
                "n_nodes",
                "algebraic_connectivity",
                "mean_anonymity_set_size",
                "std_anonymity_set_size",
                "alpha",
                "n_runs",
            ],
        )
        writer.writeheader()
        for result in aggregate.results:
            writer.writerow(result.__dict__)
    print(f"Wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
