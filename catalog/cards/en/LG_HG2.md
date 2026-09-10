# McMaster LG18650HG2 dataset v3

[한국어](../ko/LG_HG2.md) | [Catalog](../../resources.json)

**ID:** `LG_HG2` · **Priority:** P1 · **Kind:** experimental_dataset

## Evidence and scope
Fresh 3 Ah LG HG2; instrument accuracy 0.1% full scale; v3 2020-03-05

## Recommended use
External electrical/SOC-estimator benchmark with temperature and dynamic protocols once individual files are inspected.

## Invalid inference to avoid
Do not treat SOC labels or neural network output as direct electrochemical ground truth; do not transfer fitted parameters to another cell.

## Acquisition and reuse
Status: `metadata_only`. Rights: `CC-BY-4.0`. Raw byte download completed: **No**.

Use official Mendeley file manifest/export. Record each test temperature, cell ID, sign convention, full-scale ranges and files before normalization.

A source listing is not an assertion that its payload was downloaded. For included semantic captures, preserve the separate capture provenance and do not claim byte identity.

## Sources
- [S10: LG HG2 dataset v3](https://data.mendeley.com/datasets/cp3473x7xv/3)

Checked: 2026-09-10. Ranking is an engineering judgment, not a measured quality score.
