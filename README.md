# Entropic Threat Continuum

**A unified theoretical and computational framework for information security, adversarial uncertainty, anonymity networks, and attack-surface quantification.**

Author: **Ciprian Stefan Plesca**  
Primary source: *From Cipher to Shadow: A Unified Theoretical Framework for Information Security from Its Epistemic Origins to the Architecture of the Dark Web* (Doctoral Dissertation, 2024)  
License: **MIT**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](./pyproject.toml)
[![Tests](https://img.shields.io/badge/Tests-pytest-informational.svg)](./tests)

![From Cipher to Shadow hero artwork](./assets/figures/from-cipher-to-shadow-hero.png)

---

## Purpose

This repository turns the dissertation's theoretical work into a complete, inspectable, reusable research package. It contains formal definitions, simulation code, a machine-readable taxonomy, reproducibility scripts, assets, tests, notebooks, and citation metadata.

The central contribution is the **Entropic Threat Continuum (ETC)**, a model of information security as a dynamic adversarial continuum governed by three invariant axes:

| Axis | Symbol | Question answered |
|---|---:|---|
| Confidentiality-Exposure Axis | CEA | Can protected information be exposed? |
| Authentication-Impersonation Axis | AIA | Can identity or authority be forged? |
| Integrity-Corruption Axis | ICA | Can information or system state be corrupted? |

---

## Original Constructs

- **Entropic Threat Continuum (ETC)**: five-tuple model `(S, A, T, D, E)` for security states, adversarial actions, transitions, measurements, and effort.
- **Adversarial Entropy Gradient (AEG)**: quantifies how adversarial effort reduces uncertainty.
- **Trust Decay Function (TDF)**: models credential trust degradation through time and breach events.
- **Dark Topology Conjecture (DTC)**: relates network algebraic connectivity to anonymity-set behavior.
- **Layered Anonymity Stack (LAS)**: six-layer model for anonymous overlay networks.
- **Threat Surface Integral (TSI)**: integrates vulnerability, probability, and impact across attack vectors.
- **Contextual Exposure Principle (CEP)** and **Opacity Migration Theorem (OMT)**: formal principles for relational exposure and vulnerability migration.
- **Plesca Taxonomy**: ETC-axis attack classification with 847 declared primitive types.

---

## Repository Map

```text
.
|-- README.md
|-- LICENSE
|-- CITATION.cff
|-- CHANGELOG.md
|-- pyproject.toml
|-- dissertation/
|-- docs/
|   |-- FRAMEWORK_OVERVIEW.md
|   |-- FORMAL_DEFINITIONS.md
|   |-- TAXONOMY_REFERENCE.md
|   |-- GLOSSARY.md
|   |-- API_REFERENCE.md
|   |-- ERRATA.md
|   `-- ROADMAP.md
|-- src/
|   |-- simulation/
|   |   |-- etc_framework.py
|   |   |-- aeg_model.py
|   |   |-- tdf_model.py
|   |   |-- tsi_calculator.py
|   |   |-- las_analyzer.py
|   |   |-- dtc_simulation.py
|   |   `-- utils.py
|   `-- taxonomy/
|       |-- plesca_taxonomy.json
|       `-- taxonomy_validator.py
|-- assets/
|   |-- figures/
|   |-- diagrams/
|   `-- data/
|-- notebooks/
|-- scripts/
|-- tests/
`-- citation/
```

---

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

On Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
pytest
```

---

## Examples

Run a compact Dark Topology Conjecture simulation:

```bash
python -m simulation.dtc_simulation --n 60 --configs 5 --runs 5 --alpha 0.20
```

Validate the taxonomy:

```bash
python scripts/validate_taxonomy.py
```

Generate reproducibility figures and sample CSV outputs:

```bash
python scripts/generate_figures.py
```

Use the core framework from Python:

```python
from simulation import SecurityState, etc_security_functional

state = SecurityState(cea=0.82, aia=0.74, ica=0.91)
print(etc_security_functional(state))
```

---

## Academic Scope and Ethics

This repository is intended for research, education, defensive security modeling, privacy engineering, and reproducible academic discussion. It does not provide operational instructions for unauthorized access, exploitation, or abuse. The models are abstractions and should not be treated as substitutes for professional security assessment.

---

## Citation

If this repository or the dissertation's theoretical constructs are useful in academic work, cite:

```text
Plesca, C. S. (2024). From cipher to shadow: A unified theoretical framework
for information security from its epistemic origins to the architecture of the
Dark Web [Doctoral dissertation].
```

Machine-readable citation metadata is available in [`CITATION.cff`](./CITATION.cff), and BibTeX is available in [`citation/bibtex.bib`](./citation/bibtex.bib).

---

## Support This Research

This work represents years of independent research in information security theory, privacy engineering, anonymity networks, and post-quantum cryptographic transitions. Donations help sustain future publications, simulation infrastructure, open-access dissemination, and academic conference or peer-review costs.

100% of donations received through this repository are allocated to research continuation, open-access dissemination, simulation infrastructure, and academic review or conference activity. See [`DONATE.md`](./DONATE.md) for the full donation policy, institutional support options, and acknowledgement preferences.

<br>

<!-- ═══════════════════════════════════════════════════════════════
     ENTROPIC THREAT CONTINUUM — DONATION PANEL
     Axes: CEA (Confidentiality-Exposure) · AIA (Authentication-Impersonation) · ICA (Integrity-Corruption)
     ═══════════════════════════════════════════════════════════════ -->

<table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,monospace;">
<tr><td>

<!-- ── ETC BANNER ─────────────────────────────────────────────── -->
<table width="100%" cellpadding="16" cellspacing="0" border="0"
  style="background:#f6f8fa;border:1px solid #d0d7de;border-radius:12px;margin-bottom:16px;">
  <tr>
    <td>
      <strong style="font-size:13px;color:#1f2328;">Entropic Threat Continuum — Research Support</strong><br><br>
      <code style="background:#eeedfe;color:#3c3489;padding:3px 8px;border-radius:4px;font-size:11px;margin-right:6px;">CEA</code>
      <code style="background:#e1f5ee;color:#085041;padding:3px 8px;border-radius:4px;font-size:11px;margin-right:6px;">AIA</code>
      <code style="background:#e6f1fb;color:#0c447c;padding:3px 8px;border-radius:4px;font-size:11px;">ICA</code>
    </td>
    <td align="right" style="font-size:11px;color:#656d76;white-space:nowrap;">
      100% toward research<br>open-access &amp; dissemination
    </td>
  </tr>
</table>

<!-- ── EUR CARD ────────────────────────────────────────────────── -->
<table width="100%" cellpadding="0" cellspacing="0" border="0"
  style="border:1px solid #d0d7de;border-radius:12px;margin-bottom:12px;overflow:hidden;">
  <tr>
    <td style="background:#f6f8fa;padding:12px 18px;border-bottom:1px solid #d0d7de;">
      <table width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
        <td style="font-size:20px;width:36px;">🇪🇺</td>
        <td style="padding-left:10px;">
          <strong style="font-size:14px;color:#1f2328;">European Payment</strong><br>
          <span style="font-size:11px;color:#656d76;">SEPA / EUR</span>
        </td>
        <td align="right">
          <code style="background:#eeedfe;color:#3c3489;padding:3px 8px;border-radius:4px;font-size:10px;">CEA · AES-256</code>
        </td>
      </tr></table>
    </td>
  </tr>
  <tr><td style="padding:0 18px;">
    <table width="100%" cellpadding="8" cellspacing="0" border="0" style="font-size:13px;">
      <tr style="border-bottom:1px solid #f0f0f0;">
        <td style="color:#656d76;width:140px;">Recipient</td>
        <td><code>Ciprian Stefan Plesca</code></td>
      </tr>
      <tr style="border-bottom:1px solid #f0f0f0;">
        <td style="color:#656d76;">IBAN</td>
        <td><code>BE83 9679 1975 8915</code></td>
      </tr>
      <tr style="border-bottom:1px solid #f0f0f0;">
        <td style="color:#656d76;">SWIFT / BIC</td>
        <td><code>TRWIBEB1XXX</code></td>
      </tr>
      <tr>
        <td style="color:#656d76;">Bank</td>
        <td style="font-size:11px;color:#656d76;">Wise, Rue du Trône 100, 3rd floor, Brussels, 1050, Belgium</td>
      </tr>
    </table>
  </td></tr>
</table>

<!-- ── GBP CARD ────────────────────────────────────────────────── -->
<table width="100%" cellpadding="0" cellspacing="0" border="0"
  style="border:1px solid #d0d7de;border-radius:12px;margin-bottom:12px;overflow:hidden;">
  <tr>
    <td style="background:#f6f8fa;padding:12px 18px;border-bottom:1px solid #d0d7de;">
      <table width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
        <td style="font-size:20px;width:36px;">🇬🇧</td>
        <td style="padding-left:10px;">
          <strong style="font-size:14px;color:#1f2328;">United Kingdom Payment</strong><br>
          <span style="font-size:11px;color:#656d76;">Faster Payments / GBP</span>
        </td>
        <td align="right">
          <code style="background:#e1f5ee;color:#085041;padding:3px 8px;border-radius:4px;font-size:10px;">AIA · SHA-3</code>
        </td>
      </tr></table>
    </td>
  </tr>
  <tr><td style="padding:0 18px;">
    <table width="100%" cellpadding="8" cellspacing="0" border="0" style="font-size:13px;">
      <tr style="border-bottom:1px solid #f0f0f0;">
        <td style="color:#656d76;width:140px;">Recipient</td>
        <td><code>Ciprian Stefan Plesca</code></td>
      </tr>
      <tr style="border-bottom:1px solid #f0f0f0;">
        <td style="color:#656d76;">Account number</td>
        <td><code>92055372</code></td>
      </tr>
      <tr style="border-bottom:1px solid #f0f0f0;">
        <td style="color:#656d76;">Sort code</td>
        <td><code>23-14-70</code></td>
      </tr>
      <tr style="border-bottom:1px solid #f0f0f0;">
        <td style="color:#656d76;">IBAN</td>
        <td><code>GB68 TRWI 2314 7092 0553 72</code></td>
      </tr>
      <tr style="border-bottom:1px solid #f0f0f0;">
        <td style="color:#656d76;">SWIFT / BIC</td>
        <td><code>TRWIGB2LXXX</code></td>
      </tr>
      <tr>
        <td style="color:#656d76;">Bank</td>
        <td style="font-size:11px;color:#656d76;">Wise Payments Limited, 1st Floor, Worship Square, 65 Clifton Street, London, EC2A 4JE, United Kingdom</td>
      </tr>
    </table>
  </td></tr>
</table>

<!-- ── USD CARD ────────────────────────────────────────────────── -->
<table width="100%" cellpadding="0" cellspacing="0" border="0"
  style="border:1px solid #d0d7de;border-radius:12px;margin-bottom:12px;overflow:hidden;">
  <tr>
    <td style="background:#f6f8fa;padding:12px 18px;border-bottom:1px solid #d0d7de;">
      <table width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
        <td style="font-size:20px;width:36px;">🇺🇸</td>
        <td style="padding-left:10px;">
          <strong style="font-size:14px;color:#1f2328;">United States Payment</strong><br>
          <span style="font-size:11px;color:#656d76;">ACH / Wire / USD</span>
        </td>
        <td align="right">
          <code style="background:#e6f1fb;color:#0c447c;padding:3px 8px;border-radius:4px;font-size:10px;">ICA · RSA-4096</code>
        </td>
      </tr></table>
    </td>
  </tr>
  <tr><td style="padding:0 18px;">
    <table width="100%" cellpadding="8" cellspacing="0" border="0" style="font-size:13px;">
      <tr style="border-bottom:1px solid #f0f0f0;">
        <td style="color:#656d76;width:140px;">Recipient</td>
        <td><code>Ciprian Stefan Plesca</code></td>
      </tr>
      <tr style="border-bottom:1px solid #f0f0f0;">
        <td style="color:#656d76;">Account type</td>
        <td><code>Checking</code></td>
      </tr>
      <tr style="border-bottom:1px solid #f0f0f0;">
        <td style="color:#656d76;">Routing number</td>
        <td><code>026073150</code></td>
      </tr>
      <tr style="border-bottom:1px solid #f0f0f0;">
        <td style="color:#656d76;">Account number</td>
        <td><code>8314225367</code></td>
      </tr>
      <tr style="border-bottom:1px solid #f0f0f0;">
        <td style="color:#656d76;">SWIFT / BIC</td>
        <td><code>CMFGUS33</code></td>
      </tr>
      <tr>
        <td style="color:#656d76;">Bank</td>
        <td style="font-size:11px;color:#656d76;">Community Federal Savings Bank, 89-16 Jamaica Ave, Woodhaven, NY, 11421, United States</td>
      </tr>
    </table>
  </td></tr>
</table>

<!-- ── CRYPTO ─────────────────────────────────────────────────── -->
<table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom:12px;">
  <tr>
    <td width="49%" style="padding-right:6px;">
      <table width="100%" cellpadding="12" cellspacing="0" border="0"
        style="border:1px solid #d0d7de;border-radius:10px;">
        <tr>
          <td>
            <table cellpadding="0" cellspacing="0" border="0" style="margin-bottom:10px;"><tr>
              <td style="background:#faeeda;border-radius:6px;width:28px;height:28px;text-align:center;vertical-align:middle;font-weight:700;color:#633806;font-size:14px;">₿</td>
              <td style="padding-left:8px;">
                <strong style="font-size:12px;color:#1f2328;">Bitcoin</strong><br>
                <span style="font-size:10px;color:#656d76;">BTC</span>
              </td>
            </tr></table>
            <code style="font-size:10px;color:#656d76;word-break:break-all;">bc1qf3yy0w8z37rwavxpu38wem3yffpanw7wzj32qj</code>
          </td>
        </tr>
      </table>
    </td>
    <td width="49%" style="padding-left:6px;">
      <table width="100%" cellpadding="12" cellspacing="0" border="0"
        style="border:1px solid #d0d7de;border-radius:10px;">
        <tr>
          <td>
            <table cellpadding="0" cellspacing="0" border="0" style="margin-bottom:10px;"><tr>
              <td style="background:#eeedfe;border-radius:6px;width:28px;height:28px;text-align:center;vertical-align:middle;font-weight:700;color:#3c3489;font-size:14px;">Ξ</td>
              <td style="padding-left:8px;">
                <strong style="font-size:12px;color:#1f2328;">Ethereum</strong><br>
                <span style="font-size:10px;color:#656d76;">ETH</span>
              </td>
            </tr></table>
            <code style="font-size:10px;color:#656d76;word-break:break-all;">0x27d9a6a5b8507e6031bb044319410da96222d402</code>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>

<!-- ── PAYPAL ─────────────────────────────────────────────────── -->
<table width="100%" cellpadding="12" cellspacing="0" border="0"
  style="border:1px solid #d0d7de;border-radius:10px;">
  <tr>
    <td style="width:36px;background:#e6f1fb;border-radius:8px;text-align:center;vertical-align:middle;font-weight:700;color:#0c447c;font-size:13px;">PP</td>
    <td style="padding-left:12px;">
      <strong style="font-size:13px;color:#1f2328;">PayPal</strong><br>
      <a href="https://paypal.me/agentflowenterprise" style="font-size:12px;color:#0969da;">paypal.me/agentflowenterprise</a>
    </td>
  </tr>
</table>

</td></tr>
</table>

---

## License

This repository is released under the MIT License. See [`LICENSE`](./LICENSE).
