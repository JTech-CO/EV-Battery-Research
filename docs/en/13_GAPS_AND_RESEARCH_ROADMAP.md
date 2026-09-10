# Gap analysis and research gates

[한국어](../ko/13_GAPS_AND_RESEARCH_ROADMAP.md) · [README](../../README.md)

## Missing evidence that most affects realism
The present baseline lacks independent matched-cell thermal validation, broad temperature characterization, mechanism-resolved aging coefficients, original specimen/batch traceability and OEM pack topology/control/cooling information. LFP phase/hysteresis behavior and composite-electrode mechanics require model-specific evidence beyond a basic parameter exchange file. These are explicit data gaps, not proof that physics-based modeling is impossible.

| Gate | Evidence required before advancing | Stop condition |
|---|---|---|
| G0 Provenance | Original/capture reconciliation, rights, units and identities | Unresolved source or silent transcription mismatch |
| G1 Cell baseline | Same-cell parameter definitions and source curve reproduction | Compensating arbitrary parameters to hide model mismatch |
| G2 Electrothermal | Multiple temperatures and independent real thermal observations | Treating estimated properties/setpoints as measured validation |
| G3 Aging | Defined calendar/cycle matrices and mechanism-relevant diagnostics | Fitting all mechanisms from capacity alone |
| G4 Module/pack | Electrical/thermal graphs, control and synchronized observations | Claiming OEM pack fidelity from a single-cell multiplier |
| G5 Generalization | Held-out cells/batches/protocols, uncertainty and out-of-domain tests | Leakage, mirrored data duplication or unqualified extrapolation |

## Immediate collection backlog
Obtain the 16 pinned About:Energy blobs and run semantic comparison. Inspect full CSV headers and protocol conditions before creating adapters. Retrieve the licensed HG2 and mechanical-failure manifests from official exports. Review selected CALCE/NASA rights and request selected Battery Archive studies. Resolve the blocked Oxford/ILCC/Michigan primary pages and capture exact licenses/versions. Do not treat any of those actions as already completed.

The next scientifically valuable acquisition is not necessarily the biggest archive. A smaller, well-characterized, matched-cell calorimetry/pulse/OCV set may remove more uncertainty than thousands of unmatched cycle-life curves. This prioritization should be revisited after sensitivity/identifiability analysis.

## Work products for the next research phase
Produce a frozen cell identity dossier, versioned parameter source map, calibration/holdout protocol table, missing-observable ledger, uncertainty budget and rights-reviewed raw-data manifest. Only after those are approved should a separate implementation task create a scientific kernel or UI.

This repository makes no schedule or performance promise. It defines evidence gates and records which ones remain open. Future additions should preserve the initial captures and append a dated revision rather than quietly replacing source data or narrowing a failed validation report.

## Source basis

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S03: PyBaMM thermal models](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/thermal-models.html)
- [S04: PyBaMM coupled degradation](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/coupled-degradation.html)
- [S06: BPX official standard download and change notes](https://bpxstandard.com/bpx-standard/)
- [S10: LG HG2 dataset v3](https://data.mendeley.com/datasets/cp3473x7xv/3)
- [S11: Battery Archive study summaries](https://batteryarchive.org/study_summaries.html)
- [S14: Battery Failure Databank](https://www.nlr.gov/transportation/battery-failure)
- [S15: Battery Microstructures Library](https://www.nlr.gov/transportation/microstructure)
- [S24: Michigan expansion dataset landing](https://deepblue.lib.umich.edu/data/concern/data_sets/5d86p0488)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.
