# Source-specific ingestion recipes

[한국어](../ko/16_INGESTION_RECIPES.md) · [README](../../README.md)

## Included, executed offline
From the repository root, `python scripts/export_curated.py` reads the two captured BPX files, exports their parameters and embedded reference records, safely samples OCP functions and converts the EPA schedule to m/s. It does not integrate battery dynamics. `python scripts/fetch_sources.py` is a dry run; `python scripts/compare_originals.py` currently reports that original files are missing.

The download sequence for a network-enabled environment is:

```bash
python scripts/fetch_sources.py
python scripts/fetch_sources.py --execute --acknowledge-cc-by-sa
python scripts/compare_originals.py
```

Read source license conditions before the second command. A live download result belongs in its own dated report; do not rewrite the preparation audit to make past acquisition appear successful.

## Other source families: adapter specifications, not implemented collectors
**NASA MAT files.** Preserve the outer cycle type, ambient temperature and start time. Extract measured voltage/current/temperature, charge/discharge instrument channels, relative time and capacity. EIS arrays require frequency/channel interpretation from the original documentation. MATLAB v7.3/HDF5 is different from earlier MAT encoding; choose the parser after inspecting the file header. Do not mistake a MATLAB date vector for elapsed seconds. [S08, S09]

**CALCE and HG2 exports.** Inspect every file's unit and sign labels, temperature/protocol naming, instrument range and reset behavior. Normalize steps separately. Confirm whether capacity is cumulative, per-step, per-cycle or already processed. Unknown source columns must not be dropped silently. Raw file payloads were not inspected here. [S07, S10]

**MATR.** Keep descriptor, summary and cycle-level records linked by original cell ID. Derived `Qdlin`, `Tdlin` and dQ/dV are not raw measurements. Do not unpickle untrusted files: prefer original non-executable numeric formats or an isolated, reviewed conversion path. Modeling-code access has separate academic-license requirements. [S25]

**CT and failure spreadsheets.** Inspect license/readme, coordinate units, phase labels, specimen IDs, trigger/fixture metadata and missing-value conventions before extraction. Gray images, segmented volumes and generated phases are distinct. The referenced XLSX was not opened/parsed, so no claim about its exact sheet-level schema is made. [S13-S16]

Each future adapter should have a tiny licensed fixture, a unit/sign test, an original-to-normalized row-count reconciliation and a documented exclusion policy before processing a whole collection.

## Source basis

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S07: CALCE battery data](https://calce.umd.edu/battery-data)
- [S08: NASA Li-ion aging catalog](https://data.nasa.gov/dataset/li-ion-battery-aging-datasets)
- [S09: NASA PCoE data repository](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/)
- [S10: LG HG2 dataset v3](https://data.mendeley.com/datasets/cp3473x7xv/3)
- [S13: Mechanically induced thermal runaway v2](https://data.mendeley.com/datasets/sn2kv34r4h/2)
- [S14: Battery Failure Databank](https://www.nlr.gov/transportation/battery-failure)
- [S15: Battery Microstructures Library](https://www.nlr.gov/transportation/microstructure)
- [S25: Severson/Attia original data-processing repository](https://github.com/rdbraatz/data-driven-prediction-of-battery-cycle-life-before-capacity-degradation)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.
