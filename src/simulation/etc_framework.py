"""Core Entropic Threat Continuum abstractions."""

from __future__ import annotations

from dataclasses import dataclass, field
from math import log1p
from typing import Mapping

AXES = ("CEA", "AIA", "ICA")


def _clamp(value: float, lower: float = 0.0, upper: float = 1.0) -> float:
    return max(lower, min(upper, float(value)))


@dataclass(frozen=True)
class SecurityState:
    """A point in the three-axis ETC security measurement space."""

    cea: float
    aia: float
    ica: float
    metadata: Mapping[str, object] = field(default_factory=dict)

    def __post_init__(self) -> None:
        for name, value in (("cea", self.cea), ("aia", self.aia), ("ica", self.ica)):
            if not 0.0 <= float(value) <= 1.0:
                raise ValueError(f"{name} must be in [0, 1], got {value!r}")

    def as_dict(self) -> dict[str, float]:
        return {"CEA": float(self.cea), "AIA": float(self.aia), "ICA": float(self.ica)}

    def axis_score(self, axis: str) -> float:
        normalized = axis.upper()
        if normalized not in AXES:
            raise KeyError(f"unknown ETC axis: {axis!r}")
        return self.as_dict()[normalized]

    @property
    def weakest_axis(self) -> str:
        return min(self.as_dict(), key=self.as_dict().get)


@dataclass(frozen=True)
class ThreatAction:
    """An adversarial action mapped onto ETC axes."""

    name: str
    axis_weights: Mapping[str, float]
    effort: float
    impact: float
    probability: float = 1.0

    def __post_init__(self) -> None:
        if self.effort < 0:
            raise ValueError("effort must be non-negative")
        if not 0 <= self.impact <= 1:
            raise ValueError("impact must be in [0, 1]")
        if not 0 <= self.probability <= 1:
            raise ValueError("probability must be in [0, 1]")
        unknown = set(axis.upper() for axis in self.axis_weights) - set(AXES)
        if unknown:
            raise ValueError(f"unknown ETC axes: {sorted(unknown)}")

    def normalized_weights(self) -> dict[str, float]:
        weights = {axis.upper(): max(0.0, float(value)) for axis, value in self.axis_weights.items()}
        total = sum(weights.values())
        if total == 0:
            return {axis: 0.0 for axis in AXES}
        return {axis: weights.get(axis, 0.0) / total for axis in AXES}


def etc_security_functional(state: SecurityState, coupling: float = 1.0) -> float:
    """Return the multiplicative ETC posture score.

    The weakest axis dominates, while the axis product rewards balanced systems.
    `coupling` represents architecture quality: values below 1 penalize tightly
    coupled systems where one failure propagates into other axes.
    """

    coupling = _clamp(coupling)
    values = state.as_dict().values()
    product = 1.0
    for value in values:
        product *= value
    return _clamp(min(state.as_dict().values()) * (product ** (1.0 / 3.0)) * coupling)


class ETCFramework:
    """Transition engine for applying threat actions to ETC states."""

    def __init__(self, initial_state: SecurityState):
        self.initial_state = initial_state
        self.current_state = initial_state
        self.history: list[tuple[ThreatAction, SecurityState]] = []

    def transition(self, action: ThreatAction) -> SecurityState:
        weights = action.normalized_weights()
        effort_pressure = log1p(action.effort) / (1.0 + log1p(action.effort))
        degradation = action.impact * action.probability * effort_pressure
        current = self.current_state.as_dict()
        next_state = SecurityState(
            cea=_clamp(current["CEA"] - degradation * weights["CEA"]),
            aia=_clamp(current["AIA"] - degradation * weights["AIA"]),
            ica=_clamp(current["ICA"] - degradation * weights["ICA"]),
            metadata={"previous": current, "action": action.name},
        )
        self.current_state = next_state
        self.history.append((action, next_state))
        return next_state

    def reset(self) -> None:
        self.current_state = self.initial_state
        self.history.clear()


def contextual_exposure(
    base_value: float,
    audience_size: int,
    sensitivity: float,
    aggregation_factor: float = 1.0,
) -> float:
    """Estimate relational exposure under the Contextual Exposure Principle."""

    if audience_size < 0:
        raise ValueError("audience_size must be non-negative")
    audience_pressure = log1p(audience_size) / 10.0
    return max(0.0, float(base_value) * _clamp(sensitivity) * max(0.0, aggregation_factor) * audience_pressure)


def opacity_migration(before: Mapping[str, float], removed_opacity: float) -> dict[str, float]:
    """Redistribute vulnerability after opacity is removed from one component."""

    removed_opacity = _clamp(removed_opacity)
    if not before:
        return {}
    normalized = {key: max(0.0, float(value)) for key, value in before.items()}
    total = sum(normalized.values()) or 1.0
    migration = removed_opacity / len(normalized)
    return {key: value / total + migration for key, value in normalized.items()}
