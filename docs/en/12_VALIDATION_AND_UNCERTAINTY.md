# Validation and uncertainty plan

[한국어](../ko/12_VALIDATION_AND_UNCERTAINTY.md) · [README](../../README.md)

## Evidence levels
Separate data QA, numerical verification, calibration, source-benchmark reproduction, independent validation and deployment qualification. This repository performs only local data/package QA and deterministic transformations. It provides no solver result, fitted model accuracy, safety certification or vehicle deployment qualification.

The source-provided NMC curves may overlap original parameter-development data; their statistical independence is not established. They are therefore labeled **source reference curves**, not a pristine held-out test set. After reproducing them, reserve different protocols, cells/batches and temperature conditions for independent testing.

## Proposed test ladder
1. Validate units, signs, identities, schemas, input completeness and data lineage.
2. In a later solver, check initial consistency, lithium/charge/energy bookkeeping, limits and mesh/time/tolerance convergence.
3. Reproduce source curves without tuning arbitrary unrelated coefficients.
4. Evaluate held-out current profiles, SOC windows and temperatures with a frozen parameter set.
5. Add aging/mechanical/pack tests only when the corresponding observables and boundary conditions exist.

## Draft engineering targets, not achieved results
| Observable | Example starting target for a declared envelope | Necessary qualification |
|---|---|---|
| Cell voltage | RMSE 20 mV or less | Report max error, bias, SOC/rate/temp slices and sensor uncertainty |
| Reference discharge capacity | Relative error 2% or less | Same current, temperature, cutoffs and reference definition |
| Measured surface temperature | RMSE 2 K or less | Real sensor trace and boundary conditions; not a chamber setpoint |
| Aging prediction | Predeclare error/coverage at held-out checkpoints | Cell-level resampling, censoring and horizon defined |
| Pack behavior | Predeclare cell-limit and branch-current error | Full topology, controls and sensor mapping required |

These numbers are suggested starting acceptance budgets for discussion, not standards, published performance claims or guarantees. They must be revised against the intended operating envelope and instrument uncertainties. This package has not met or tested them.

## Uncertainty report
Distinguish measurement error, parameter uncertainty, manufacturing variance, interpolation/processing error, model discrepancy and out-of-domain use. Use parameter covariance/posterior ensembles when justified; report joint rather than independent uncertainties for correlated parameters. Bootstrap cells rather than individual adjacent samples to avoid inflated effective sample size.

Report failed conditions and residual structure, not only a global average. A physically plausible terminal curve does not validate invisible internal concentration, plating or SEI states. The user-facing simulator should eventually expose validity and confidence status rather than silently extrapolate beyond the evidence.

## Source basis

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S05: PyBaMM parameterisation](https://docs.pybamm.org/en/latest/source/examples/notebooks/parameterization/parameterization.html)
- [S07: CALCE battery data](https://calce.umd.edu/battery-data)
- [S10: LG HG2 dataset v3](https://data.mendeley.com/datasets/cp3473x7xv/3)
- [S25: Severson/Attia original data-processing repository](https://github.com/rdbraatz/data-driven-prediction-of-battery-cycle-life-before-capacity-degradation)
- [S28: PyBOP paper](https://arxiv.org/abs/2412.15859)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.
