"""Entropic Threat Continuum simulation and modeling package."""

from .etc_framework import (
    ETCFramework,
    SecurityState,
    ThreatAction,
    contextual_exposure,
    etc_security_functional,
    opacity_migration,
)

__all__ = [
    "ETCFramework",
    "SecurityState",
    "ThreatAction",
    "contextual_exposure",
    "etc_security_functional",
    "opacity_migration",
]

__version__ = "1.1.0"
__author__ = "Ciprian Stefan Plesca"
