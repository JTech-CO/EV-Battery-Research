# Cell structure and material identity

[한국어](../ko/02_CELL_STRUCTURE_AND_MATERIALS.md) · [README](../../README.md)

## Geometry is part of the physics
Keep at least four scales separate: active particles; porous electrode/separator/current-collector layers; a wound or stacked cell; and a module/pack. A 1D through-thickness electrode model plus particle-radius diffusion is not a literal 3D reconstruction of a wound cell. Tab placement, current-collector resistance and anisotropic heat flow can matter even when electrochemical layers are homogenized. [S02, S03]

| Scale | Data required | Common invalid substitution |
|---|---|---|
| Particle | Size distribution, phase composition, diffusivity, surface area, expansion | One generic spherical radius for all materials |
| Electrode | Thickness, loading, active/binder/void fractions, transport efficiency, conductivity | Porosity alone determines transport |
| Cell | Layer count/area, collector and tab geometry, enclosure, mass, cooling contacts | External cylinder diameter determines internal active area |
| Module/pack | Node-edge connectivity, contacts, thermal network, fixtures | Multiply one cell output by Ns and Np |

For spherical, uniformly represented particles, $a_s=3\epsilon_s/R$ is a model identity. Surface-area-derived active fraction is therefore an **assumption-dependent reconstruction**, not a second independent measurement. Likewise, tortuosity factor, tortuosity length ratio and transport efficiency are not interchangeable definitions. Keep the source definition beside the number.

## Materials cannot be merged by category name
NMC111, nickel-rich NMC compositions, NCA and mixed positive electrodes are not interchangeable parameter identities. Graphite/silicon blends need phase-specific contributions. A laboratory LFP 18650 parameterization does not identify a large automotive prismatic LFP cell. Preserve exact cell variant, batch, formation, storage history and specimen ID, leaving missing fields null.

The About:Energy pouch example specifies electrode face area and 34 electrode pairs. These are not 34 external cells. Mistaking that count for pack parallelization produces area, capacity and heat-scaling errors. [S01]

## Microstructure acquisition
Use CT voxel dimensions, raw versus segmented status, labels, field of view, resolution, calendering and reconstruction metadata. NLR explicitly explains that the carbon-binder region is numerically generated in its reconstructions. Do not label all segmented phases as directly measured. Quantify descriptor sensitivity to segmentation and unresolved pores before using a reconstruction to set effective transport. [S15]

The required inventory is in `catalog/parameter_requirements.csv`. It includes quantities not present in this package. Missing OEM drawings, weld/contact distributions and material constitutive tests remain research gaps, not opportunities to insert undocumented constants.

## Source basis

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S02: PyBaMM DFN equations](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/DFN.html)
- [S03: PyBaMM thermal models](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/thermal-models.html)
- [S15: Battery Microstructures Library](https://www.nlr.gov/transportation/microstructure)
- [S16: Microstructure library agreement](https://www.nlr.gov/transportation/microstructure-library-disclaimer)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.
