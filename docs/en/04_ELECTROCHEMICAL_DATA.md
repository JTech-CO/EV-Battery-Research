# Electrochemical characterization and parameter use

[한국어](../ko/04_ELECTROCHEMICAL_DATA.md) · [README](../../README.md)

## Store functions and test conditions
The useful object is often $D_s(\theta,T)$, $\kappa_e(c_e,T)$, $U(\theta,T,history)$ or $i_0(c_e,c_s,T)$ rather than one constant. A constant may be an intentional approximation; label it as such. Record method, concentration convention, electrode area normalization, temperature, rest duration, rate and uncertainty beside each parameter. [S01, S05]

| Measurement | Main constraint | Essential caveat |
|---|---|---|
| Low-rate/full-cell OCV | Equilibrium voltage and capacity windows | Finite current is not exact equilibrium; relaxation and hysteresis remain |
| Half-cell OCP | Electrode-specific equilibrium curves | Teardown/reassembly may alter specimen conditions |
| GITT/PITT | Diffusion-related response | Geometry, phase behavior and thermodynamic slope affect inference |
| Pulses/HPPC | Transient resistance and RC response | Resistance depends on pulse duration and SOC/T/history |
| EIS | Frequency-dependent linear response | Record excitation, rest, stationarity and complex-sign convention |
| Rate/drive cycles | Combined dynamic response | Good terminal fit does not identify each internal coefficient |

CALCE supplies useful examples of low-current and incremental OCV characterization and dynamic profiles. NASA aging records include time-series and impedance channels. The LG HG2 source reports accuracy as 0.1% of instrument full scale, which must not be rewritten as 0.1% of each reading. [S07, S08, S10]

## Identification order
Fix independently measured geometry and composition first. Estimate electrode balance and equilibrium relations next. Then constrain transport/kinetics with multiple pulse durations, rates, temperatures and electrode-level evidence. Fit thermal boundary parameters from suitable thermal observations, not by making voltage residuals smaller. Reserve entirely separate protocols/cells for evaluation.

A diffusion time scale roughly involves $R^2/D_s$; voltage data can therefore permit compensating radius/diffusivity changes. Active area and kinetic coefficients also compensate. Sensitivity analysis, profile likelihood/posterior correlation and independent tests are required before claiming unique physical identification. Do not fit every listed parameter simultaneously to a single discharge curve.

## Additional import rules
Preserve raw EIS $Z'$ and $Z''$, frequency and instrument convention. Kramers-Kronig checks require appropriate linear/stationary conditions; a failed check does not uniquely diagnose one material defect. Derived DRT peaks or differential-capacity features are interpretation tools, not direct labels for a unique mechanism.

Do not fill missing temperature dependence with an arbitrary activation energy. A literature value may be used only as an explicit prior with a stated transfer assumption. Retain the source parameterization as one coherent baseline before testing any such substitutions.

## Source basis

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S05: PyBaMM parameterisation](https://docs.pybamm.org/en/latest/source/examples/notebooks/parameterization/parameterization.html)
- [S07: CALCE battery data](https://calce.umd.edu/battery-data)
- [S08: NASA Li-ion aging catalog](https://data.nasa.gov/dataset/li-ion-battery-aging-datasets)
- [S10: LG HG2 dataset v3](https://data.mendeley.com/datasets/cp3473x7xv/3)
- [S28: PyBOP paper](https://arxiv.org/abs/2412.15859)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.
