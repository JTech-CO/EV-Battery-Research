# EV Battery Research

[한국어](README-KR.md) · [Complete English report](RESEARCH_REPORT.md) · [Complete Korean report](RESEARCH_REPORT-KR.md)

**Public-data research and evidence preparation for a future realistic EV battery simulator. No simulator or web application is included.**

Research snapshot: **2026-09-10** · Release: **1.0.0** · Mixed licenses: see [third-party notices](THIRD_PARTY_NOTICES.md).

## Start here
The recommended scientific starting point is one coherent cell parameter set with matching observations, not a mixture of unrelated chemistry/thermal/aging numbers. Read the [research summary](docs/en/00_RESEARCH_SUMMARY.md), [dataset strategy](docs/en/09_DATASET_SELECTION.md) and [captured-data audit](docs/en/14_CAPTURED_DATA_AUDIT.md).

## Actual contents
| Item | Included quantity | What it is not |
|---|---:|---|
| Research chapters | 20 English + 20 Korean | An implemented scientific engine |
| Resource cards | 23 in each language | 23 fully downloaded experimental datasets |
| Source records | 28 | A guarantee every primary payload was accessible |
| Data requirements | 139 bilingual fields | 139 collected target-cell measurements |
| BPX semantic captures | 2 legacy 0.1 files; 104 parameter entries | Byte-identical verified originals or all-measured parameters |
| NMC source reference curves | 114 points | Independent held-out validation or full raw cycler data |
| EPA US06 | 601 prescribed speed points | A measured battery-current trace |
| OCP fit tables | 404 derived points | New experimental observations |
| Acquisition manifest | 16 pinned blobs, 1,740,269 expected bytes | Raw files already downloaded here |
| Data schemas | 4 JSON Schema documents | Official BPX conformance validation |

Direct byte downloads failed in the preparation environment. The two BPX JSONs and the speed CSV are **manual semantic captures from source text**, with separate provenance. Full cycling/aging archives, original validation CSVs, CT volumes and failure spreadsheets remain uncollected. This is a research starter corpus, not a complete public-data mirror or an OEM digital twin.

## Layout
```text
README.md / README-KR.md           Entry points
RESEARCH_REPORT.md / -KR.md        Combined reading copies
docs/en/ and docs/ko/              Detailed research chapters
catalog/                          Resource cards and 139-field requirements
data/curated/                      Attributed source-content captures
data/derived/                      Normalized records and published-fit tables
metadata/                         Sources, rights, acquisition and checksums
schemas/                          Research data contracts
scripts/ and tests/                Data preparation and offline QA only
reports/                          Executed QA and arithmetic audit results
```

## Run local data QA
Python 3.10+ is required. Data transforms and unit tests use the standard library; full JSON Schema validation uses `jsonschema`.

```bash
python -m pip install -r requirements.txt
python scripts/validate_package.py --verify-checksums
python scripts/export_curated.py
python scripts/audit_numeric.py
python -m unittest discover -s tests -v
python scripts/validate_package.py
```

The release was checked with Python 3.13.5 and jsonschema 4.26.0. Local QA is not a model-accuracy test. [QA report](reports/QA_REPORT.md) · [machine-readable validation](reports/package_validation.json).

## Retrieve the indexed originals later
```bash
python scripts/fetch_sources.py
# After reviewing the source license, in a network-enabled environment:
python scripts/fetch_sources.py --execute --acknowledge-cc-by-sa
python scripts/compare_originals.py
```

The first command makes no network request. The successful live downloader path was not demonstrated here. Other portals require the source-specific steps in the cards; no generic scraper or agreement bypass is supplied. New verified originals go under Git-ignored `data/raw/`.

## Research documents
| No. | Chapter |
|---|---|
| 00 | [Research summary and decision](docs/en/00_RESEARCH_SUMMARY.md) |
| 01 | [Operating physics and chemistry](docs/en/01_PHYSICS_AND_CHEMISTRY.md) |
| 02 | [Cell structure and material identity](docs/en/02_CELL_STRUCTURE_AND_MATERIALS.md) |
| 03 | [Model hierarchy and evidence requirements](docs/en/03_MODEL_HIERARCHY.md) |
| 04 | [Electrochemical characterization and parameter use](docs/en/04_ELECTROCHEMICAL_DATA.md) |
| 05 | [Thermal behavior and cooling boundaries](docs/en/05_THERMAL_AND_COOLING.md) |
| 06 | [Aging mechanisms and identifiability](docs/en/06_DEGRADATION_AND_IDENTIFIABILITY.md) |
| 07 | [Mechanics, microstructure and failure](docs/en/07_MECHANICS_MICROSTRUCTURE_AND_FAILURE.md) |
| 08 | [Pack, BMS and vehicle boundaries](docs/en/08_PACK_BMS_AND_VEHICLE.md) |
| 09 | [Dataset selection and matching strategy](docs/en/09_DATASET_SELECTION.md) |
| 10 | [Acquisition, crawling boundaries and reuse](docs/en/10_ACQUISITION_AND_RIGHTS.md) |
| 11 | [Data contracts and normalization](docs/en/11_DATA_CONTRACTS_AND_NORMALIZATION.md) |
| 12 | [Validation and uncertainty plan](docs/en/12_VALIDATION_AND_UNCERTAINTY.md) |
| 13 | [Gap analysis and research gates](docs/en/13_GAPS_AND_RESEARCH_ROADMAP.md) |
| 14 | [Audit of the captured numeric data](docs/en/14_CAPTURED_DATA_AUDIT.md) |
| 15 | [BPX semantics and version control](docs/en/15_BPX_AND_VERSIONING.md) |
| 16 | [Source-specific ingestion recipes](docs/en/16_INGESTION_RECIPES.md) |
| 17 | [Handoff to a future scientific-engine project](docs/en/17_FUTURE_ENGINE_HANDOFF.md) |
| 18 | [Sources and access audit](docs/en/18_SOURCES_AND_ACCESS_AUDIT.md) |
| 19 | [Technical glossary](docs/en/19_GLOSSARY.md) |

## Licensing and publication
Original scripts/tests are MIT; original research prose is CC BY 4.0. About:Energy captures and adaptations remain **CC BY-SA 4.0**. EPA scientific/educational use has a separate notice and **commercial reuse is not blanket-cleared**. Do not label the whole repository MIT or remove data attribution. Review [LICENSE](LICENSE) and the [file-scope licensing map](metadata/license_map.json) before publishing.

This package did not create, modify or publish a GitHub repository. No source provider endorses this package. Cite the original dataset providers and papers as well as any use of this research snapshot.
