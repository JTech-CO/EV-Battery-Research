# Dataset selection and matching strategy

[한국어](../ko/09_DATASET_SELECTION.md) · [README](../../README.md)

## Recommended acquisition stack
| Need | First choice | How to use it |
|---|---|---|
| Coherent electrochemical baseline | About:Energy NMC, separate LFP example | Preserve one cell's parameter set and its reference curves |
| Dynamic electrical/temperature testing | LG HG2, selected CALCE collections | Independent benchmark within the exact cell/protocol identity |
| Aging and impedance history | NASA PCoE, Sandia/Archive, CALCE, MATR | Reference tests, cell/batch holdouts and history-aware analysis |
| Condition interactions and expansion | ILCC and Michigan candidates | Obtain primary files and fixture/condition metadata before use |
| Failure heat and mechanical signatures | NLR Failure, ORNL/Sandia v2 | Separate failure-regime model-validation branch |
| Microstructure priors | NLR microstructure library | Agreement-controlled reconstruction with phase provenance |
| Vehicle demand inputs | EPA schedules | Prescribed speed boundary; vehicle conversion still required |
| Model/schema references | PyBaMM, BPX, BLAST, Materials Project | Definitions and priors, not experimental ground truth |

These are engineering priorities based on complementarity, not a ranking by file count. Read the individual cards for acquisition/rights limitations. Several original landing pages were blocked, several file lists were JavaScript-only, and some data requires a request or agreement. No bypass or submission was attempted.

## Same-cell matching gate
Before combining data, compare manufacturer/variant, positive and negative composition, format, capacity, electrode geometry, formation/batch, electrolyte, temperature, SOC definition, rate, cutoff, rest and age. A mismatch does not necessarily make a source useless; it changes the role from direct calibration evidence to a transfer prior or external comparison. Record that role explicitly.

“Same chemistry” is weaker than “same commercial cell,” which is weaker than “same batch/specimen.” Do not construct a supposedly measured virtual cell from NMC811 diffusion, NMC111 OCP, another cell's thermal conductivity and an unrelated aging law without a documented uncertainty/transfer model.

## Three proposed evidence bundles
**Bundle A: reproducible source benchmark.** The two captured About:Energy sets plus their original validation files. Suitable for checking parameter semantics and source benchmark reproduction, not proof of independent validation.

**Bundle B: matched electrothermal cell.** A chosen single commercial variant with temperature-resolved pulses, cycling, entropy/calorimetry and geometry. The complete matched bundle is not yet acquired.

**Bundle C: aging/module realism.** Add calendar/cycle matrices, expansion/EIS diagnostics and a documented module's thermal/electrical/control data. This is a later evidence target, not a present dataset.

Always count original specimens rather than file copies. Preserve calibration, source-provided reference and truly held-out evidence as separate labels.

## Source basis

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S07: CALCE battery data](https://calce.umd.edu/battery-data)
- [S08: NASA Li-ion aging catalog](https://data.nasa.gov/dataset/li-ion-battery-aging-datasets)
- [S09: NASA PCoE data repository](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/)
- [S10: LG HG2 dataset v3](https://data.mendeley.com/datasets/cp3473x7xv/3)
- [S11: Battery Archive study summaries](https://batteryarchive.org/study_summaries.html)
- [S13: Mechanically induced thermal runaway v2](https://data.mendeley.com/datasets/sn2kv34r4h/2)
- [S14: Battery Failure Databank](https://www.nlr.gov/transportation/battery-failure)
- [S15: Battery Microstructures Library](https://www.nlr.gov/transportation/microstructure)
- [S17: EPA dynamometer schedules](https://www.epa.gov/vehicle-and-fuel-emissions-testing/dynamometer-drive-schedules)
- [S25: Severson/Attia original data-processing repository](https://github.com/rdbraatz/data-driven-prediction-of-battery-cycle-life-before-capacity-degradation)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.
