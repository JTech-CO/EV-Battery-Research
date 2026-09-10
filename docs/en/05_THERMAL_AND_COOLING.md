# Thermal behavior and cooling boundaries

[한국어](../ko/05_THERMAL_AND_COOLING.md) · [README](../../README.md)

## Separate heat generation from heat removal
For a spatial thermal domain, the working balance is

$$\rho c_p\partial_tT=\nabla\cdot(\mathbf{k}\nabla T)+q_{gen},$$

with explicitly defined contacts, convection, radiation and coolant boundaries. A lumped model replaces spatial temperature with a representative state; it cannot independently predict a core-to-surface gradient that it does not resolve. Obtain anisotropic conductivity, heat capacity, density, sensor placement and cooling geometry. [S03]

A convenient whole-cell diagnostic under discharge-positive current, near-equilibrium thermodynamic assumptions and a consistent OCV definition is

$$\dot Q_{irr}=I(U_{OCV}-V),\qquad \dot Q_{rev}=-IT\frac{\partial U_{OCV}}{\partial T}.$$

This is not a substitute for all nonequilibrium mixing and side-reaction terms in a detailed model. If using distributed ohmic/reaction/entropy heat terms, do not add the same whole-cell loss again. Tab/busbar resistance included in terminal loss must be allocated to its actual thermal domain. Always verify the current and reaction sign conventions before using an entropy term.

## Thermal dataset contract
Record sensor coordinates and attachment, surface versus core versus chamber temperature, sample rate, calibration/lag, current/voltage synchronization, coolant inlet/outlet temperatures, mass flow, contact pressure and calorimeter boundaries. A flat chamber setpoint is not a measured cell-temperature trace. Fit heat transfer and heat capacity using informative experiments rather than a single curve in which they compensate.

The captured BPX files explicitly describe other thermal properties as estimates. Their entropy inputs come from literature. The embedded NMC temperature array is identically 298.15 K; the source excerpt does not establish it as a core or surface sensor measurement. The normalized file therefore stores it as `reference_temperature_K` and leaves surface/core temperature null. [S01]

## Failure heat is a different regime
NLR's failure databank reports body/ejecta heat and mass during triggered thermal runaway. It is useful for conditional failure-energy and variability bounds, not calibration of ordinary reversible/irreversible cycling heat or a universal reaction-kinetics model. The listed spreadsheet revision is February 2024, regardless of later webpage maintenance dates. [S14]

For the next collection round, prioritize matched-cell normal-cycle calorimetry and independent thermal relaxation data before adding a sophisticated cooling visualization. No thermal accuracy has been demonstrated by this package.

## Source basis

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S03: PyBaMM thermal models](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/thermal-models.html)
- [S14: Battery Failure Databank](https://www.nlr.gov/transportation/battery-failure)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.
