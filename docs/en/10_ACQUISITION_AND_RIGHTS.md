# Acquisition, crawling boundaries and reuse

[한국어](../ko/10_ACQUISITION_AND_RIGHTS.md) · [README](../../README.md)

## What was done
Public primary pages were searched/read, source metadata was recorded, and GitHub's connected read API supplied the About:Energy parameter text and file-tree/blob identifiers. Two BPX JSONs were manually transcribed/reserialized; EPA's parsed plain-text US06 rows were transcribed into CSV. Direct byte-download attempts did not succeed. No full aging/CT/spreadsheet archive was downloaded. See `metadata/retrieval_audit.json`.

Use **semantic capture** for the included files, not “raw download.” Local SHA-256 checks file integrity after capture; it cannot prove that a transcription equals an unacquired upstream file. The downloader records immutable Git blob SHA-1 separately from local SHA-256, byte size and future retrieval time. A Git tree SHA is not a commit SHA.

## Rights matrix
| Source | Verified or unresolved condition | Repository treatment |
|---|---|---|
| About:Energy | CC BY-SA 4.0 license heading verified | Attribution and share-alike retained for captures and adaptations |
| LG HG2 / mechanical runaway Mendeley v2 | CC BY 4.0 on dataset pages | Metadata only here; preserve attribution after later download |
| NASA aging | Catalog says license not specified | No blanket public-domain assumption; raw data excluded |
| CALCE / Battery Archive | Attribution / study-specific permission | Review chosen files; requests not submitted |
| NLR microstructure | Custom agreement | User review/acceptance required; no volumes included |
| NLR failure spreadsheet | File-level terms/readme not verified | No spreadsheet included |
| EPA | Scientific/educational use described; commercial use not blanket-cleared | Research schedule capture with separate notice; commercial review required |
| BPX specification | Public notes; contact-details download form | No form submitted; no specification PDF bundled |

The repository's original-code license does not relicense any third-party data. Do not delete source attribution or relabel CC BY-SA adaptations as MIT. Metadata availability and download availability do not establish redistribution permission. This is an operational rights audit, not a jurisdiction-specific legal opinion. [S01, S06-S19]

## Reproducible collection
The included collector is **allowlisted**, not a general web spider. Its default is a dry run. With explicit execution/license acknowledgement it requests only 16 verified About:Energy Git blobs, checks expected size and Git object hash, stores local SHA-256 and writes an acquisition report. It refuses changed repository/rights/URL/path assumptions, uses limited retries and avoids cross-host redirects. Its successful live network path was not demonstrated here.

For larger collections, use official APIs/exports and manually accepted agreements. Record version/DOI, server checksum if available, source terms, file list and a dated receipt. Keep download logs free of API keys and personal contact data. Do not scrape hidden endpoints, bypass authentication/CAPTCHA or silently accept terms on behalf of a user.

## Source basis

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S06: BPX official standard download and change notes](https://bpxstandard.com/bpx-standard/)
- [S07: CALCE battery data](https://calce.umd.edu/battery-data)
- [S08: NASA Li-ion aging catalog](https://data.nasa.gov/dataset/li-ion-battery-aging-datasets)
- [S10: LG HG2 dataset v3](https://data.mendeley.com/datasets/cp3473x7xv/3)
- [S12: Battery Archive access page](https://www.batteryarchive.org/)
- [S13: Mechanically induced thermal runaway v2](https://data.mendeley.com/datasets/sn2kv34r4h/2)
- [S14: Battery Failure Databank](https://www.nlr.gov/transportation/battery-failure)
- [S16: Microstructure library agreement](https://www.nlr.gov/transportation/microstructure-library-disclaimer)
- [S19: EPA disclaimers and copyright status](https://www.epa.gov/web-policies-and-procedures/epa-disclaimers)
- [S25: Severson/Attia original data-processing repository](https://github.com/rdbraatz/data-driven-prediction-of-battery-cycle-life-before-capacity-degradation)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.
