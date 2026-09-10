# PyBaMM parameter and model documentation

[한국어](../ko/PYBAMM_PARAMETERS.md) | [Catalog](../../resources.json)

**ID:** `PYBAMM_PARAMETERS` · **Priority:** P0 · **Kind:** software_reference_resource

## Evidence and scope
DFN, thermal, degradation and parameterization references; latest pages identify a development build

## Recommended use
Define model equations and parameter meanings; later choose one stable pinned implementation and associated cell parameter set.

## Invalid inference to avoid
A library default is not a measured property of the selected target cell. Do not claim current stable compatibility based on latest docs.

## Acquisition and reuse
Status: `metadata_only`. Rights: `reference_only;upstream_licenses_apply`. Raw byte download completed: **No**.

Pin a stable release during implementation and verify parameter source lineage; old Chen2020 source path returned 404 after repository restructuring.

A source listing is not an assertion that its payload was downloaded. For included semantic captures, preserve the separate capture provenance and do not claim byte identity.

## Sources
- [S02: PyBaMM DFN equations](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/DFN.html)
- [S03: PyBaMM thermal models](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/thermal-models.html)
- [S04: PyBaMM coupled degradation](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/coupled-degradation.html)
- [S05: PyBaMM parameterisation](https://docs.pybamm.org/en/latest/source/examples/notebooks/parameterization/parameterization.html)

Checked: 2026-09-10. Ranking is an engineering judgment, not a measured quality score.
