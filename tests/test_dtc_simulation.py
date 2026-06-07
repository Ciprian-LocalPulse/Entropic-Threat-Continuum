from simulation.dtc_simulation import SimulationConfig, run_simulation


def test_dtc_small_simulation_runs():
    aggregate = run_simulation(SimulationConfig(n_nodes=20, n_runs=2, n_configs=3, seed=7))
    assert aggregate.n_configs >= 1
    assert len(aggregate.results) == aggregate.n_configs
