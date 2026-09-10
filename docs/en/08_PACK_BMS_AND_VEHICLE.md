# Pack, BMS and vehicle boundaries

[한국어](../ko/08_PACK_BMS_AND_VEHICLE.md) · [README](../../README.md)

## Pack identity is not a scale factor
The ideal relations $V_{pack}\approx N_sV_{cell}$ and $Q_{pack}\approx N_pQ_{cell}$ are useful checks for identical balanced cells, not a complete pack model. A realistic electrical network must enforce node/branch constraints with interconnect resistance and cell-dependent states. Parallel currents need not be equal; series cells share string current but may reach voltage/temperature limits at different times.

Collect node-edge topology, cell grouping, weld/busbar/contactor/fuse resistance, initial SOC and SOH distributions, batch correlations, cooling contacts and sensor locations. Preserve electrical and thermal graphs separately. Do not infer an OEM topology from a photograph or a nominal pack energy value. Module studies found through Battery Archive are useful intermediate evidence but do not establish a full-vehicle pack model. [S11]

## Control and observation
Record balancing current/thresholds, charger power/current/voltage limits, temperature-dependent charge acceptance, sensor latency/quantization/drift and BMS filtering. Distinguish true model states from reported SOC/SOH. Closed-loop cooling or current limits can mask cell behavior: the observed current is partly a controller response, not an independent experimental excitation.

## Turning speed into a future battery load
EPA provides **prescribed speed versus time**. The included US06 trace is not a battery-current recording. A later load model would need vehicle mass/rotating inertia, grade, rolling resistance, air density, drag/frontal area, drivetrain efficiency and accessory demand. A schematic wheel force is

$$F=m_{eq}\dot v+mgC_{rr}\cos\gamma+mg\sin\gamma+\tfrac12\rho_{air}C_dAv^2,$$

with $P_{wheel}=Fv$ and explicitly defined traction/regeneration efficiency and control limits. The current demand then depends on pack voltage and limits through $P=VI$; voltage depends on state/current, so the coupling is not a fixed conversion factor. HVAC, coolant pumps, battery preconditioning and charging overhead need their own accounting.

Finite differences on a one-second schedule require a declared interpolation/filtering rule. Regenerative energy cannot exceed braking demand or charge acceptance. No battery load, driving range or pack energy prediction has been synthesized in this package. [S17, S18]

## Public-data gap
A public cell dataset plus a standard speed trace is enough to define a transparent hypothetical scenario, not to claim manufacturer-equivalent pack performance. Label every assumed vehicle/pack/control value and keep that scenario separate from observed vehicle telemetry.

## Source basis

- [S03: PyBaMM thermal models](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/thermal-models.html)
- [S11: Battery Archive study summaries](https://batteryarchive.org/study_summaries.html)
- [S17: EPA dynamometer schedules](https://www.epa.gov/vehicle-and-fuel-emissions-testing/dynamometer-drive-schedules)
- [S18: EPA US06 numeric schedule](https://www.epa.gov/system/files/other-files/2025-03/us06col.txt)
- [S20: BLAST battery lifetime models](https://www.nlr.gov/transportation/blast)

Research snapshot: 2026-09-10. Design choices are recommendations, not measured simulator performance.
