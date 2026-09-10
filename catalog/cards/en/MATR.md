# MATR / Severson-Attia cycle-life data

[한국어](../ko/MATR.md) | [Catalog](../../resources.json)

**ID:** `MATR` · **Priority:** P1 · **Kind:** experimental_dataset

## Evidence and scope
MAT structs / Python dictionaries; per-cell descriptors, per-cycle summaries and cycle traces

## Recommended use
Evaluate early-cycle predictors with cell/batch holdouts. Keep measured capacity separate from interpolated Qdlin and derived dQ/dV.

## Invalid inference to avoid
Academic modeling-code access is not an automatic data license. Never split adjacent cycles of one cell into train and test.

## Acquisition and reuse
Status: `metadata_only`. Rights: `data_license_not_reverified`. Raw byte download completed: **No**.

MATR page yielded only a JavaScript shell. Obtain official data export and license, avoid untrusted pickle loading.

A source listing is not an assertion that its payload was downloaded. For included semantic captures, preserve the separate capture provenance and do not claim byte identity.

## Sources
- [S25: Severson/Attia original data-processing repository](https://github.com/rdbraatz/data-driven-prediction-of-battery-cycle-life-before-capacity-degradation)
- [S26: MATR Experimental Data Platform](https://data.matr.io/1/)

Checked: 2026-09-10. Ranking is an engineering judgment, not a measured quality score.
