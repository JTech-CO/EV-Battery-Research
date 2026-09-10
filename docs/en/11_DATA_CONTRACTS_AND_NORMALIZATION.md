# Data contracts and normalization

[한국어](../ko/11_DATA_CONTRACTS_AND_NORMALIZATION.md) · [README](../../README.md)

## Keep three layers
`data/curated` holds captured source content with unchanged scientific meaning where possible, but explicitly altered serialization. `data/raw` is reserved for future verified original bytes and is ignored by Git. `data/derived` holds normalized records and sampled fits with transformation provenance. Never overwrite a source capture during cleaning.

Schemas describe cell identity, parameter evidence, normalized reference-curve records and generic quantity evidence. JSON Schema checks structure, not scientific truth or BPX conformance. Unknown specimen IDs, uncertainty and measured temperatures remain null. Dataset-local logical IDs are not verified manufacturer serial numbers.

## Canonical conventions
| Quantity | Canonical convention | Preserve also |
|---|---|---|
| Time | Seconds, monotonic within a segment | Original timestamp, segment/reset history |
| Current | Positive discharge | Raw current and explicit source convention |
| Temperature | Kelvin | Original Celsius/setpoint/sensor meaning |
| Capacity | Ah with reference protocol | Coulombs if used, cutoff/rate/temp definition |
| Potential | Full-cell V or explicit V vs Li/Li+ | Electrode/reference identity |
| EIS | Real and imaginary ohms plus Hz | Original sign and excitation/rest details |
| Speed | m/s | Source mph and prescribed/measured status |

Conversions used here are $T_K=T_C+273.15$, $1\,Ah=3600\,C$ and $1\,mph=0.44704\,m/s$. About:Energy embedded discharge currents are negative; normalization negates them while retaining the raw values. Do not infer a source's current convention solely from the majority sign in a file.

## Processing rules
Reject nonfinite numbers and unequal curve-column lengths. Check time order per segment; a cycle reset is not necessarily corrupt data. Preserve duplicates and their resolution policy before resampling. Do not interpolate across charge/rest/discharge discontinuities, missing blocks or end-of-test boundaries. Interpolation cannot create a new independent observation or justify a higher effective sampling rate.

Source OCP expressions are parsed with a small AST whitelist, not Python `eval`. The supplied script samples only the source electrode stoichiometric windows. It does not extrapolate electrolyte fits over an invented concentration range. A function may still be scientifically unsuitable inside a syntactic domain; domain checks are not model validation.

The included CSVs are UTF-8 with ASCII machine keys. English/Korean descriptions live in the catalogs and documents. Physical units are encoded in column names or dedicated fields; localized display formatting must never alter stored numeric values.

## Source basis

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S05: PyBaMM parameterisation](https://docs.pybamm.org/en/latest/source/examples/notebooks/parameterization/parameterization.html)
- [S07: CALCE battery data](https://calce.umd.edu/battery-data)
- [S08: NASA Li-ion aging catalog](https://data.nasa.gov/dataset/li-ion-battery-aging-datasets)
- [S17: EPA dynamometer schedules](https://www.epa.gov/vehicle-and-fuel-emissions-testing/dynamometer-drive-schedules)
- [S18: EPA US06 numeric schedule](https://www.epa.gov/system/files/other-files/2025-03/us06col.txt)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.
