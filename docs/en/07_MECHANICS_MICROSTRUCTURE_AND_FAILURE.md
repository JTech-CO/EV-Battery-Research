# Mechanics, microstructure and failure

[한국어](../ko/07_MECHANICS_MICROSTRUCTURE_AND_FAILURE.md) · [README](../../README.md)

## Coupling levels
For normal operation, link composition-dependent expansion, thermal strain, fixture pressure and contact changes to the electrical/thermal model only when measurements support the coupling. Separate reversible expansion from irreversible swelling, gas accumulation and creep. A thickness sensor under a stiff clamp does not measure free expansion. A constitutive model needs material/fixture geometry, stiffness, preload, temperature and loading history.

Michigan expansion studies are promising because they connect mechanical observations with cycling conditions, but the primary payload was not accessible in this session. Their files, license and fixture metadata are therefore not claimed as collected. The NLR microstructure library is accessible through an agreement; the agreement was not accepted on the user's behalf. [S11, S15, S16, S24]

## Reconstruction uncertainty
Store raw image versus segmentation versus generated phase labels as different artifacts. Preserve voxel spacing and physical coordinates; image pixels alone have no length unit. Evaluate segmentation sensitivity before deriving porosity, particle surface area or a transport tensor. If a binder phase is generated numerically, label downstream transport results as reconstruction-dependent computed quantities rather than direct measurements.

## Failure data is a separate branch
The ORNL/Sandia Mendeley dataset v2 includes mechanical/voltage/temperature histories and specimen metadata. The NLR failure databank adds calorimetric heat partitions and mass outcomes. They constrain different observables: deformation-linked failure response versus total energy/ejecta outcomes. They do not automatically provide a complete multiphase chemical decomposition and gas-flow model. [S13, S14]

Needed additional parameters include chemistry- and SOC-specific reaction networks, reaction enthalpies and kinetics, pressure/vent boundaries, effective short resistance, casing/fixture mechanics, thermal barriers and module propagation observations. Values must be tied to the specific test regime and specimen. A single onset temperature or total heat value is not a universal material constant.

This package provides **data interpretation and model-validation planning only**. It contains no instructions for performing destructive battery tests, inducing failures, modifying protection systems or certifying safety. Later safety claims require appropriate qualified testing, complete boundary conditions and the applicable regulatory process; a fitted simulator is not a replacement.

## Source basis

- [S11: Battery Archive study summaries](https://batteryarchive.org/study_summaries.html)
- [S13: Mechanically induced thermal runaway v2](https://data.mendeley.com/datasets/sn2kv34r4h/2)
- [S14: Battery Failure Databank](https://www.nlr.gov/transportation/battery-failure)
- [S15: Battery Microstructures Library](https://www.nlr.gov/transportation/microstructure)
- [S16: Microstructure library agreement](https://www.nlr.gov/transportation/microstructure-library-disclaimer)
- [S24: Michigan expansion dataset landing](https://deepblue.lib.umich.edu/data/concern/data_sets/5d86p0488)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.
