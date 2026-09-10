# Audit of the captured numeric data

[한국어](../ko/14_CAPTURED_DATA_AUDIT.md) · [README](../../README.md)

## Acquisition inventory
| Artifact | Contents | Evidence status |
|---|---|---|
| LFP BPX capture | 2 Ah graphite/LFP 18650, legacy BPX 0.1 | Source text transcribed/reserialized; original bytes not acquired |
| NMC BPX capture | 12.5 Ah graphite/NMC111 pouch, BPX 0.1 | Same capture method; includes source reference curves |
| Parameter export | 104 entries across both parameterizations | Includes conditions, fits and estimates; not 104 independent measurements |
| NMC curve export | 76 C/20 points and 38 1C points | Embedded source reference data, not full raw cycler CSVs |
| OCP samples | 101 samples per electrode, 404 total | Evaluated published functions within source stoichiometric windows |
| US06 schedule | 601 points from 0 to 600 s | Prescribed speed input; transcribed from EPA text |

Both parameter sets have a reference temperature of 298.15 K. The LFP voltage limits are 2.0/3.65 V and the NMC limits are 2.7/4.2 V **within these source examples**, not universal operating limits. LFP's nominal 2 Ah and the pouch's 12.5 Ah are source nominal capacities. Thermal values are partly estimated and entropy inputs are literature-derived. [S01]

## Deterministic checks and integrals
For the captured 1C NMC interval, constant discharge current 12.5 A over 3700 s integrates to approximately **12.8472 Ah**. For C/20, 0.625 A over 75000 s gives **13.0208 Ah**. These are interval integrals, not a remeasurement or certification of cell capacity. They need not equal the nominal 12.5 Ah label. The retained terminal voltages are approximately 2.9047 V and 2.8947 V, above the BPX lower cutoff. Do not extend the records to 2.7 V by invented observations.

Trapezoidal integration of the captured voltage/current samples gives about 46.2534 Wh and 48.3844 Wh over those intervals. This uses linear interpolation between retained samples and does not reconstruct unretained high-frequency behavior. The detailed values/assumptions are in `reports/numeric_audit.json`.

The transcribed US06 maximum is 80.3 mph. Trapezoidal integration of its prescribed speed gives about 12,887.582 m over 600 s. This is a derived schedule distance, **not EV range**, measured trip distance or battery energy demand. [S18]

## Unresolved checks
Original-byte downloads and full original-versus-capture semantic comparison have not succeeded. Checksums in this package prove only local release integrity. The two arrays' constant 298.15 K is not accepted as a measured thermal response. The LFP full validation CSVs and both cells' drive-cycle CSVs remain indexed but uncollected. No accuracy claim follows from these arithmetic checks.

## Source basis

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S18: EPA US06 numeric schedule](https://www.epa.gov/system/files/other-files/2025-03/us06col.txt)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.
