"""Generate SVG figures for the repository assets folder."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "assets" / "figures"


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")


def main() -> int:
    write(
        FIGURES / "etc_axes.svg",
        """
<svg xmlns="http://www.w3.org/2000/svg" width="900" height="420" viewBox="0 0 900 420">
  <rect width="900" height="420" fill="#f8fafc"/>
  <text x="450" y="45" text-anchor="middle" font-family="Arial" font-size="26" font-weight="700">Entropic Threat Continuum</text>
  <line x1="160" y1="320" x2="740" y2="320" stroke="#0f172a" stroke-width="3"/>
  <line x1="160" y1="320" x2="450" y2="95" stroke="#0f172a" stroke-width="3"/>
  <line x1="740" y1="320" x2="450" y2="95" stroke="#0f172a" stroke-width="3"/>
  <circle cx="160" cy="320" r="56" fill="#bfdbfe" stroke="#1d4ed8" stroke-width="3"/>
  <circle cx="740" cy="320" r="56" fill="#bbf7d0" stroke="#15803d" stroke-width="3"/>
  <circle cx="450" cy="95" r="56" fill="#fecaca" stroke="#b91c1c" stroke-width="3"/>
  <text x="160" y="315" text-anchor="middle" font-family="Arial" font-size="24" font-weight="700">CEA</text>
  <text x="160" y="340" text-anchor="middle" font-family="Arial" font-size="13">Exposure</text>
  <text x="740" y="315" text-anchor="middle" font-family="Arial" font-size="24" font-weight="700">AIA</text>
  <text x="740" y="340" text-anchor="middle" font-family="Arial" font-size="13">Impersonation</text>
  <text x="450" y="90" text-anchor="middle" font-family="Arial" font-size="24" font-weight="700">ICA</text>
  <text x="450" y="115" text-anchor="middle" font-family="Arial" font-size="13">Corruption</text>
  <text x="450" y="250" text-anchor="middle" font-family="Arial" font-size="17">Security posture is constrained by the weakest axis</text>
</svg>
""",
    )
    write(
        FIGURES / "las_layers.svg",
        """
<svg xmlns="http://www.w3.org/2000/svg" width="760" height="430" viewBox="0 0 760 430">
  <rect width="760" height="430" fill="#ffffff"/>
  <text x="380" y="38" text-anchor="middle" font-family="Arial" font-size="24" font-weight="700">Layered Anonymity Stack</text>
  <g font-family="Arial" font-size="16">
    <rect x="120" y="70" width="520" height="45" fill="#dbeafe" stroke="#1e40af"/><text x="380" y="98" text-anchor="middle">6. Operational Layer</text>
    <rect x="120" y="120" width="520" height="45" fill="#dcfce7" stroke="#166534"/><text x="380" y="148" text-anchor="middle">5. Application Layer</text>
    <rect x="120" y="170" width="520" height="45" fill="#fef3c7" stroke="#92400e"/><text x="380" y="198" text-anchor="middle">4. Routing Layer</text>
    <rect x="120" y="220" width="520" height="45" fill="#fee2e2" stroke="#991b1b"/><text x="380" y="248" text-anchor="middle">3. Network Layer</text>
    <rect x="120" y="270" width="520" height="45" fill="#ede9fe" stroke="#5b21b6"/><text x="380" y="298" text-anchor="middle">2. Link Layer</text>
    <rect x="120" y="320" width="520" height="45" fill="#e2e8f0" stroke="#334155"/><text x="380" y="348" text-anchor="middle">1. Physical Layer</text>
  </g>
  <text x="380" y="398" text-anchor="middle" font-family="Arial" font-size="14">Lower-layer failures can propagate upward into anonymity loss.</text>
</svg>
""",
    )
    print(f"Wrote figures to {FIGURES}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
