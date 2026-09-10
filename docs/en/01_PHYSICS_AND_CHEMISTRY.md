# Operating physics and chemistry

[한국어](../ko/01_PHYSICS_AND_CHEMISTRY.md) · [README](../../README.md)

## Lithium and charge pathways
During discharge, lithium leaves the negative active material as ions while electrons enter the external circuit. Ions traverse electrolyte-filled pores and the separator; electrons follow the electronically conductive electrode/current-collector path. The separator must prevent electronic contact while allowing ionic transport. During charge the net insertion/deinsertion directions reverse. Use “negative” and “positive electrode” consistently: the electrochemical anode/cathode labels depend on reaction direction.

A graphite half-reaction may be written on discharge as

$$\mathrm{Li_xC_6\rightarrow Li_{x-\delta}C_6+\delta Li^++\delta e^-}.$$

An insertion positive electrode accepts the corresponding lithium and electron inventory. LFP involves the LiFePO4/FePO4 system, whereas a layered NMC host has a composition-dependent lithium occupancy. These schematic balances do not specify reaction kinetics or a universal phase-transition law. The chosen continuum model must supply those closures. [S01, S02]

## Quantities that must remain distinct
Electrode stoichiometry is $\theta=c_s/c_{s,max}$. Full-cell SOC is a reference-dependent usable-charge coordinate, not identical to either electrode's stoichiometry. Electrode usable stoichiometric limits depend on balancing, cutoffs and lithium inventory. Capacity-based SOH is $Q_{ref,aged}/Q_{ref,fresh}$ only when both reference tests use matched conditions. BMS-reported SOC/SOH is an estimator output, not direct ground truth.

An illustrative charge balance, with **discharge-positive** current and ideal coulomb counting, is

$$\dot z=-I/(3600Q_{ref,Ah}).$$

Efficiency corrections, side-reaction currents and capacity evolution must be introduced explicitly rather than hidden in a changing denominator.

## What creates voltage loss and heat
Equilibrium voltage reflects the difference between positive and negative electrode chemical potentials. Under load, electronic/ionic resistance, reaction overpotential and concentration gradients change terminal voltage. Temperature affects diffusion and reaction kinetics; concentration and phase history can affect both equilibrium and transport. A single constant internal resistance cannot represent all these effects across arbitrary current, SOC and temperature. [S02, S03]

The common Arrhenius representation is

$$k(T)=k(T_{ref})\exp\left[-\frac{E_a}{R}\left(\frac1T-\frac1{T_{ref}}\right)\right].$$

Record kelvin, J/mol, reference temperature and the experimentally supported range. A coefficient fitted over one range is not a license to extrapolate into freezing, decomposition or a different electrolyte composition.

## Required evidence
Collect full-cell and half-cell equilibrium relations, electrode capacities/windows, initial lithium inventory, transport functions, kinetic conventions and temperature dependence. Record phase fractions and hysteresis history where relevant. Ordinary cycling, EIS, GITT and structural measurements constrain different parts of the model; they are complementary rather than interchangeable.

## Source basis

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S02: PyBaMM DFN equations](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/DFN.html)
- [S03: PyBaMM thermal models](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/thermal-models.html)
- [S05: PyBaMM parameterisation](https://docs.pybamm.org/en/latest/source/examples/notebooks/parameterization/parameterization.html)
- [S07: CALCE battery data](https://calce.umd.edu/battery-data)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.
