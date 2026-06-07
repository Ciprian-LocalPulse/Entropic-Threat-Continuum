from pathlib import Path

from taxonomy.taxonomy_validator import load_taxonomy, validate_taxonomy


def test_taxonomy_validates_with_warning_for_representative_json():
    path = Path(__file__).resolve().parents[1] / "src" / "taxonomy" / "plesca_taxonomy.json"
    result = validate_taxonomy(load_taxonomy(path))
    assert result.valid
    assert result.primitive_count > 0
