# ETC Framework - Relationships Between Constructs

```mermaid
flowchart TD
    ETC["Entropic Threat Continuum<br/>(S, A, T, D, E)"]
    CEA["CEA<br/>Confidentiality-Exposure"]
    AIA["AIA<br/>Authentication-Impersonation"]
    ICA["ICA<br/>Integrity-Corruption"]
    AEG["Adversarial Entropy Gradient"]
    TDF["Trust Decay Function"]
    DTC["Dark Topology Conjecture"]
    LAS["Layered Anonymity Stack"]
    TSI["Threat Surface Integral"]
    TAX["Plesca Taxonomy"]

    ETC --> CEA
    ETC --> AIA
    ETC --> ICA
    AEG --> ETC
    TDF --> AIA
    DTC --> LAS
    LAS --> CEA
    LAS --> AIA
    TSI --> TAX
    TAX --> CEA
    TAX --> AIA
    TAX --> ICA
```

The constructs are deliberately coupled: ETC supplies the coordinate system, the taxonomy supplies the vector catalogue, and AEG/TDF/TSI/LAS/DTC provide specialized analytic lenses.
