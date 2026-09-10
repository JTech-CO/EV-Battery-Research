# Research summary and decision

[한국어](../ko/00_RESEARCH_SUMMARY.md) · [README](../../README.md)

## Decision
Build the future research program around **one internally consistent cell parameterization**, not a pool of unrelated battery measurements. Start with the About:Energy NMC111/graphite 12.5 Ah pouch example. Keep the LFP/graphite 2 Ah cylindrical example as a separate chemistry/model-form benchmark. Neither is a verified representation of a current production EV pack. Both source files identify legacy BPX 0.1 and explicitly mix characterization, literature inputs and estimated thermal properties. [S01]

The scientific deliverable should eventually be a set of validated mappings from current, initial state, temperature, cooling and history to terminal voltage, material states, heat generation and aging observables. A realistic rendering or a numerically converged DFN solution alone is not evidence of physical accuracy.

## Four data layers
| Layer | Necessary content | Current package |
|---|---|---|
| Constitutive data | Geometry, electrode OCP, diffusion, reaction rates, electrolyte transport, thermal properties | Two source parameter sets captured; mixed evidence quality |
| Experiments | Charge/discharge, pulses, rest, EIS, calorimetry, aging and expansion | NMC embedded reference curves captured; other studies cataloged |
| Boundary/control conditions | Cooling, pack topology, drive demand, BMS limits, sensors | US06 speed schedule captured; OEM pack/control data missing |
| Evidence | Specimen identity, units, methods, uncertainty, license, version, calibration/holdout roles | Schemas, inventories, provenance and acquisition records |

## What is actually included
The archive contains two **manually transcribed/reserialized JSON captures**, 104 parameter entries extracted from them, 114 NMC embedded reference-curve points and 601 EPA prescribed speed samples. It also contains 404 samples of published OCP fits; these are derived values, not new measurements. The 139-row requirement inventory is a specification of needed information, not 139 acquired measurements.

There are 23 resource cards, including experimental collections, parameter examples, a standard and software references. Do not report this as 23 downloaded experimental datasets. Sixteen immutable About:Energy Git blobs are indexed for later download; none of those raw byte files was downloaded here. No simulation, calibration, ML training, original-data semantic equality check, account change or repository publication was performed.

## Priority
First reconcile the captured BPX files with their original blobs and obtain all matching validation CSVs. Next add independent temperature/thermal measurements for the same cell. Only then introduce identified aging mechanisms and an explicitly parameterized module/pack. Public data supports a rigorous bounded research model; it does not justify a claim of an exact OEM digital twin.

## Source basis

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S06: BPX official standard download and change notes](https://bpxstandard.com/bpx-standard/)
- [S10: LG HG2 dataset v3](https://data.mendeley.com/datasets/cp3473x7xv/3)
- [S17: EPA dynamometer schedules](https://www.epa.gov/vehicle-and-fuel-emissions-testing/dynamometer-drive-schedules)
- [S18: EPA US06 numeric schedule](https://www.epa.gov/system/files/other-files/2025-03/us06col.txt)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.
