"""Validate the machine-readable Plesca Taxonomy artifact."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

AXES = ("CEA", "AIA", "ICA")
LEVELS = ("Physical", "Logical", "Social", "Combinatorial")
REQUIRED_PRIMITIVE_FIELDS = ("code", "name", "complexity", "description", "primary_defense")
CODE_PATTERN = re.compile(r"^(CEA|AIA|ICA)-[PLSC]-\d{2,}$")


@dataclass
class TaxonomyValidationResult:
    valid: bool
    primitive_count: int
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def load_taxonomy(path: str | Path) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_taxonomy(data: dict[str, Any]) -> TaxonomyValidationResult:
    errors: list[str] = []
    warnings: list[str] = []
    primitive_count = 0

    if "_meta" not in data:
        errors.append("missing _meta section")
    if "axes" not in data:
        errors.append("missing axes section")
    if "primitives" not in data:
        errors.append("missing primitives section")
        return TaxonomyValidationResult(False, 0, errors, warnings)

    for axis in AXES:
        if axis not in data.get("axes", {}):
            errors.append(f"missing axis metadata: {axis}")
        if axis not in data["primitives"]:
            errors.append(f"missing primitive axis: {axis}")
            continue
        for level in LEVELS:
            primitives = data["primitives"][axis].get(level)
            if primitives is None:
                errors.append(f"missing level {axis}/{level}")
                continue
            if not isinstance(primitives, list):
                errors.append(f"{axis}/{level} must be a list")
                continue
            primitive_count += len(primitives)
            for index, primitive in enumerate(primitives):
                _validate_primitive(axis, level, index, primitive, errors)

    declared_total = data.get("_meta", {}).get("total_primitives")
    if isinstance(declared_total, int) and declared_total != primitive_count:
        warnings.append(
            f"declared total_primitives is {declared_total}, while this JSON contains {primitive_count} listed entries"
        )

    return TaxonomyValidationResult(valid=not errors, primitive_count=primitive_count, errors=errors, warnings=warnings)


def _validate_primitive(axis: str, level: str, index: int, primitive: Any, errors: list[str]) -> None:
    location = f"{axis}/{level}[{index}]"
    if not isinstance(primitive, dict):
        errors.append(f"{location} must be an object")
        return
    for field_name in REQUIRED_PRIMITIVE_FIELDS:
        if not primitive.get(field_name):
            errors.append(f"{location} missing {field_name}")
    code = str(primitive.get("code", ""))
    if code and not CODE_PATTERN.match(code):
        errors.append(f"{location} has invalid code format: {code}")
    if code and not code.startswith(axis):
        errors.append(f"{location} code axis mismatch: {code}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Plesca Taxonomy JSON.")
    parser.add_argument("path", nargs="?", default="src/taxonomy/plesca_taxonomy.json")
    args = parser.parse_args()
    result = validate_taxonomy(load_taxonomy(args.path))
    print(f"valid={result.valid}")
    print(f"primitive_count={result.primitive_count}")
    for warning in result.warnings:
        print(f"warning: {warning}")
    for error in result.errors:
        print(f"error: {error}")
    return 0 if result.valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
