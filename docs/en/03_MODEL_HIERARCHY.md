# Model hierarchy and evidence requirements

[한국어](../ko/03_MODEL_HIERARCHY.md) · [README](../../README.md)

## Choose fidelity per observable
| Model | Appropriate role | Minimum additional evidence | Main limitation |
|---|---|---|---|
| ECM | Fast terminal voltage and BMS baseline | OCV, pulse/RC maps versus SOC/T/SOH | Internal concentration/reaction states not resolved |
| SPM | Reduced particle diffusion model | Particle/OCP/kinetic identities | Electrolyte limitations simplified |
| SPMe | Reduced electrochemistry including electrolyte effects | Electrolyte transport and geometry | Restricted asymptotic/model assumptions |
| DFN/P2D | Porous-electrode charge/mass/reaction model | Coherent detailed parameter set | Not a direct 3D cell or guaranteed chemistry-complete model |
| Spatial electrothermal | Temperature/current nonuniformity | Collectors, tabs, anisotropic material and boundary data | Higher-dimensional unknowns can dominate accuracy |
| Coupled aging/mechanics | History and damage observables | Mechanism-resolved diagnostics and constitutive data | Identifiability and model-form uncertainty |

The proposed sequence is ECM as a comparison baseline, SPMe/DFN as a scientific reference, and spatial/coupled models only where data supports the added states. This is a research decision, not an instruction to implement any solver in this repository. [S02-S05]

## Core DFN contracts
A representative spherical diffusion equation is

$$\partial_t c_s=\frac{1}{r^2}\partial_r(r^2D_s\partial_r c_s).$$

At the particle center the radial flux vanishes. At the surface, flux is linked to interfacial current density by Faraday's constant under the selected sign convention. Electrode and electrolyte potentials must satisfy charge conservation, and electrolyte salt must satisfy its own transport balance. Specify initial concentrations, no-flux/current-collector conditions, continuity at interfaces and a potential reference. [S02]

For dimensional interfacial current density, a generic Butler-Volmer closure is

$$j=i_0\left[e^{\alpha_aF\eta/(RT)}-e^{-\alpha_cF\eta/(RT)}\right].$$

The units and concentration normalization inside $i_0$ are part of this equation. The BPX legacy molar reaction-rate parameter cannot be inserted blindly into an unrelated implementation's exchange-current function.

## Model-form limits
The source LFP README warns about high-rate/low-SOC discrepancies, cylindrical nonuniformity and limitations of basic Fick/Butler-Volmer descriptions for LFP. Retain these as explicit validity limits; do not hide them by adjusting unrelated thermal coefficients. A converged but misspecified model remains misspecified.

No performance benchmark or runtime claim is supplied because no scientific solver was run. Computational cost must later be measured on a pinned solver, mesh, tolerance and hardware configuration rather than estimated from the model name alone.

## Source basis

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S02: PyBaMM DFN equations](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/DFN.html)
- [S03: PyBaMM thermal models](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/thermal-models.html)
- [S04: PyBaMM coupled degradation](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/coupled-degradation.html)
- [S05: PyBaMM parameterisation](https://docs.pybamm.org/en/latest/source/examples/notebooks/parameterization/parameterization.html)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.
