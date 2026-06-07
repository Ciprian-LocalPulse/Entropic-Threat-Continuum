# API Reference

This reference summarizes the public Python modules under `src/simulation` and `src/taxonomy`.

## `simulation.etc_framework`

- `SecurityState(cea, aia, ica, metadata=None)`: immutable ETC axis vector with validation.
- `ThreatAction(name, axis_weights, effort, impact, probability=1.0)`: adversarial action model.
- `ETCFramework`: transition engine for applying threat actions to security states.
- `etc_security_functional(state, coupling=1.0)`: multiplicative ETC posture score.
- `contextual_exposure(base_value, audience_size, sensitivity, aggregation_factor=1.0)`: Contextual Exposure Principle helper.
- `opacity_migration(before, removed_opacity)`: Opacity Migration Theorem helper.

## `simulation.aeg_model`

- `EntropyObservation(effort, entropy)`: effort/uncertainty point.
- `AdversarialEntropyGradient`: estimates entropy gradients, marginal efficiency, and fitted decay curves.

## `simulation.tdf_model`

- `BreachEvent(time, severity, label="")`: discrete trust shock.
- `CredentialTrust`: exponential trust-decay model with multiplicative breach penalties.

## `simulation.tsi_calculator`

- `AttackVector`: normalized exposure vector.
- `ThreatSurfaceIntegral`: weighted integration, axis aggregation, ranking, and reporting.

## `simulation.las_analyzer`

- `LASLayer`: six-layer anonymity stack component.
- `LayeredAnonymityStack`: stack scoring, weakest-layer detection, and compromise-path analysis.

## `simulation.dtc_simulation`

- `SimulationConfig`: DTC run configuration.
- `run_simulation(config)`: returns aggregate correlation statistics.
- `generate_erdos_renyi`, `generate_barabasi_albert`, `generate_constrained`: graph generators.

## `taxonomy.taxonomy_validator`

- `validate_taxonomy(data)`: validates axes, levels, primitive fields, code formats, and metadata.
- `load_taxonomy(path)`: loads taxonomy JSON.
- CLI: `python -m taxonomy.taxonomy_validator src/taxonomy/plesca_taxonomy.json`
