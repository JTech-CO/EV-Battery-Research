# Release QA report

[한국어](QA_REPORT-KR.md) · [README](../README.md)

Snapshot: **2026-09-10**. This report concerns the data-preparation package, not a simulator.

## Executed checks
The delivered package was checked using Python 3.13.5 and jsonschema 4.26.0. The offline unit suite contains **26 tests** covering explicit current conventions, temperature bounds, restricted mathematical expression evaluation, path traversal rejection, Git blob hashing, payload-tamper rejection, allowlisted source URLs, and the retained-data counts and provenance constraints. The actual console output is preserved in [unit_tests.txt](unit_tests.txt).

The [package validator](../scripts/validate_package.py) checks unique source/resource/requirement identifiers, resolvable source references, English/Korean chapter and card counterparts, local Markdown links, legacy-data semantics and unit conversions. Four JSON Schema definitions are checked for structural validity; the three applicable schemas are applied to the included cell, parameter and normalized reference-curve records. It does **not** certify a BPX file against the current official BPX standard. See [package_validation.json](package_validation.json) for the executed result.

The [numeric audit](numeric_audit.json) computes trapezoidal integrals only over the captured intervals. Those integrals are not certified full-test capacity, energy, or vehicle range. The two NMC source arrays end above their nominal lower voltage cutoff; no tail was invented or extrapolated.

The exports and numeric audit were executed twice in the tested environment; all generated data and arithmetic-report file hashes were unchanged. Floating-point fit tables are not promised to be byte-identical across all Python versions or operating systems. Verify the delivered checksums before regenerating data.

## Acquisition and provenance limitations
The [downloader report](downloader_dry_run.json) is a **dry run**, not a successful network acquisition. It indexes 16 immutable About:Energy Git blobs. The [original comparison](original_comparison.json) remains `not_checked_raw_file_missing` for both BPX captures. Raw-file-versus-capture semantic identity, byte identity, source transcription completeness, and a live downloader success path are **not validated**.

Captured and derived files carry their source identity and evidence type. Constant 298.15 K source values remain a reference temperature; measured surface/core temperature remains null. Requirements are not relabeled as measured target-cell values. Published-fit samples remain derived samples.

## Local release integrity
[SHA256SUMS.json](../metadata/SHA256SUMS.json) fingerprints the local release files, not the upstream originals. It excludes itself, raw acquisitions, Git internals and Python caches. Verify with `python scripts/validate_package.py --verify-checksums`. Recreate the manifest only after deliberate review of changes; regenerating it is not a way to resolve unexplained mismatches.

The checked-in package validation report is written before this checksum manifest, so its `checksum_verification` field is `not_requested`. A subsequent checksum verification is intentionally not written back to a hashed file. This avoids a self-invalidating checksum/report cycle.

## Not demonstrated
No cell/pack solver, parameter calibration, thermal/aging/failure prediction, independent holdout result, runtime benchmark or OEM digital-twin fidelity was tested. Software/data QA is not scientific model validation. No GitHub repository was modified, and no portal agreement or access form was submitted.
