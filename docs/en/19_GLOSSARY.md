# Technical glossary

[한국어](../ko/19_GLOSSARY.md) · [README](../../README.md)

| Term | Expansion | Interpretation |
|---|---|---|
| SOC | State of charge | Reference-dependent usable-charge coordinate; not electrode stoichiometry. |
| SOH | State of health | Always specify capacity, resistance or another definition and reference conditions. |
| OCP / OCV | Open-circuit potential / voltage | State electrode/reference identity and rest/measurement conditions. |
| DFN / P2D | Doyle-Fuller-Newman / pseudo-two-dimensional | Through-electrode and representative-particle dimensions are not literal 3D geometry. |
| SPM / SPMe | Single particle model / with electrolyte | Reduced models with explicit assumptions and operating domains. |
| ECM | Equivalent circuit model | Terminal behavior approximation; internal chemistry is not directly resolved. |
| SEI | Solid electrolyte interphase | A layer and associated mechanisms, not synonymous with all capacity fade. |
| LLI / LAM | Lithium inventory / active-material loss | Distinct latent states requiring supporting evidence. |
| EIS | Electrochemical impedance spectroscopy | Record frequency, excitation, rest, SOC/T and complex signs. |
| GITT / PITT | Intermittent titration methods | Diffusion-related inference depends on model and experimental assumptions. |
| HPPC | Hybrid pulse power characterization | Pulse duration is part of resistance/response definition. |
| DOD / EFC | Depth of discharge / equivalent full cycles | State the SOC/throughput denominator and counting convention. |
| C-rate | Current relative to a reference capacity | Reference Ah and current A are both needed. |
| BPX | Battery Parameter eXchange | Versioned parameter semantics, not automatic model validation. |
| Semantic capture | Transcribed or reserialized source content | Not necessarily byte-identical to the upstream file. |
| Ground truth | Reference observation with known limitations | Not a synonym for BMS estimates, synthetic data or fitted curves. |
| Identifiability | Ability to constrain parameters from observations | Small residuals alone do not establish unique physical parameters. |
| Model discrepancy | Error from incomplete model structure | Must not be hidden entirely inside parameter uncertainty. |

## Source basis

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S02: PyBaMM DFN equations](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/DFN.html)
- [S05: PyBaMM parameterisation](https://docs.pybamm.org/en/latest/source/examples/notebooks/parameterization/parameterization.html)
- [S06: BPX official standard download and change notes](https://bpxstandard.com/bpx-standard/)
- [S07: CALCE battery data](https://calce.umd.edu/battery-data)
- [S08: NASA Li-ion aging catalog](https://data.nasa.gov/dataset/li-ion-battery-aging-datasets)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.
