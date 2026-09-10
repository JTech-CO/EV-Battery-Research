# EV Battery Research | Complete research report

[한국어](RESEARCH_REPORT-KR.md) · [README](README.md)

2026-09-10 · Research/data preparation only. No simulator.

00. [Research summary and decision](#chapter-00)
01. [Operating physics and chemistry](#chapter-01)
02. [Cell structure and material identity](#chapter-02)
03. [Model hierarchy and evidence requirements](#chapter-03)
04. [Electrochemical characterization and parameter use](#chapter-04)
05. [Thermal behavior and cooling boundaries](#chapter-05)
06. [Aging mechanisms and identifiability](#chapter-06)
07. [Mechanics, microstructure and failure](#chapter-07)
08. [Pack, BMS and vehicle boundaries](#chapter-08)
09. [Dataset selection and matching strategy](#chapter-09)
10. [Acquisition, crawling boundaries and reuse](#chapter-10)
11. [Data contracts and normalization](#chapter-11)
12. [Validation and uncertainty plan](#chapter-12)
13. [Gap analysis and research gates](#chapter-13)
14. [Audit of the captured numeric data](#chapter-14)
15. [BPX semantics and version control](#chapter-15)
16. [Source-specific ingestion recipes](#chapter-16)
17. [Handoff to a future scientific-engine project](#chapter-17)
18. [Sources and access audit](#chapter-18)
19. [Technical glossary](#chapter-19)


---

<a id="chapter-00"></a>

## 00. Research summary and decision

### Decision
Build the future research program around **one internally consistent cell parameterization**, not a pool of unrelated battery measurements. Start with the About:Energy NMC111/graphite 12.5 Ah pouch example. Keep the LFP/graphite 2 Ah cylindrical example as a separate chemistry/model-form benchmark. Neither is a verified representation of a current production EV pack. Both source files identify legacy BPX 0.1 and explicitly mix characterization, literature inputs and estimated thermal properties. [S01]

The scientific deliverable should eventually be a set of validated mappings from current, initial state, temperature, cooling and history to terminal voltage, material states, heat generation and aging observables. A realistic rendering or a numerically converged DFN solution alone is not evidence of physical accuracy.

### Four data layers
| Layer | Necessary content | Current package |
|---|---|---|
| Constitutive data | Geometry, electrode OCP, diffusion, reaction rates, electrolyte transport, thermal properties | Two source parameter sets captured; mixed evidence quality |
| Experiments | Charge/discharge, pulses, rest, EIS, calorimetry, aging and expansion | NMC embedded reference curves captured; other studies cataloged |
| Boundary/control conditions | Cooling, pack topology, drive demand, BMS limits, sensors | US06 speed schedule captured; OEM pack/control data missing |
| Evidence | Specimen identity, units, methods, uncertainty, license, version, calibration/holdout roles | Schemas, inventories, provenance and acquisition records |

### What is actually included
The archive contains two **manually transcribed/reserialized JSON captures**, 104 parameter entries extracted from them, 114 NMC embedded reference-curve points and 601 EPA prescribed speed samples. It also contains 404 samples of published OCP fits; these are derived values, not new measurements. The 139-row requirement inventory is a specification of needed information, not 139 acquired measurements.

There are 23 resource cards, including experimental collections, parameter examples, a standard and software references. Do not report this as 23 downloaded experimental datasets. Sixteen immutable About:Energy Git blobs are indexed for later download; none of those raw byte files was downloaded here. No simulation, calibration, ML training, original-data semantic equality check, account change or repository publication was performed.

### Priority
First reconcile the captured BPX files with their original blobs and obtain all matching validation CSVs. Next add independent temperature/thermal measurements for the same cell. Only then introduce identified aging mechanisms and an explicitly parameterized module/pack. Public data supports a rigorous bounded research model; it does not justify a claim of an exact OEM digital twin.

### Source basis

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S06: BPX official standard download and change notes](https://bpxstandard.com/bpx-standard/)
- [S10: LG HG2 dataset v3](https://data.mendeley.com/datasets/cp3473x7xv/3)
- [S17: EPA dynamometer schedules](https://www.epa.gov/vehicle-and-fuel-emissions-testing/dynamometer-drive-schedules)
- [S18: EPA US06 numeric schedule](https://www.epa.gov/system/files/other-files/2025-03/us06col.txt)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.


---

<a id="chapter-01"></a>

## 01. Operating physics and chemistry

### Lithium and charge pathways
During discharge, lithium leaves the negative active material as ions while electrons enter the external circuit. Ions traverse electrolyte-filled pores and the separator; electrons follow the electronically conductive electrode/current-collector path. The separator must prevent electronic contact while allowing ionic transport. During charge the net insertion/deinsertion directions reverse. Use “negative” and “positive electrode” consistently: the electrochemical anode/cathode labels depend on reaction direction.

A graphite half-reaction may be written on discharge as

$$\mathrm{Li_xC_6\rightarrow Li_{x-\delta}C_6+\delta Li^++\delta e^-}.$$

An insertion positive electrode accepts the corresponding lithium and electron inventory. LFP involves the LiFePO4/FePO4 system, whereas a layered NMC host has a composition-dependent lithium occupancy. These schematic balances do not specify reaction kinetics or a universal phase-transition law. The chosen continuum model must supply those closures. [S01, S02]

### Quantities that must remain distinct
Electrode stoichiometry is $\theta=c_s/c_{s,max}$. Full-cell SOC is a reference-dependent usable-charge coordinate, not identical to either electrode's stoichiometry. Electrode usable stoichiometric limits depend on balancing, cutoffs and lithium inventory. Capacity-based SOH is $Q_{ref,aged}/Q_{ref,fresh}$ only when both reference tests use matched conditions. BMS-reported SOC/SOH is an estimator output, not direct ground truth.

An illustrative charge balance, with **discharge-positive** current and ideal coulomb counting, is

$$\dot z=-I/(3600Q_{ref,Ah}).$$

Efficiency corrections, side-reaction currents and capacity evolution must be introduced explicitly rather than hidden in a changing denominator.

### What creates voltage loss and heat
Equilibrium voltage reflects the difference between positive and negative electrode chemical potentials. Under load, electronic/ionic resistance, reaction overpotential and concentration gradients change terminal voltage. Temperature affects diffusion and reaction kinetics; concentration and phase history can affect both equilibrium and transport. A single constant internal resistance cannot represent all these effects across arbitrary current, SOC and temperature. [S02, S03]

The common Arrhenius representation is

$$k(T)=k(T_{ref})\exp\left[-\frac{E_a}{R}\left(\frac1T-\frac1{T_{ref}}\right)\right].$$

Record kelvin, J/mol, reference temperature and the experimentally supported range. A coefficient fitted over one range is not a license to extrapolate into freezing, decomposition or a different electrolyte composition.

### Required evidence
Collect full-cell and half-cell equilibrium relations, electrode capacities/windows, initial lithium inventory, transport functions, kinetic conventions and temperature dependence. Record phase fractions and hysteresis history where relevant. Ordinary cycling, EIS, GITT and structural measurements constrain different parts of the model; they are complementary rather than interchangeable.

### Source basis

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S02: PyBaMM DFN equations](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/DFN.html)
- [S03: PyBaMM thermal models](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/thermal-models.html)
- [S05: PyBaMM parameterisation](https://docs.pybamm.org/en/latest/source/examples/notebooks/parameterization/parameterization.html)
- [S07: CALCE battery data](https://calce.umd.edu/battery-data)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.


---

<a id="chapter-02"></a>

## 02. Cell structure and material identity

### Geometry is part of the physics
Keep at least four scales separate: active particles; porous electrode/separator/current-collector layers; a wound or stacked cell; and a module/pack. A 1D through-thickness electrode model plus particle-radius diffusion is not a literal 3D reconstruction of a wound cell. Tab placement, current-collector resistance and anisotropic heat flow can matter even when electrochemical layers are homogenized. [S02, S03]

| Scale | Data required | Common invalid substitution |
|---|---|---|
| Particle | Size distribution, phase composition, diffusivity, surface area, expansion | One generic spherical radius for all materials |
| Electrode | Thickness, loading, active/binder/void fractions, transport efficiency, conductivity | Porosity alone determines transport |
| Cell | Layer count/area, collector and tab geometry, enclosure, mass, cooling contacts | External cylinder diameter determines internal active area |
| Module/pack | Node-edge connectivity, contacts, thermal network, fixtures | Multiply one cell output by Ns and Np |

For spherical, uniformly represented particles, $a_s=3\epsilon_s/R$ is a model identity. Surface-area-derived active fraction is therefore an **assumption-dependent reconstruction**, not a second independent measurement. Likewise, tortuosity factor, tortuosity length ratio and transport efficiency are not interchangeable definitions. Keep the source definition beside the number.

### Materials cannot be merged by category name
NMC111, nickel-rich NMC compositions, NCA and mixed positive electrodes are not interchangeable parameter identities. Graphite/silicon blends need phase-specific contributions. A laboratory LFP 18650 parameterization does not identify a large automotive prismatic LFP cell. Preserve exact cell variant, batch, formation, storage history and specimen ID, leaving missing fields null.

The About:Energy pouch example specifies electrode face area and 34 electrode pairs. These are not 34 external cells. Mistaking that count for pack parallelization produces area, capacity and heat-scaling errors. [S01]

### Microstructure acquisition
Use CT voxel dimensions, raw versus segmented status, labels, field of view, resolution, calendering and reconstruction metadata. NLR explicitly explains that the carbon-binder region is numerically generated in its reconstructions. Do not label all segmented phases as directly measured. Quantify descriptor sensitivity to segmentation and unresolved pores before using a reconstruction to set effective transport. [S15]

The required inventory is in `catalog/parameter_requirements.csv`. It includes quantities not present in this package. Missing OEM drawings, weld/contact distributions and material constitutive tests remain research gaps, not opportunities to insert undocumented constants.

### Source basis

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S02: PyBaMM DFN equations](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/DFN.html)
- [S03: PyBaMM thermal models](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/thermal-models.html)
- [S15: Battery Microstructures Library](https://www.nlr.gov/transportation/microstructure)
- [S16: Microstructure library agreement](https://www.nlr.gov/transportation/microstructure-library-disclaimer)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.


---

<a id="chapter-03"></a>

## 03. Model hierarchy and evidence requirements

### Choose fidelity per observable
| Model | Appropriate role | Minimum additional evidence | Main limitation |
|---|---|---|---|
| ECM | Fast terminal voltage and BMS baseline | OCV, pulse/RC maps versus SOC/T/SOH | Internal concentration/reaction states not resolved |
| SPM | Reduced particle diffusion model | Particle/OCP/kinetic identities | Electrolyte limitations simplified |
| SPMe | Reduced electrochemistry including electrolyte effects | Electrolyte transport and geometry | Restricted asymptotic/model assumptions |
| DFN/P2D | Porous-electrode charge/mass/reaction model | Coherent detailed parameter set | Not a direct 3D cell or guaranteed chemistry-complete model |
| Spatial electrothermal | Temperature/current nonuniformity | Collectors, tabs, anisotropic material and boundary data | Higher-dimensional unknowns can dominate accuracy |
| Coupled aging/mechanics | History and damage observables | Mechanism-resolved diagnostics and constitutive data | Identifiability and model-form uncertainty |

The proposed sequence is ECM as a comparison baseline, SPMe/DFN as a scientific reference, and spatial/coupled models only where data supports the added states. This is a research decision, not an instruction to implement any solver in this repository. [S02-S05]

### Core DFN contracts
A representative spherical diffusion equation is

$$\partial_t c_s=\frac{1}{r^2}\partial_r(r^2D_s\partial_r c_s).$$

At the particle center the radial flux vanishes. At the surface, flux is linked to interfacial current density by Faraday's constant under the selected sign convention. Electrode and electrolyte potentials must satisfy charge conservation, and electrolyte salt must satisfy its own transport balance. Specify initial concentrations, no-flux/current-collector conditions, continuity at interfaces and a potential reference. [S02]

For dimensional interfacial current density, a generic Butler-Volmer closure is

$$j=i_0\left[e^{\alpha_aF\eta/(RT)}-e^{-\alpha_cF\eta/(RT)}\right].$$

The units and concentration normalization inside $i_0$ are part of this equation. The BPX legacy molar reaction-rate parameter cannot be inserted blindly into an unrelated implementation's exchange-current function.

### Model-form limits
The source LFP README warns about high-rate/low-SOC discrepancies, cylindrical nonuniformity and limitations of basic Fick/Butler-Volmer descriptions for LFP. Retain these as explicit validity limits; do not hide them by adjusting unrelated thermal coefficients. A converged but misspecified model remains misspecified.

No performance benchmark or runtime claim is supplied because no scientific solver was run. Computational cost must later be measured on a pinned solver, mesh, tolerance and hardware configuration rather than estimated from the model name alone.

### Source basis

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S02: PyBaMM DFN equations](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/DFN.html)
- [S03: PyBaMM thermal models](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/thermal-models.html)
- [S04: PyBaMM coupled degradation](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/coupled-degradation.html)
- [S05: PyBaMM parameterisation](https://docs.pybamm.org/en/latest/source/examples/notebooks/parameterization/parameterization.html)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.


---

<a id="chapter-04"></a>

## 04. Electrochemical characterization and parameter use

### Store functions and test conditions
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

### Identification order
Fix independently measured geometry and composition first. Estimate electrode balance and equilibrium relations next. Then constrain transport/kinetics with multiple pulse durations, rates, temperatures and electrode-level evidence. Fit thermal boundary parameters from suitable thermal observations, not by making voltage residuals smaller. Reserve entirely separate protocols/cells for evaluation.

A diffusion time scale roughly involves $R^2/D_s$; voltage data can therefore permit compensating radius/diffusivity changes. Active area and kinetic coefficients also compensate. Sensitivity analysis, profile likelihood/posterior correlation and independent tests are required before claiming unique physical identification. Do not fit every listed parameter simultaneously to a single discharge curve.

### Additional import rules
Preserve raw EIS $Z'$ and $Z''$, frequency and instrument convention. Kramers-Kronig checks require appropriate linear/stationary conditions; a failed check does not uniquely diagnose one material defect. Derived DRT peaks or differential-capacity features are interpretation tools, not direct labels for a unique mechanism.

Do not fill missing temperature dependence with an arbitrary activation energy. A literature value may be used only as an explicit prior with a stated transfer assumption. Retain the source parameterization as one coherent baseline before testing any such substitutions.

### Source basis

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S05: PyBaMM parameterisation](https://docs.pybamm.org/en/latest/source/examples/notebooks/parameterization/parameterization.html)
- [S07: CALCE battery data](https://calce.umd.edu/battery-data)
- [S08: NASA Li-ion aging catalog](https://data.nasa.gov/dataset/li-ion-battery-aging-datasets)
- [S10: LG HG2 dataset v3](https://data.mendeley.com/datasets/cp3473x7xv/3)
- [S28: PyBOP paper](https://arxiv.org/abs/2412.15859)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.


---

<a id="chapter-05"></a>

## 05. Thermal behavior and cooling boundaries

### Separate heat generation from heat removal
For a spatial thermal domain, the working balance is

$$\rho c_p\partial_tT=\nabla\cdot(\mathbf{k}\nabla T)+q_{gen},$$

with explicitly defined contacts, convection, radiation and coolant boundaries. A lumped model replaces spatial temperature with a representative state; it cannot independently predict a core-to-surface gradient that it does not resolve. Obtain anisotropic conductivity, heat capacity, density, sensor placement and cooling geometry. [S03]

A convenient whole-cell diagnostic under discharge-positive current, near-equilibrium thermodynamic assumptions and a consistent OCV definition is

$$\dot Q_{irr}=I(U_{OCV}-V),\qquad \dot Q_{rev}=-IT\frac{\partial U_{OCV}}{\partial T}.$$

This is not a substitute for all nonequilibrium mixing and side-reaction terms in a detailed model. If using distributed ohmic/reaction/entropy heat terms, do not add the same whole-cell loss again. Tab/busbar resistance included in terminal loss must be allocated to its actual thermal domain. Always verify the current and reaction sign conventions before using an entropy term.

### Thermal dataset contract
Record sensor coordinates and attachment, surface versus core versus chamber temperature, sample rate, calibration/lag, current/voltage synchronization, coolant inlet/outlet temperatures, mass flow, contact pressure and calorimeter boundaries. A flat chamber setpoint is not a measured cell-temperature trace. Fit heat transfer and heat capacity using informative experiments rather than a single curve in which they compensate.

The captured BPX files explicitly describe other thermal properties as estimates. Their entropy inputs come from literature. The embedded NMC temperature array is identically 298.15 K; the source excerpt does not establish it as a core or surface sensor measurement. The normalized file therefore stores it as `reference_temperature_K` and leaves surface/core temperature null. [S01]

### Failure heat is a different regime
NLR's failure databank reports body/ejecta heat and mass during triggered thermal runaway. It is useful for conditional failure-energy and variability bounds, not calibration of ordinary reversible/irreversible cycling heat or a universal reaction-kinetics model. The listed spreadsheet revision is February 2024, regardless of later webpage maintenance dates. [S14]

For the next collection round, prioritize matched-cell normal-cycle calorimetry and independent thermal relaxation data before adding a sophisticated cooling visualization. No thermal accuracy has been demonstrated by this package.

### Source basis

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S03: PyBaMM thermal models](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/thermal-models.html)
- [S14: Battery Failure Databank](https://www.nlr.gov/transportation/battery-failure)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.


---

<a id="chapter-06"></a>

## 06. Aging mechanisms and identifiability

### Capacity loss is an observable, not a unique mechanism
Distinguish loss of cyclable lithium inventory (LLI), loss of active material (LAM), SEI growth, lithium plating/stripping and dead lithium, particle cracking, electrolyte depletion, contact degradation and gas-related swelling. Coupling changes the bookkeeping: cracks may create new SEI area; a plated-lithium pathway may also reduce cyclable inventory. Adding separate capacity-loss terms without inventory accounting can double-count the same lithium. [S04]

| Mechanism/state | Needed evidence | Weak evidence alone |
|---|---|---|
| LLI/electrode balance | Matched OCP/DVA analysis and supporting diagnostics | Total capacity loss |
| LAM | Electrode capacity/structural or electrochemical diagnostics | Resistance increase alone |
| SEI | Film/transport evidence, aging matrix, temperature/potential dependence | An arbitrary square-root-time fit |
| Plating/dead lithium | Mechanism-sensitive measurements and charge history | A voltage anomaly alone |
| Cracking/swelling | Mechanical fixture data and structural diagnostics | Unqualified cell-thickness change |

The first aging model should be the smallest identifiable model consistent with available observables. A semiempirical law may be an honest bounded predictor when a more detailed mechanism network is underdetermined. Label that choice rather than describing fitted coefficients as directly measured material properties.

### Experimental design
Keep calendar time, throughput, number of cycles, rest periods, mean SOC, DOD, rates and temperature histories. For one declared convention, equivalent full cycles may be discharge Ah divided by reference capacity; with absolute charge-plus-discharge throughput the denominator is twice that capacity. Do not mix the two definitions. Every capacity/resistance comparison requires a matched reference-performance test.

NASA, Sandia/Archive, CALCE, Oxford, ILCC and MATR provide different history/observable combinations; none should be merged blindly into a universal EV aging curve. Matched cell identity, protocol, censoring and uncertainty are more important than raw row count. [S07-S12, S23, S25]

### Leakage and uncertainty
Split entire cells, batches and source studies before fitting. A cell's late-life traces must not inform an early-life predictor. Derived features such as interpolated capacity and dQ/dV must retain their processing lineage. Mirrors and repackaged datasets must be de-duplicated by original study/specimen identifiers.

Report parameter/posterior correlations, uncertainty in unobserved states and model-form alternatives. A small voltage residual cannot alone validate SEI thickness or plated-lithium mass. Do not infer a universal mechanism from whichever term an optimizer happened to adjust.

### Source basis

- [S04: PyBaMM coupled degradation](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/coupled-degradation.html)
- [S07: CALCE battery data](https://calce.umd.edu/battery-data)
- [S08: NASA Li-ion aging catalog](https://data.nasa.gov/dataset/li-ion-battery-aging-datasets)
- [S09: NASA PCoE data repository](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/)
- [S11: Battery Archive study summaries](https://batteryarchive.org/study_summaries.html)
- [S23: Iowa State ILCC dataset landing](https://doi.org/10.25380/iastate.22582234)
- [S25: Severson/Attia original data-processing repository](https://github.com/rdbraatz/data-driven-prediction-of-battery-cycle-life-before-capacity-degradation)
- [S28: PyBOP paper](https://arxiv.org/abs/2412.15859)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.


---

<a id="chapter-07"></a>

## 07. Mechanics, microstructure and failure

### Coupling levels
For normal operation, link composition-dependent expansion, thermal strain, fixture pressure and contact changes to the electrical/thermal model only when measurements support the coupling. Separate reversible expansion from irreversible swelling, gas accumulation and creep. A thickness sensor under a stiff clamp does not measure free expansion. A constitutive model needs material/fixture geometry, stiffness, preload, temperature and loading history.

Michigan expansion studies are promising because they connect mechanical observations with cycling conditions, but the primary payload was not accessible in this session. Their files, license and fixture metadata are therefore not claimed as collected. The NLR microstructure library is accessible through an agreement; the agreement was not accepted on the user's behalf. [S11, S15, S16, S24]

### Reconstruction uncertainty
Store raw image versus segmentation versus generated phase labels as different artifacts. Preserve voxel spacing and physical coordinates; image pixels alone have no length unit. Evaluate segmentation sensitivity before deriving porosity, particle surface area or a transport tensor. If a binder phase is generated numerically, label downstream transport results as reconstruction-dependent computed quantities rather than direct measurements.

### Failure data is a separate branch
The ORNL/Sandia Mendeley dataset v2 includes mechanical/voltage/temperature histories and specimen metadata. The NLR failure databank adds calorimetric heat partitions and mass outcomes. They constrain different observables: deformation-linked failure response versus total energy/ejecta outcomes. They do not automatically provide a complete multiphase chemical decomposition and gas-flow model. [S13, S14]

Needed additional parameters include chemistry- and SOC-specific reaction networks, reaction enthalpies and kinetics, pressure/vent boundaries, effective short resistance, casing/fixture mechanics, thermal barriers and module propagation observations. Values must be tied to the specific test regime and specimen. A single onset temperature or total heat value is not a universal material constant.

This package provides **data interpretation and model-validation planning only**. It contains no instructions for performing destructive battery tests, inducing failures, modifying protection systems or certifying safety. Later safety claims require appropriate qualified testing, complete boundary conditions and the applicable regulatory process; a fitted simulator is not a replacement.

### Source basis

- [S11: Battery Archive study summaries](https://batteryarchive.org/study_summaries.html)
- [S13: Mechanically induced thermal runaway v2](https://data.mendeley.com/datasets/sn2kv34r4h/2)
- [S14: Battery Failure Databank](https://www.nlr.gov/transportation/battery-failure)
- [S15: Battery Microstructures Library](https://www.nlr.gov/transportation/microstructure)
- [S16: Microstructure library agreement](https://www.nlr.gov/transportation/microstructure-library-disclaimer)
- [S24: Michigan expansion dataset landing](https://deepblue.lib.umich.edu/data/concern/data_sets/5d86p0488)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.


---

<a id="chapter-08"></a>

## 08. Pack, BMS and vehicle boundaries

### Pack identity is not a scale factor
The ideal relations $V_{pack}\approx N_sV_{cell}$ and $Q_{pack}\approx N_pQ_{cell}$ are useful checks for identical balanced cells, not a complete pack model. A realistic electrical network must enforce node/branch constraints with interconnect resistance and cell-dependent states. Parallel currents need not be equal; series cells share string current but may reach voltage/temperature limits at different times.

Collect node-edge topology, cell grouping, weld/busbar/contactor/fuse resistance, initial SOC and SOH distributions, batch correlations, cooling contacts and sensor locations. Preserve electrical and thermal graphs separately. Do not infer an OEM topology from a photograph or a nominal pack energy value. Module studies found through Battery Archive are useful intermediate evidence but do not establish a full-vehicle pack model. [S11]

### Control and observation
Record balancing current/thresholds, charger power/current/voltage limits, temperature-dependent charge acceptance, sensor latency/quantization/drift and BMS filtering. Distinguish true model states from reported SOC/SOH. Closed-loop cooling or current limits can mask cell behavior: the observed current is partly a controller response, not an independent experimental excitation.

### Turning speed into a future battery load
EPA provides **prescribed speed versus time**. The included US06 trace is not a battery-current recording. A later load model would need vehicle mass/rotating inertia, grade, rolling resistance, air density, drag/frontal area, drivetrain efficiency and accessory demand. A schematic wheel force is

$$F=m_{eq}\dot v+mgC_{rr}\cos\gamma+mg\sin\gamma+\tfrac12\rho_{air}C_dAv^2,$$

with $P_{wheel}=Fv$ and explicitly defined traction/regeneration efficiency and control limits. The current demand then depends on pack voltage and limits through $P=VI$; voltage depends on state/current, so the coupling is not a fixed conversion factor. HVAC, coolant pumps, battery preconditioning and charging overhead need their own accounting.

Finite differences on a one-second schedule require a declared interpolation/filtering rule. Regenerative energy cannot exceed braking demand or charge acceptance. No battery load, driving range or pack energy prediction has been synthesized in this package. [S17, S18]

### Public-data gap
A public cell dataset plus a standard speed trace is enough to define a transparent hypothetical scenario, not to claim manufacturer-equivalent pack performance. Label every assumed vehicle/pack/control value and keep that scenario separate from observed vehicle telemetry.

### Source basis

- [S03: PyBaMM thermal models](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/thermal-models.html)
- [S11: Battery Archive study summaries](https://batteryarchive.org/study_summaries.html)
- [S17: EPA dynamometer schedules](https://www.epa.gov/vehicle-and-fuel-emissions-testing/dynamometer-drive-schedules)
- [S18: EPA US06 numeric schedule](https://www.epa.gov/system/files/other-files/2025-03/us06col.txt)
- [S20: BLAST battery lifetime models](https://www.nlr.gov/transportation/blast)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.


---

<a id="chapter-09"></a>

## 09. Dataset selection and matching strategy

### Recommended acquisition stack
| Need | First choice | How to use it |
|---|---|---|
| Coherent electrochemical baseline | About:Energy NMC, separate LFP example | Preserve one cell's parameter set and its reference curves |
| Dynamic electrical/temperature testing | LG HG2, selected CALCE collections | Independent benchmark within the exact cell/protocol identity |
| Aging and impedance history | NASA PCoE, Sandia/Archive, CALCE, MATR | Reference tests, cell/batch holdouts and history-aware analysis |
| Condition interactions and expansion | ILCC and Michigan candidates | Obtain primary files and fixture/condition metadata before use |
| Failure heat and mechanical signatures | NLR Failure, ORNL/Sandia v2 | Separate failure-regime model-validation branch |
| Microstructure priors | NLR microstructure library | Agreement-controlled reconstruction with phase provenance |
| Vehicle demand inputs | EPA schedules | Prescribed speed boundary; vehicle conversion still required |
| Model/schema references | PyBaMM, BPX, BLAST, Materials Project | Definitions and priors, not experimental ground truth |

These are engineering priorities based on complementarity, not a ranking by file count. Read the individual cards for acquisition/rights limitations. Several original landing pages were blocked, several file lists were JavaScript-only, and some data requires a request or agreement. No bypass or submission was attempted.

### Same-cell matching gate
Before combining data, compare manufacturer/variant, positive and negative composition, format, capacity, electrode geometry, formation/batch, electrolyte, temperature, SOC definition, rate, cutoff, rest and age. A mismatch does not necessarily make a source useless; it changes the role from direct calibration evidence to a transfer prior or external comparison. Record that role explicitly.

“Same chemistry” is weaker than “same commercial cell,” which is weaker than “same batch/specimen.” Do not construct a supposedly measured virtual cell from NMC811 diffusion, NMC111 OCP, another cell's thermal conductivity and an unrelated aging law without a documented uncertainty/transfer model.

### Three proposed evidence bundles
**Bundle A: reproducible source benchmark.** The two captured About:Energy sets plus their original validation files. Suitable for checking parameter semantics and source benchmark reproduction, not proof of independent validation.

**Bundle B: matched electrothermal cell.** A chosen single commercial variant with temperature-resolved pulses, cycling, entropy/calorimetry and geometry. The complete matched bundle is not yet acquired.

**Bundle C: aging/module realism.** Add calendar/cycle matrices, expansion/EIS diagnostics and a documented module's thermal/electrical/control data. This is a later evidence target, not a present dataset.

Always count original specimens rather than file copies. Preserve calibration, source-provided reference and truly held-out evidence as separate labels.

### Source basis

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S07: CALCE battery data](https://calce.umd.edu/battery-data)
- [S08: NASA Li-ion aging catalog](https://data.nasa.gov/dataset/li-ion-battery-aging-datasets)
- [S09: NASA PCoE data repository](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/)
- [S10: LG HG2 dataset v3](https://data.mendeley.com/datasets/cp3473x7xv/3)
- [S11: Battery Archive study summaries](https://batteryarchive.org/study_summaries.html)
- [S13: Mechanically induced thermal runaway v2](https://data.mendeley.com/datasets/sn2kv34r4h/2)
- [S14: Battery Failure Databank](https://www.nlr.gov/transportation/battery-failure)
- [S15: Battery Microstructures Library](https://www.nlr.gov/transportation/microstructure)
- [S17: EPA dynamometer schedules](https://www.epa.gov/vehicle-and-fuel-emissions-testing/dynamometer-drive-schedules)
- [S25: Severson/Attia original data-processing repository](https://github.com/rdbraatz/data-driven-prediction-of-battery-cycle-life-before-capacity-degradation)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.


---

<a id="chapter-10"></a>

## 10. Acquisition, crawling boundaries and reuse

### What was done
Public primary pages were searched/read, source metadata was recorded, and GitHub's connected read API supplied the About:Energy parameter text and file-tree/blob identifiers. Two BPX JSONs were manually transcribed/reserialized; EPA's parsed plain-text US06 rows were transcribed into CSV. Direct byte-download attempts did not succeed. No full aging/CT/spreadsheet archive was downloaded. See `metadata/retrieval_audit.json`.

Use **semantic capture** for the included files, not “raw download.” Local SHA-256 checks file integrity after capture; it cannot prove that a transcription equals an unacquired upstream file. The downloader records immutable Git blob SHA-1 separately from local SHA-256, byte size and future retrieval time. A Git tree SHA is not a commit SHA.

### Rights matrix
| Source | Verified or unresolved condition | Repository treatment |
|---|---|---|
| About:Energy | CC BY-SA 4.0 license heading verified | Attribution and share-alike retained for captures and adaptations |
| LG HG2 / mechanical runaway Mendeley v2 | CC BY 4.0 on dataset pages | Metadata only here; preserve attribution after later download |
| NASA aging | Catalog says license not specified | No blanket public-domain assumption; raw data excluded |
| CALCE / Battery Archive | Attribution / study-specific permission | Review chosen files; requests not submitted |
| NLR microstructure | Custom agreement | User review/acceptance required; no volumes included |
| NLR failure spreadsheet | File-level terms/readme not verified | No spreadsheet included |
| EPA | Scientific/educational use described; commercial use not blanket-cleared | Research schedule capture with separate notice; commercial review required |
| BPX specification | Public notes; contact-details download form | No form submitted; no specification PDF bundled |

The repository's original-code license does not relicense any third-party data. Do not delete source attribution or relabel CC BY-SA adaptations as MIT. Metadata availability and download availability do not establish redistribution permission. This is an operational rights audit, not a jurisdiction-specific legal opinion. [S01, S06-S19]

### Reproducible collection
The included collector is **allowlisted**, not a general web spider. Its default is a dry run. With explicit execution/license acknowledgement it requests only 16 verified About:Energy Git blobs, checks expected size and Git object hash, stores local SHA-256 and writes an acquisition report. It refuses changed repository/rights/URL/path assumptions, uses limited retries and avoids cross-host redirects. Its successful live network path was not demonstrated here.

For larger collections, use official APIs/exports and manually accepted agreements. Record version/DOI, server checksum if available, source terms, file list and a dated receipt. Keep download logs free of API keys and personal contact data. Do not scrape hidden endpoints, bypass authentication/CAPTCHA or silently accept terms on behalf of a user.

### Source basis

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S06: BPX official standard download and change notes](https://bpxstandard.com/bpx-standard/)
- [S07: CALCE battery data](https://calce.umd.edu/battery-data)
- [S08: NASA Li-ion aging catalog](https://data.nasa.gov/dataset/li-ion-battery-aging-datasets)
- [S10: LG HG2 dataset v3](https://data.mendeley.com/datasets/cp3473x7xv/3)
- [S12: Battery Archive access page](https://www.batteryarchive.org/)
- [S13: Mechanically induced thermal runaway v2](https://data.mendeley.com/datasets/sn2kv34r4h/2)
- [S14: Battery Failure Databank](https://www.nlr.gov/transportation/battery-failure)
- [S16: Microstructure library agreement](https://www.nlr.gov/transportation/microstructure-library-disclaimer)
- [S19: EPA disclaimers and copyright status](https://www.epa.gov/web-policies-and-procedures/epa-disclaimers)
- [S25: Severson/Attia original data-processing repository](https://github.com/rdbraatz/data-driven-prediction-of-battery-cycle-life-before-capacity-degradation)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.


---

<a id="chapter-11"></a>

## 11. Data contracts and normalization

### Keep three layers
`data/curated` holds captured source content with unchanged scientific meaning where possible, but explicitly altered serialization. `data/raw` is reserved for future verified original bytes and is ignored by Git. `data/derived` holds normalized records and sampled fits with transformation provenance. Never overwrite a source capture during cleaning.

Schemas describe cell identity, parameter evidence, normalized reference-curve records and generic quantity evidence. JSON Schema checks structure, not scientific truth or BPX conformance. Unknown specimen IDs, uncertainty and measured temperatures remain null. Dataset-local logical IDs are not verified manufacturer serial numbers.

### Canonical conventions
| Quantity | Canonical convention | Preserve also |
|---|---|---|
| Time | Seconds, monotonic within a segment | Original timestamp, segment/reset history |
| Current | Positive discharge | Raw current and explicit source convention |
| Temperature | Kelvin | Original Celsius/setpoint/sensor meaning |
| Capacity | Ah with reference protocol | Coulombs if used, cutoff/rate/temp definition |
| Potential | Full-cell V or explicit V vs Li/Li+ | Electrode/reference identity |
| EIS | Real and imaginary ohms plus Hz | Original sign and excitation/rest details |
| Speed | m/s | Source mph and prescribed/measured status |

Conversions used here are $T_K=T_C+273.15$, $1\,Ah=3600\,C$ and $1\,mph=0.44704\,m/s$. About:Energy embedded discharge currents are negative; normalization negates them while retaining the raw values. Do not infer a source's current convention solely from the majority sign in a file.

### Processing rules
Reject nonfinite numbers and unequal curve-column lengths. Check time order per segment; a cycle reset is not necessarily corrupt data. Preserve duplicates and their resolution policy before resampling. Do not interpolate across charge/rest/discharge discontinuities, missing blocks or end-of-test boundaries. Interpolation cannot create a new independent observation or justify a higher effective sampling rate.

Source OCP expressions are parsed with a small AST whitelist, not Python `eval`. The supplied script samples only the source electrode stoichiometric windows. It does not extrapolate electrolyte fits over an invented concentration range. A function may still be scientifically unsuitable inside a syntactic domain; domain checks are not model validation.

The included CSVs are UTF-8 with ASCII machine keys. English/Korean descriptions live in the catalogs and documents. Physical units are encoded in column names or dedicated fields; localized display formatting must never alter stored numeric values.

### Source basis

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S05: PyBaMM parameterisation](https://docs.pybamm.org/en/latest/source/examples/notebooks/parameterization/parameterization.html)
- [S07: CALCE battery data](https://calce.umd.edu/battery-data)
- [S08: NASA Li-ion aging catalog](https://data.nasa.gov/dataset/li-ion-battery-aging-datasets)
- [S17: EPA dynamometer schedules](https://www.epa.gov/vehicle-and-fuel-emissions-testing/dynamometer-drive-schedules)
- [S18: EPA US06 numeric schedule](https://www.epa.gov/system/files/other-files/2025-03/us06col.txt)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.


---

<a id="chapter-12"></a>

## 12. Validation and uncertainty plan

### Evidence levels
Separate data QA, numerical verification, calibration, source-benchmark reproduction, independent validation and deployment qualification. This repository performs only local data/package QA and deterministic transformations. It provides no solver result, fitted model accuracy, safety certification or vehicle deployment qualification.

The source-provided NMC curves may overlap original parameter-development data; their statistical independence is not established. They are therefore labeled **source reference curves**, not a pristine held-out test set. After reproducing them, reserve different protocols, cells/batches and temperature conditions for independent testing.

### Proposed test ladder
1. Validate units, signs, identities, schemas, input completeness and data lineage.
2. In a later solver, check initial consistency, lithium/charge/energy bookkeeping, limits and mesh/time/tolerance convergence.
3. Reproduce source curves without tuning arbitrary unrelated coefficients.
4. Evaluate held-out current profiles, SOC windows and temperatures with a frozen parameter set.
5. Add aging/mechanical/pack tests only when the corresponding observables and boundary conditions exist.

### Draft engineering targets, not achieved results
| Observable | Example starting target for a declared envelope | Necessary qualification |
|---|---|---|
| Cell voltage | RMSE 20 mV or less | Report max error, bias, SOC/rate/temp slices and sensor uncertainty |
| Reference discharge capacity | Relative error 2% or less | Same current, temperature, cutoffs and reference definition |
| Measured surface temperature | RMSE 2 K or less | Real sensor trace and boundary conditions; not a chamber setpoint |
| Aging prediction | Predeclare error/coverage at held-out checkpoints | Cell-level resampling, censoring and horizon defined |
| Pack behavior | Predeclare cell-limit and branch-current error | Full topology, controls and sensor mapping required |

These numbers are suggested starting acceptance budgets for discussion, not standards, published performance claims or guarantees. They must be revised against the intended operating envelope and instrument uncertainties. This package has not met or tested them.

### Uncertainty report
Distinguish measurement error, parameter uncertainty, manufacturing variance, interpolation/processing error, model discrepancy and out-of-domain use. Use parameter covariance/posterior ensembles when justified; report joint rather than independent uncertainties for correlated parameters. Bootstrap cells rather than individual adjacent samples to avoid inflated effective sample size.

Report failed conditions and residual structure, not only a global average. A physically plausible terminal curve does not validate invisible internal concentration, plating or SEI states. The user-facing simulator should eventually expose validity and confidence status rather than silently extrapolate beyond the evidence.

### Source basis

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S05: PyBaMM parameterisation](https://docs.pybamm.org/en/latest/source/examples/notebooks/parameterization/parameterization.html)
- [S07: CALCE battery data](https://calce.umd.edu/battery-data)
- [S10: LG HG2 dataset v3](https://data.mendeley.com/datasets/cp3473x7xv/3)
- [S25: Severson/Attia original data-processing repository](https://github.com/rdbraatz/data-driven-prediction-of-battery-cycle-life-before-capacity-degradation)
- [S28: PyBOP paper](https://arxiv.org/abs/2412.15859)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.


---

<a id="chapter-13"></a>

## 13. Gap analysis and research gates

### Missing evidence that most affects realism
The present baseline lacks independent matched-cell thermal validation, broad temperature characterization, mechanism-resolved aging coefficients, original specimen/batch traceability and OEM pack topology/control/cooling information. LFP phase/hysteresis behavior and composite-electrode mechanics require model-specific evidence beyond a basic parameter exchange file. These are explicit data gaps, not proof that physics-based modeling is impossible.

| Gate | Evidence required before advancing | Stop condition |
|---|---|---|
| G0 Provenance | Original/capture reconciliation, rights, units and identities | Unresolved source or silent transcription mismatch |
| G1 Cell baseline | Same-cell parameter definitions and source curve reproduction | Compensating arbitrary parameters to hide model mismatch |
| G2 Electrothermal | Multiple temperatures and independent real thermal observations | Treating estimated properties/setpoints as measured validation |
| G3 Aging | Defined calendar/cycle matrices and mechanism-relevant diagnostics | Fitting all mechanisms from capacity alone |
| G4 Module/pack | Electrical/thermal graphs, control and synchronized observations | Claiming OEM pack fidelity from a single-cell multiplier |
| G5 Generalization | Held-out cells/batches/protocols, uncertainty and out-of-domain tests | Leakage, mirrored data duplication or unqualified extrapolation |

### Immediate collection backlog
Obtain the 16 pinned About:Energy blobs and run semantic comparison. Inspect full CSV headers and protocol conditions before creating adapters. Retrieve the licensed HG2 and mechanical-failure manifests from official exports. Review selected CALCE/NASA rights and request selected Battery Archive studies. Resolve the blocked Oxford/ILCC/Michigan primary pages and capture exact licenses/versions. Do not treat any of those actions as already completed.

The next scientifically valuable acquisition is not necessarily the biggest archive. A smaller, well-characterized, matched-cell calorimetry/pulse/OCV set may remove more uncertainty than thousands of unmatched cycle-life curves. This prioritization should be revisited after sensitivity/identifiability analysis.

### Work products for the next research phase
Produce a frozen cell identity dossier, versioned parameter source map, calibration/holdout protocol table, missing-observable ledger, uncertainty budget and rights-reviewed raw-data manifest. Only after those are approved should a separate implementation task create a scientific kernel or UI.

This repository makes no schedule or performance promise. It defines evidence gates and records which ones remain open. Future additions should preserve the initial captures and append a dated revision rather than quietly replacing source data or narrowing a failed validation report.

### Source basis

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S03: PyBaMM thermal models](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/thermal-models.html)
- [S04: PyBaMM coupled degradation](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/coupled-degradation.html)
- [S06: BPX official standard download and change notes](https://bpxstandard.com/bpx-standard/)
- [S10: LG HG2 dataset v3](https://data.mendeley.com/datasets/cp3473x7xv/3)
- [S11: Battery Archive study summaries](https://batteryarchive.org/study_summaries.html)
- [S14: Battery Failure Databank](https://www.nlr.gov/transportation/battery-failure)
- [S15: Battery Microstructures Library](https://www.nlr.gov/transportation/microstructure)
- [S24: Michigan expansion dataset landing](https://deepblue.lib.umich.edu/data/concern/data_sets/5d86p0488)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.


---

<a id="chapter-14"></a>

## 14. Audit of the captured numeric data

### Acquisition inventory
| Artifact | Contents | Evidence status |
|---|---|---|
| LFP BPX capture | 2 Ah graphite/LFP 18650, legacy BPX 0.1 | Source text transcribed/reserialized; original bytes not acquired |
| NMC BPX capture | 12.5 Ah graphite/NMC111 pouch, BPX 0.1 | Same capture method; includes source reference curves |
| Parameter export | 104 entries across both parameterizations | Includes conditions, fits and estimates; not 104 independent measurements |
| NMC curve export | 76 C/20 points and 38 1C points | Embedded source reference data, not full raw cycler CSVs |
| OCP samples | 101 samples per electrode, 404 total | Evaluated published functions within source stoichiometric windows |
| US06 schedule | 601 points from 0 to 600 s | Prescribed speed input; transcribed from EPA text |

Both parameter sets have a reference temperature of 298.15 K. The LFP voltage limits are 2.0/3.65 V and the NMC limits are 2.7/4.2 V **within these source examples**, not universal operating limits. LFP's nominal 2 Ah and the pouch's 12.5 Ah are source nominal capacities. Thermal values are partly estimated and entropy inputs are literature-derived. [S01]

### Deterministic checks and integrals
For the captured 1C NMC interval, constant discharge current 12.5 A over 3700 s integrates to approximately **12.8472 Ah**. For C/20, 0.625 A over 75000 s gives **13.0208 Ah**. These are interval integrals, not a remeasurement or certification of cell capacity. They need not equal the nominal 12.5 Ah label. The retained terminal voltages are approximately 2.9047 V and 2.8947 V, above the BPX lower cutoff. Do not extend the records to 2.7 V by invented observations.

Trapezoidal integration of the captured voltage/current samples gives about 46.2534 Wh and 48.3844 Wh over those intervals. This uses linear interpolation between retained samples and does not reconstruct unretained high-frequency behavior. The detailed values/assumptions are in `reports/numeric_audit.json`.

The transcribed US06 maximum is 80.3 mph. Trapezoidal integration of its prescribed speed gives about 12,887.582 m over 600 s. This is a derived schedule distance, **not EV range**, measured trip distance or battery energy demand. [S18]

### Unresolved checks
Original-byte downloads and full original-versus-capture semantic comparison have not succeeded. Checksums in this package prove only local release integrity. The two arrays' constant 298.15 K is not accepted as a measured thermal response. The LFP full validation CSVs and both cells' drive-cycle CSVs remain indexed but uncollected. No accuracy claim follows from these arithmetic checks.

### Source basis

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S18: EPA US06 numeric schedule](https://www.epa.gov/system/files/other-files/2025-03/us06col.txt)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.


---

<a id="chapter-15"></a>

## 15. BPX semantics and version control

### Legacy capture versus current documentation
The captured About:Energy examples explicitly declare **BPX 0.1** and were parameterized in December 2022. The official BPX download page now documents 1.1 additions including SPMe, one-state hysteresis, composite electrodes, LAM/LLI state and a separate cell-state description. The public change notes do not establish compatibility of the captured legacy files with a current parser. The full specification download requires contact details; that form was not submitted. [S01, S06]

Do not change the header to a newer version without a semantic migration. No BPX 1.1 conformance result is provided. The four repository schemas are research-data schemas, not reimplementations of the official BPX schema.

### Migration review table
| Legacy object | Review required |
|---|---|
| `Header.BPX` | Preserve original version; record target schema and migration tool version separately |
| Cell/initial/ambient temperatures | Separate intrinsic parameter references from experiment/initial state |
| Electrode area and parallel pairs | Confirm area/layer normalization; do not map to pack Ns/Np |
| Rate constants | Reconcile molar rate, Faraday factor and concentration normalization with the target equation |
| OCP expressions/tables | Confirm variable definitions, stoichiometric domain and interpolation rules |
| Entropy and thermal values | Preserve literature/estimate provenance; no upgrade to “measured” |
| Validation currents | Retain negative-discharge source convention and documented normalization |
| Aging state | Distinguish state descriptors from kinetics governing their future evolution |

### Version ledger
Record source URL, source blob or release/DOI, source license, acquisition method, exact local hash, parser version, transformation script revision and known semantic changes. The About:Energy tree SHA is recorded as a tree SHA; no commit identity was fabricated. The downloader pins individual blob identities instead of trusting a mutable branch name.

PyBaMM's retrieved `latest` pages identify a development build and warn that notebooks may differ from stable releases. This package does not pin an unverified stable solver or install PyBaMM. During implementation, select an actual tested release and archive its parameter/schema compatibility report.

The first migration test should compare numeric values, expression behavior, initial state, voltage/capacity scaling and current signs on source reference protocols. Merely passing JSON parsing is insufficient. Preserve both original and migrated artifacts so that every changed field is reviewable.

### Source basis

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S02: PyBaMM DFN equations](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/DFN.html)
- [S05: PyBaMM parameterisation](https://docs.pybamm.org/en/latest/source/examples/notebooks/parameterization/parameterization.html)
- [S06: BPX official standard download and change notes](https://bpxstandard.com/bpx-standard/)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.


---

<a id="chapter-16"></a>

## 16. Source-specific ingestion recipes

### Included, executed offline
From the repository root, `python scripts/export_curated.py` reads the two captured BPX files, exports their parameters and embedded reference records, safely samples OCP functions and converts the EPA schedule to m/s. It does not integrate battery dynamics. `python scripts/fetch_sources.py` is a dry run; `python scripts/compare_originals.py` currently reports that original files are missing.

The download sequence for a network-enabled environment is:

```bash
python scripts/fetch_sources.py
python scripts/fetch_sources.py --execute --acknowledge-cc-by-sa
python scripts/compare_originals.py
```

Read source license conditions before the second command. A live download result belongs in its own dated report; do not rewrite the preparation audit to make past acquisition appear successful.

### Other source families: adapter specifications, not implemented collectors
**NASA MAT files.** Preserve the outer cycle type, ambient temperature and start time. Extract measured voltage/current/temperature, charge/discharge instrument channels, relative time and capacity. EIS arrays require frequency/channel interpretation from the original documentation. MATLAB v7.3/HDF5 is different from earlier MAT encoding; choose the parser after inspecting the file header. Do not mistake a MATLAB date vector for elapsed seconds. [S08, S09]

**CALCE and HG2 exports.** Inspect every file's unit and sign labels, temperature/protocol naming, instrument range and reset behavior. Normalize steps separately. Confirm whether capacity is cumulative, per-step, per-cycle or already processed. Unknown source columns must not be dropped silently. Raw file payloads were not inspected here. [S07, S10]

**MATR.** Keep descriptor, summary and cycle-level records linked by original cell ID. Derived `Qdlin`, `Tdlin` and dQ/dV are not raw measurements. Do not unpickle untrusted files: prefer original non-executable numeric formats or an isolated, reviewed conversion path. Modeling-code access has separate academic-license requirements. [S25]

**CT and failure spreadsheets.** Inspect license/readme, coordinate units, phase labels, specimen IDs, trigger/fixture metadata and missing-value conventions before extraction. Gray images, segmented volumes and generated phases are distinct. The referenced XLSX was not opened/parsed, so no claim about its exact sheet-level schema is made. [S13-S16]

Each future adapter should have a tiny licensed fixture, a unit/sign test, an original-to-normalized row-count reconciliation and a documented exclusion policy before processing a whole collection.

### Source basis

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S07: CALCE battery data](https://calce.umd.edu/battery-data)
- [S08: NASA Li-ion aging catalog](https://data.nasa.gov/dataset/li-ion-battery-aging-datasets)
- [S09: NASA PCoE data repository](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/)
- [S10: LG HG2 dataset v3](https://data.mendeley.com/datasets/cp3473x7xv/3)
- [S13: Mechanically induced thermal runaway v2](https://data.mendeley.com/datasets/sn2kv34r4h/2)
- [S14: Battery Failure Databank](https://www.nlr.gov/transportation/battery-failure)
- [S15: Battery Microstructures Library](https://www.nlr.gov/transportation/microstructure)
- [S25: Severson/Attia original data-processing repository](https://github.com/rdbraatz/data-driven-prediction-of-battery-cycle-life-before-capacity-degradation)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.


---

<a id="chapter-17"></a>

## 17. Handoff to a future scientific-engine project

### Scope boundary
This repository is a research/data-preparation asset. It contains no interactive battery model, physics time-stepper, solver integration, trained predictor, web application or deployment pipeline. The transformation scripts do not imply approval to begin simulator development.

A later engineering brief should specify target chemistry/cell identity, observable outputs, operating envelope, acceptable errors, experimental holdouts, compute/runtime budget and what claims the interface may make. Keep a scientific kernel independently testable from rendering and UI.

### Proposed input/output contract
An experiment description should reference a versioned cell parameter set, initial state, current/power/voltage-control protocol, thermal boundaries, stop conditions and requested observables. Do not allow mutually inconsistent input controls without an explicit controller model. The output should retain time, terminal quantities, state provenance, conservation residuals, domain violations, solver settings and uncertainty metadata.

Each field should state whether it is measured input, specified boundary, fitted parameter, estimated prior or predicted state. Visual particle/ion animations must be labeled schematic unless they truly correspond to resolved physical states. Interpolated or model-generated points cannot be presented as laboratory measurements.

### Implementation acceptance gates
Require source/capture reconciliation before automatic parameter import; enforce units/signs; prohibit unsafe expression evaluation; keep fitted priors identifiable; freeze calibration and test partitions; add numerical-convergence and conservation tests; report failed conditions. Only then compare kernel predictions to independent reference data.

The later UI may offer different model levels, but it must not silently change chemistry, phase behavior, thermal assumptions or aging definitions when switching levels. A visually continuous transition is not a physically equivalent model conversion.

### What to hand to a coding agent
Provide this report, source registry, parameter requirement inventory, acquisition/rights ledger, schemas, exact captured datasets and QA results. The first coding-agent assignment should be to validate ingestion against newly acquired originals, not to fill missing science with plausible constants. Unmeasured values remain explicit priors or unresolved requirements.

No repository on the user's account was created or modified. The delivered ZIP is a local, reviewable research snapshot ready for a deliberate publication decision with its mixed-license notices intact.

### Source basis

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S02: PyBaMM DFN equations](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/DFN.html)
- [S05: PyBaMM parameterisation](https://docs.pybamm.org/en/latest/source/examples/notebooks/parameterization/parameterization.html)
- [S06: BPX official standard download and change notes](https://bpxstandard.com/bpx-standard/)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.


---

<a id="chapter-18"></a>

## 18. Sources and access audit

#### S01. About:Energy BPX parameterisation repository

[https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)

Kind: `primary_repository`. Access: `read_via_GitHub_connector`. Rights: `CC-BY-SA-4.0`.

License heading verified; source values captured; binary/byte download unavailable.

#### S02. PyBaMM DFN equations

[https://docs.pybamm.org/en/latest/source/examples/notebooks/models/DFN.html](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/DFN.html)

Kind: `official_documentation`. Access: `read`. Rights: `reference_only`.

Development documentation, not a stable-version installation recommendation.

#### S03. PyBaMM thermal models

[https://docs.pybamm.org/en/latest/source/examples/notebooks/models/thermal-models.html](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/thermal-models.html)

Kind: `official_documentation`. Access: `read`. Rights: `reference_only`.

Thermal geometry, heat sources, contact resistance and cooling boundary conditions.

#### S04. PyBaMM coupled degradation

[https://docs.pybamm.org/en/latest/source/examples/notebooks/models/coupled-degradation.html](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/coupled-degradation.html)

Kind: `official_documentation`. Access: `read`. Rights: `reference_only`.

Model structure is not evidence that all coefficients are identifiable.

#### S05. PyBaMM parameterisation

[https://docs.pybamm.org/en/latest/source/examples/notebooks/parameterization/parameterization.html](https://docs.pybamm.org/en/latest/source/examples/notebooks/parameterization/parameterization.html)

Kind: `official_documentation`. Access: `read`. Rights: `reference_only`.

Parameter functions and characterization workflow.

#### S06. BPX official standard download and change notes

[https://bpxstandard.com/bpx-standard/](https://bpxstandard.com/bpx-standard/)

Kind: `official_standard`. Access: `read_public_page_only`. Rights: `form_gated_documents`.

Public page describes 1.1 extensions. Contact form not submitted; full specification not downloaded.

#### S07. CALCE battery data

[https://calce.umd.edu/battery-data](https://calce.umd.edu/battery-data)

Kind: `primary_data_portal`. Access: `read`. Rights: `no_blanket_license_verified`.

Public data and attribution instructions; individual files need rights review.

#### S08. NASA Li-ion aging catalog

[https://data.nasa.gov/dataset/li-ion-battery-aging-datasets](https://data.nasa.gov/dataset/li-ion-battery-aging-datasets)

Kind: `primary_data_catalog`. Access: `read`. Rights: `license_not_specified`.

Do not infer public-domain status for all contributor data.

#### S09. NASA PCoE data repository

[https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/)

Kind: `primary_data_portal`. Access: `read`. Rights: `per_dataset_review`.

Official links for Battery and Randomized Battery archives; not downloaded.

#### S10. LG HG2 dataset v3

[https://data.mendeley.com/datasets/cp3473x7xv/3](https://data.mendeley.com/datasets/cp3473x7xv/3)

Kind: `primary_dataset`. Access: `read_metadata`. Rights: `CC-BY-4.0`.

DOI 10.17632/cp3473x7xv.3, published 2020-03-05. File list not captured.

#### S11. Battery Archive study summaries

[https://batteryarchive.org/study_summaries.html](https://batteryarchive.org/study_summaries.html)

Kind: `data_custodian_summary`. Access: `read`. Rights: `institution_specific`.

Study-level descriptions; original files/rights must be obtained separately.

#### S12. Battery Archive access page

[https://www.batteryarchive.org/](https://www.batteryarchive.org/)

Kind: `data_custodian_portal`. Access: `read`. Rights: `permission_request`.

Full CSV access by email request; no request sent.

#### S13. Mechanically induced thermal runaway v2

[https://data.mendeley.com/datasets/sn2kv34r4h/2](https://data.mendeley.com/datasets/sn2kv34r4h/2)

Kind: `primary_dataset`. Access: `read_metadata`. Rights: `CC-BY-4.0`.

DOI 10.17632/sn2kv34r4h.2, published 2024-09-24. Numerical files not downloaded.

#### S14. Battery Failure Databank

[https://www.nlr.gov/transportation/battery-failure](https://www.nlr.gov/transportation/battery-failure)

Kind: `primary_data_portal`. Access: `read_metadata`. Rights: `spreadsheet_terms_not_verified`.

Spreadsheet revision February 2024; full spreadsheet not inspected or downloaded.

#### S15. Battery Microstructures Library

[https://www.nlr.gov/transportation/microstructure](https://www.nlr.gov/transportation/microstructure)

Kind: `primary_data_portal`. Access: `read_metadata`. Rights: `custom_agreement`.

Carbon-binder phase is numerically generated in supplied reconstructions.

#### S16. Microstructure library agreement

[https://www.nlr.gov/transportation/microstructure-library-disclaimer](https://www.nlr.gov/transportation/microstructure-library-disclaimer)

Kind: `primary_terms`. Access: `read`. Rights: `custom_agreement_not_accepted`.

Agreement includes notice retention and credit obligations. No acceptance submitted.

#### S17. EPA dynamometer schedules

[https://www.epa.gov/vehicle-and-fuel-emissions-testing/dynamometer-drive-schedules](https://www.epa.gov/vehicle-and-fuel-emissions-testing/dynamometer-drive-schedules)

Kind: `primary_test_schedule`. Access: `read`. Rights: `scientific_educational_use_policy`.

Speed schedules, not measured battery-current records.

#### S18. EPA US06 numeric schedule

[https://www.epa.gov/system/files/other-files/2025-03/us06col.txt](https://www.epa.gov/system/files/other-files/2025-03/us06col.txt)

Kind: `primary_numeric_schedule`. Access: `numeric_text_captured`. Rights: `see_S19`.

601 rows, 0-600 s. Transcribed semantic snapshot, not byte-identical download.

#### S19. EPA disclaimers and copyright status

[https://www.epa.gov/web-policies-and-procedures/epa-disclaimers](https://www.epa.gov/web-policies-and-procedures/epa-disclaimers)

Kind: `primary_terms`. Access: `read`. Rights: `custom_site_policy`.

Scientific/educational distribution is described; commercial use is not blanket-cleared.

#### S20. BLAST battery lifetime models

[https://www.nlr.gov/transportation/blast](https://www.nlr.gov/transportation/blast)

Kind: `official_software_description`. Access: `read`. Rights: `code_and_data_licenses_separate`.

Semiempirical model coefficients are not raw observations.

#### S21. Materials Project API guide

[https://docs.materialsproject.org/downloading-data/using-the-api](https://docs.materialsproject.org/downloading-data/using-the-api)

Kind: `official_api_documentation`. Access: `read`. Rights: `API_terms_review`.

Material calculations are priors, not measured manufactured-cell parameters.

#### S22. Oxford Battery Degradation Dataset 1

[https://ora.ox.ac.uk/objects/uuid:03ba4b01-cfed-46d3-9b1a-7d4a7bdf6fac](https://ora.ox.ac.uk/objects/uuid:03ba4b01-cfed-46d3-9b1a-7d4a7bdf6fac)

Kind: `primary_dataset_landing`. Access: `access_blocked`. Rights: `not_reverified`.

Primary landing blocked in this session. Study information cross-referenced to S11.

#### S23. Iowa State ILCC dataset landing

[https://doi.org/10.25380/iastate.22582234](https://doi.org/10.25380/iastate.22582234)

Kind: `primary_dataset_landing`. Access: `access_blocked`. Rights: `not_reverified`.

Institution DOI linked by S11; primary payload not inspected.

#### S24. Michigan expansion dataset landing

[https://deepblue.lib.umich.edu/data/concern/data_sets/5d86p0488](https://deepblue.lib.umich.edu/data/concern/data_sets/5d86p0488)

Kind: `primary_dataset_landing`. Access: `access_blocked`. Rights: `not_reverified`.

Primary payload not inspected; matching and rights unresolved.

#### S25. Severson/Attia original data-processing repository

[https://github.com/rdbraatz/data-driven-prediction-of-battery-cycle-life-before-capacity-degradation](https://github.com/rdbraatz/data-driven-prediction-of-battery-cycle-life-before-capacity-degradation)

Kind: `author_repository`. Access: `read_via_GitHub_connector`. Rights: `data_license_not_established`.

README distinguishes accessible processing code from modeling code requiring an academic license.

#### S26. MATR Experimental Data Platform

[https://data.matr.io/1/](https://data.matr.io/1/)

Kind: `primary_data_portal`. Access: `javascript_shell_only`. Rights: `not_reverified`.

No hidden API queried; no numerical files retrieved.

#### S27. BatteryML paper

[https://arxiv.org/abs/2310.14714](https://arxiv.org/abs/2310.14714)

Kind: `primary_research_preprint`. Access: `search_metadata_reviewed`. Rights: `reference_only`.

Benchmark/processing framework; dataset-specific rights and source splits still apply.

#### S28. PyBOP paper

[https://arxiv.org/abs/2412.15859](https://arxiv.org/abs/2412.15859)

Kind: `primary_research_preprint`. Access: `search_metadata_reviewed`. Rights: `reference_only`.

Parameter identification framework; does not solve observational non-identifiability.

### Source basis

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S08: NASA Li-ion aging catalog](https://data.nasa.gov/dataset/li-ion-battery-aging-datasets)
- [S16: Microstructure library agreement](https://www.nlr.gov/transportation/microstructure-library-disclaimer)
- [S19: EPA disclaimers and copyright status](https://www.epa.gov/web-policies-and-procedures/epa-disclaimers)
- [S25: Severson/Attia original data-processing repository](https://github.com/rdbraatz/data-driven-prediction-of-battery-cycle-life-before-capacity-degradation)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.


---

<a id="chapter-19"></a>

## 19. Technical glossary

| Term | Expansion | Interpretation |
|---|---|---|
| SOC | State of charge | Reference-dependent usable-charge coordinate; not electrode stoichiometry. |
| SOH | State of health | Always specify capacity, resistance or another definition and reference conditions. |
| OCP / OCV | Open-circuit potential / voltage | State electrode/reference identity and rest/measurement conditions. |
| DFN / P2D | Doyle-Fuller-Newman / pseudo-two-dimensional | Through-electrode and representative-particle dimensions are not literal 3D geometry. |
| SPM / SPMe | Single particle model / with electrolyte | Reduced models with explicit assumptions and operating domains. |
| ECM | Equivalent circuit model | Terminal behavior approximation; internal chemistry is not directly resolved. |
| SEI | Solid electrolyte interphase | A layer and associated mechanisms, not synonymous with all capacity fade. |
| LLI / LAM | Lithium inventory / active-material loss | Distinct latent states requiring supporting evidence. |
| EIS | Electrochemical impedance spectroscopy | Record frequency, excitation, rest, SOC/T and complex signs. |
| GITT / PITT | Intermittent titration methods | Diffusion-related inference depends on model and experimental assumptions. |
| HPPC | Hybrid pulse power characterization | Pulse duration is part of resistance/response definition. |
| DOD / EFC | Depth of discharge / equivalent full cycles | State the SOC/throughput denominator and counting convention. |
| C-rate | Current relative to a reference capacity | Reference Ah and current A are both needed. |
| BPX | Battery Parameter eXchange | Versioned parameter semantics, not automatic model validation. |
| Semantic capture | Transcribed or reserialized source content | Not necessarily byte-identical to the upstream file. |
| Ground truth | Reference observation with known limitations | Not a synonym for BMS estimates, synthetic data or fitted curves. |
| Identifiability | Ability to constrain parameters from observations | Small residuals alone do not establish unique physical parameters. |
| Model discrepancy | Error from incomplete model structure | Must not be hidden entirely inside parameter uncertainty. |

### Source basis

- [S01: About:Energy BPX parameterisation repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
- [S02: PyBaMM DFN equations](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/DFN.html)
- [S05: PyBaMM parameterisation](https://docs.pybamm.org/en/latest/source/examples/notebooks/parameterization/parameterization.html)
- [S06: BPX official standard download and change notes](https://bpxstandard.com/bpx-standard/)
- [S07: CALCE battery data](https://calce.umd.edu/battery-data)
- [S08: NASA Li-ion aging catalog](https://data.nasa.gov/dataset/li-ion-battery-aging-datasets)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.
