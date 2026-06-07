"""Trust Decay Function model."""

from __future__ import annotations

from dataclasses import dataclass, field
from math import exp


@dataclass(frozen=True)
class BreachEvent:
    """A discrete event that reduces credential trust after a given time."""

    time: float
    severity: float
    label: str = ""

    def __post_init__(self) -> None:
        if self.time < 0:
            raise ValueError("time must be non-negative")
        if not 0 <= self.severity <= 1:
            raise ValueError("severity must be in [0, 1]")


@dataclass
class CredentialTrust:
    """Continuous trust decay with multiplicative breach shocks."""

    initial_trust: float = 1.0
    decay_rate: float = 0.01
    breach_events: list[BreachEvent] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not 0 <= self.initial_trust <= 1:
            raise ValueError("initial_trust must be in [0, 1]")
        if self.decay_rate < 0:
            raise ValueError("decay_rate must be non-negative")

    def add_breach(self, event: BreachEvent) -> None:
        self.breach_events.append(event)
        self.breach_events.sort(key=lambda item: item.time)

    def trust_at(self, time: float) -> float:
        if time < 0:
            raise ValueError("time must be non-negative")
        trust = self.initial_trust * exp(-self.decay_rate * time)
        for event in self.breach_events:
            if event.time <= time:
                trust *= 1.0 - event.severity
        return max(0.0, min(1.0, float(trust)))

    def timeline(self, start: float, stop: float, steps: int) -> list[dict[str, float]]:
        if steps < 2:
            raise ValueError("steps must be at least 2")
        if stop < start:
            raise ValueError("stop must be greater than or equal to start")
        delta = (stop - start) / (steps - 1)
        return [
            {"time": start + index * delta, "trust": self.trust_at(start + index * delta)}
            for index in range(steps)
        ]
