"""Layered Anonymity Stack analyzer."""

from __future__ import annotations

from dataclasses import dataclass
from functools import reduce
from operator import mul
from typing import Iterable


DEFAULT_LAYERS = (
    "Physical",
    "Link",
    "Network",
    "Routing",
    "Application",
    "Operational",
)


@dataclass(frozen=True)
class LASLayer:
    """One layer in the Layered Anonymity Stack."""

    name: str
    confidentiality: float
    authentication: float
    integrity: float
    observability: float = 0.0

    def __post_init__(self) -> None:
        for field_name in ("confidentiality", "authentication", "integrity", "observability"):
            value = float(getattr(self, field_name))
            if not 0 <= value <= 1:
                raise ValueError(f"{field_name} must be in [0, 1]")

    @property
    def resilience(self) -> float:
        return min(self.confidentiality, self.authentication, self.integrity) * (1.0 - self.observability)


class LayeredAnonymityStack:
    """Evaluate anonymity posture across the six-layer LAS model."""

    def __init__(self, layers: Iterable[LASLayer]):
        self.layers = list(layers)
        if not self.layers:
            raise ValueError("at least one LAS layer is required")

    @classmethod
    def balanced(cls, score: float = 0.8) -> "LayeredAnonymityStack":
        return cls(LASLayer(name, score, score, score) for name in DEFAULT_LAYERS)

    def overall_resilience(self) -> float:
        return float(reduce(mul, (layer.resilience for layer in self.layers), 1.0) ** (1.0 / len(self.layers)))

    def weakest_layer(self) -> LASLayer:
        return min(self.layers, key=lambda layer: layer.resilience)

    def compromise_path(self, threshold: float = 0.5) -> list[dict[str, float | str]]:
        return [
            {"layer": layer.name, "resilience": layer.resilience}
            for layer in self.layers
            if layer.resilience < threshold
        ]

    def as_table(self) -> list[dict[str, float | str]]:
        return [
            {
                "layer": layer.name,
                "confidentiality": layer.confidentiality,
                "authentication": layer.authentication,
                "integrity": layer.integrity,
                "observability": layer.observability,
                "resilience": layer.resilience,
            }
            for layer in self.layers
        ]
