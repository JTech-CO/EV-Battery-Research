# BPX semantics and version control

[한국어](../ko/15_BPX_AND_VERSIONING.md) · [README](../../README.md)

## Legacy capture versus current documentation
The captured About:Energy examples explicitly declare **BPX 0.1** and were parameterized in December 2022. The official BPX download page now documents 1.1 additions including SPMe, one-state hysteresis, composite electrodes, LAM/LLI state and a separate cell-state description. The public change notes do not establish compatibility of the captured legacy files with a current parser. The full specification download requires contact details; that form was not submitted. [S01, S06]

Do not change the header to a newer version without a semantic migration. No BPX 1.1 conformance result is provided. The four repository schemas are research-data schemas, not reimplementations of the official BPX schema.

## Migration review table
| Legacy object | Review required |
|---|---|
| `Header.BPX` | Preserve original version; record target schema and migration tool version separately |
| Cell/initial/ambient temperatures | Separate intrinsic parameter references from experiment/initial state |
| Electrode area and parallel pairs | Confirm area/layer normalization; do not map to pack Ns/Np |
| Rate constants | Reconcile molar rate, Faraday factor and concentration normalization with the target equation |
| OCP expressions/tables | Confirm variable definitions, stoichiometric domain and interpolation rules |
| Entropy and thermal values | Preserve literature/estimate provenance; no upgrade to “measured” |
| Validation currents | Retain negative-discharge source convention and documented normalization |
| Aging state | Distinguish state descriptors from kinetics governing their future evolution |

## Version ledger
Record source URL, source blob or release/DOI, source license, acquisition method, exact local hash, parser version, transformation script revision and known semantic changes. The About:Energy tree SHA is recorded as a tree SHA; no commit identity was fabricated. The downloader pins individual blob identities instead of trusting a mutable branch name.

PyBaMM's retrieved `latest` pages identify a development build and warn that notebooks may differ from stable releases. This package does not pin an unverified stable solver or install PyBaMM. During implementation, select an actual tested release and archive its parameter/schema compatibility report.

The first migration test should compare numeric values, expression behavior, initial state, voltage/capacity scaling and current signs on source reference protocols. Merely passing JSON parsing is insufficient. Preserve both original and migrated artifacts so that every changed field is reviewable.

## Source basis

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S02: PyBaMM DFN equations](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/DFN.html)
- [S05: PyBaMM parameterisation](https://docs.pybamm.org/en/latest/source/examples/notebooks/parameterization/parameterization.html)
- [S06: BPX official standard download and change notes](https://bpxstandard.com/bpx-standard/)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.
