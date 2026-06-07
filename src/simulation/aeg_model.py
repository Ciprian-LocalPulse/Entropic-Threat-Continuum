"""Adversarial Entropy Gradient model."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class EntropyObservation:
    """One observed point in the effort/uncertainty curve."""

    effort: float
    entropy: float


class AdversarialEntropyGradient:
    """Estimate how quickly adversarial effort reduces uncertainty."""

    def __init__(self, observations: list[EntropyObservation]):
        if len(observations) < 2:
            raise ValueError("at least two observations are required")
        ordered = sorted(observations, key=lambda item: item.effort)
        efforts = np.array([item.effort for item in ordered], dtype=float)
        entropies = np.array([item.entropy for item in ordered], dtype=float)
        if np.any(efforts < 0):
            raise ValueError("effort values must be non-negative")
        if np.any(entropies < 0):
            raise ValueError("entropy values must be non-negative")
        if len(np.unique(efforts)) != len(efforts):
            raise ValueError("effort values must be unique")
        self.observations = ordered
        self.efforts = efforts
        self.entropies = entropies

    def gradient(self) -> np.ndarray:
        """Return -dH/dE so positive values mean adversarial progress."""

        return -np.gradient(self.entropies, self.efforts)

    def mean_gradient(self) -> float:
        return float(np.mean(self.gradient()))

    def marginal_efficiency(self) -> list[dict[str, float]]:
        gradients = self.gradient()
        return [
            {"effort": float(effort), "entropy": float(entropy), "gradient": float(gradient)}
            for effort, entropy, gradient in zip(self.efforts, self.entropies, gradients)
        ]

    def fit_exponential_decay(self) -> dict[str, float]:
        """Fit entropy ~= floor + amplitude * exp(-rate * effort)."""

        floor = float(max(0.0, np.min(self.entropies) * 0.95))
        shifted = np.maximum(self.entropies - floor, 1e-9)
        slope, intercept = np.polyfit(self.efforts, np.log(shifted), 1)
        return {
            "floor": floor,
            "amplitude": float(np.exp(intercept)),
            "rate": float(max(0.0, -slope)),
            "r2": self._log_fit_r2(slope, intercept, shifted),
        }

    def predict(self, effort: float) -> float:
        params = self.fit_exponential_decay()
        return float(params["floor"] + params["amplitude"] * np.exp(-params["rate"] * effort))

    def _log_fit_r2(self, slope: float, intercept: float, shifted: np.ndarray) -> float:
        actual = np.log(shifted)
        predicted = slope * self.efforts + intercept
        ss_res = float(np.sum((actual - predicted) ** 2))
        ss_tot = float(np.sum((actual - np.mean(actual)) ** 2))
        return 1.0 if ss_tot == 0 else float(1.0 - ss_res / ss_tot)
