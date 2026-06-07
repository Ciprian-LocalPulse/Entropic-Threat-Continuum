"""Threat Surface Integral model."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, Mapping

from .etc_framework import AXES


@dataclass(frozen=True)
class AttackVector:
    """One vector in a threat surface integral."""

    code: str
    axis: str
    vulnerability: float
    probability: float
    impact: float
    weight: float = 1.0
    metadata: Mapping[str, object] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.axis.upper() not in AXES:
            raise ValueError(f"axis must be one of {AXES}")
        for field_name in ("vulnerability", "probability", "impact", "weight"):
            value = float(getattr(self, field_name))
            if value < 0:
                raise ValueError(f"{field_name} must be non-negative")

    @property
    def exposure(self) -> float:
        return float(self.vulnerability * self.probability * self.impact * self.weight)


class ThreatSurfaceIntegral:
    """Discrete approximation of the ETC threat-surface integral."""

    def __init__(self, vectors: Iterable[AttackVector] = ()):
        self.vectors = list(vectors)

    def add(self, vector: AttackVector) -> None:
        self.vectors.append(vector)

    def total(self) -> float:
        return float(sum(vector.exposure for vector in self.vectors))

    def by_axis(self) -> dict[str, float]:
        totals = {axis: 0.0 for axis in AXES}
        for vector in self.vectors:
            totals[vector.axis.upper()] += vector.exposure
        return totals

    def normalized_by_axis(self) -> dict[str, float]:
        totals = self.by_axis()
        total = sum(totals.values())
        if total == 0:
            return totals
        return {axis: value / total for axis, value in totals.items()}

    def top_vectors(self, limit: int = 10) -> list[AttackVector]:
        return sorted(self.vectors, key=lambda vector: vector.exposure, reverse=True)[:limit]

    def report(self) -> dict[str, object]:
        return {
            "total_exposure": self.total(),
            "axis_totals": self.by_axis(),
            "axis_share": self.normalized_by_axis(),
            "top_vectors": [
                {"code": vector.code, "axis": vector.axis.upper(), "exposure": vector.exposure}
                for vector in self.top_vectors()
            ],
        }
