# Aging mechanisms and identifiability

[한국어](../ko/06_DEGRADATION_AND_IDENTIFIABILITY.md) · [README](../../README.md)

## Capacity loss is an observable, not a unique mechanism
Distinguish loss of cyclable lithium inventory (LLI), loss of active material (LAM), SEI growth, lithium plating/stripping and dead lithium, particle cracking, electrolyte depletion, contact degradation and gas-related swelling. Coupling changes the bookkeeping: cracks may create new SEI area; a plated-lithium pathway may also reduce cyclable inventory. Adding separate capacity-loss terms without inventory accounting can double-count the same lithium. [S04]

| Mechanism/state | Needed evidence | Weak evidence alone |
|---|---|---|
| LLI/electrode balance | Matched OCP/DVA analysis and supporting diagnostics | Total capacity loss |
| LAM | Electrode capacity/structural or electrochemical diagnostics | Resistance increase alone |
| SEI | Film/transport evidence, aging matrix, temperature/potential dependence | An arbitrary square-root-time fit |
| Plating/dead lithium | Mechanism-sensitive measurements and charge history | A voltage anomaly alone |
| Cracking/swelling | Mechanical fixture data and structural diagnostics | Unqualified cell-thickness change |

The first aging model should be the smallest identifiable model consistent with available observables. A semiempirical law may be an honest bounded predictor when a more detailed mechanism network is underdetermined. Label that choice rather than describing fitted coefficients as directly measured material properties.

## Experimental design
Keep calendar time, throughput, number of cycles, rest periods, mean SOC, DOD, rates and temperature histories. For one declared convention, equivalent full cycles may be discharge Ah divided by reference capacity; with absolute charge-plus-discharge throughput the denominator is twice that capacity. Do not mix the two definitions. Every capacity/resistance comparison requires a matched reference-performance test.

NASA, Sandia/Archive, CALCE, Oxford, ILCC and MATR provide different history/observable combinations; none should be merged blindly into a universal EV aging curve. Matched cell identity, protocol, censoring and uncertainty are more important than raw row count. [S07-S12, S23, S25]

## Leakage and uncertainty
Split entire cells, batches and source studies before fitting. A cell's late-life traces must not inform an early-life predictor. Derived features such as interpolated capacity and dQ/dV must retain their processing lineage. Mirrors and repackaged datasets must be de-duplicated by original study/specimen identifiers.

Report parameter/posterior correlations, uncertainty in unobserved states and model-form alternatives. A small voltage residual cannot alone validate SEI thickness or plated-lithium mass. Do not infer a universal mechanism from whichever term an optimizer happened to adjust.

## Source basis

- [S04: PyBaMM coupled degradation](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/coupled-degradation.html)
- [S07: CALCE battery data](https://calce.umd.edu/battery-data)
- [S08: NASA Li-ion aging catalog](https://data.nasa.gov/dataset/li-ion-battery-aging-datasets)
- [S09: NASA PCoE data repository](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/)
- [S11: Battery Archive study summaries](https://batteryarchive.org/study_summaries.html)
- [S23: Iowa State ILCC dataset landing](https://doi.org/10.25380/iastate.22582234)
- [S25: Severson/Attia original data-processing repository](https://github.com/rdbraatz/data-driven-prediction-of-battery-cycle-life-before-capacity-degradation)
- [S28: PyBOP paper](https://arxiv.org/abs/2412.15859)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.
