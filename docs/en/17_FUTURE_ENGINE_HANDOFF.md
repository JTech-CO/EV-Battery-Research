# Handoff to a future scientific-engine project

[한국어](../ko/17_FUTURE_ENGINE_HANDOFF.md) · [README](../../README.md)

## Scope boundary
This repository is a research/data-preparation asset. It contains no interactive battery model, physics time-stepper, solver integration, trained predictor, web application or deployment pipeline. The transformation scripts do not imply approval to begin simulator development.

A later engineering brief should specify target chemistry/cell identity, observable outputs, operating envelope, acceptable errors, experimental holdouts, compute/runtime budget and what claims the interface may make. Keep a scientific kernel independently testable from rendering and UI.

## Proposed input/output contract
An experiment description should reference a versioned cell parameter set, initial state, current/power/voltage-control protocol, thermal boundaries, stop conditions and requested observables. Do not allow mutually inconsistent input controls without an explicit controller model. The output should retain time, terminal quantities, state provenance, conservation residuals, domain violations, solver settings and uncertainty metadata.

Each field should state whether it is measured input, specified boundary, fitted parameter, estimated prior or predicted state. Visual particle/ion animations must be labeled schematic unless they truly correspond to resolved physical states. Interpolated or model-generated points cannot be presented as laboratory measurements.

## Implementation acceptance gates
Require source/capture reconciliation before automatic parameter import; enforce units/signs; prohibit unsafe expression evaluation; keep fitted priors identifiable; freeze calibration and test partitions; add numerical-convergence and conservation tests; report failed conditions. Only then compare kernel predictions to independent reference data.

The later UI may offer different model levels, but it must not silently change chemistry, phase behavior, thermal assumptions or aging definitions when switching levels. A visually continuous transition is not a physically equivalent model conversion.

## What to hand to a coding agent
Provide this report, source registry, parameter requirement inventory, acquisition/rights ledger, schemas, exact captured datasets and QA results. The first coding-agent assignment should be to validate ingestion against newly acquired originals, not to fill missing science with plausible constants. Unmeasured values remain explicit priors or unresolved requirements.

No repository on the user's account was created or modified. The delivered ZIP is a local, reviewable research snapshot ready for a deliberate publication decision with its mixed-license notices intact.

## Source basis

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S02: PyBaMM DFN equations](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/DFN.html)
- [S05: PyBaMM parameterisation](https://docs.pybamm.org/en/latest/source/examples/notebooks/parameterization/parameterization.html)
- [S06: BPX official standard download and change notes](https://bpxstandard.com/bpx-standard/)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.
