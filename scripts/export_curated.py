"""Normalize captured data and tabulate published OCP fits. No simulation or fitting."""
from __future__ import annotations
import csv
import re
from common import ROOT, read_json, write_json, write_csv, discharge_positive, sample_expression

def main() -> None:
    base = ROOT / "data/curated/about_energy"
    provenance = read_json(base / "provenance.json")
    parameters, cells, ocp, reference = [], [], [], []
    for chem, file in [("LFP", "lfp_18650_bpx_0_1.reserialized.json"),
                       ("NMC", "nmc_pouch_bpx_0_1.reserialized.json")]:
        obj = read_json(base / file)
        did = "AE_" + chem
        prov = next(p for p in provenance if p["dataset_id"] == did)
        cells.append({"cell_id":did + "_reference_unknown_serial", "dataset_id":did,
            "manufacturer_model":None, "batch_id":None,
            "format":"18650 cylindrical" if chem == "LFP" else "pouch",
            "positive_chemistry":"LFP" if chem == "LFP" else "NMC111",
            "negative_chemistry":"graphite",
            "nominal_capacity_Ah":obj["Parameterisation"]["Cell"]["Nominal cell capacity [A.h]"],
            "bpx_version":"0.1", "source_ids":["S01"], "evidence_status":"source_reported",
            "notes":["Logical parameter-set identity, not a verified specimen serial number.",
                     "Mixed measured/fitted/literature/estimated source provenance."]})
        for section, values in obj["Parameterisation"].items():
            for name, value in values.items():
                unit = re.search(r"\[([^]]+)\]", name)
                evidence = "mixed_not_resolved"
                note = "Source supplies no per-parameter uncertainty; do not interpret decimals as accuracy."
                if section == "Electrolyte" or section == "Separator":
                    evidence = "literature"
                    note = "Electrolyte/separator informed by literature; exact per-entry provenance not fully resolved."
                if "Entropic change" in name:
                    evidence = "literature"
                    note = "Entropy data borrowed from cited studies; chemistry/sample match must be checked."
                if section == "Cell" and name in ["Specific heat capacity [J.K-1.kg-1]", "Thermal conductivity [W.m-1.K-1]", "Density [kg.m-3]"]:
                    evidence = "estimated"
                    note = "Source header says other thermal properties are estimated."
                if "Reaction rate constant [" in name:
                    note += " BPX molar-rate convention: do not substitute into a dimensional exchange-current law without conversion."
                domain = None
                if section in {"Negative electrode", "Positive electrode"} and ("OCP" in name or "Entropic" in name):
                    domain = {"stoichiometry_min":values["Minimum stoichiometry"],
                              "stoichiometry_max":values["Maximum stoichiometry"],
                              "reference_temperature_K":298.15,
                              "note":"Source usable stoichiometric window; not independently validated across temperature or age."}
                parameters.append({"parameter_id":f"{did}.{section}.{name}", "dataset_id":did,
                    "section":section, "name":name, "value":value, "unit":unit.group(1) if unit else None,
                    "evidence_type":evidence, "source_id":"S01", "source_blob_sha1":prov["upstream_git_blob_sha1"],
                    "uncertainty":None, "validity_domain":domain, "note":note})
            if section in {"Negative electrode", "Positive electrode"}:
                lo, hi = values["Minimum stoichiometry"], values["Maximum stoichiometry"]
                for i in range(101):
                    x = lo + (hi-lo)*i/100
                    ocp.append({"dataset_id":did, "electrode":section, "stoichiometry":x,
                        "ocp_V_vs_Li":sample_expression(values["OCP [V]"],x,lo,hi),
                        "data_kind":"tabulated_published_fit_not_measurement", "source_id":"S01"})
        for label, curve in obj.get("Validation", {}).items():
            arrays = [curve[k] for k in ("Time [s]","Current [A]","Voltage [V]","Temperature [K]")]
            if len({len(a) for a in arrays}) != 1:
                raise ValueError("Unequal source curve columns")
            for t,i,v,temp in zip(*arrays):
                reference.append({"dataset_id":did,"cell_id":did+"_reference_unknown_serial",
                    "protocol_id":"C20_discharge" if label.startswith("C/20") else "1C_discharge",
                    "segment_id":label,"time_s":t,"current_raw_A":i,
                    "current_discharge_A":discharge_positive(i,"charge"),"voltage_V":v,
                    "reference_temperature_K":temp,"surface_temperature_K":None,"core_temperature_K":None,
                    "data_kind":"source_embedded_reference_curve","source_id":"S01"})
    write_json(ROOT/"data/derived/parameters.json",parameters)
    flat=[]
    for p in parameters:
        row=dict(p)
        for key in ("value","validity_domain","uncertainty"):
            if isinstance(row[key],(dict,list)):
                import json
                row[key]=json.dumps(row[key],ensure_ascii=False)
        flat.append(row)
    write_csv(ROOT/"data/derived/parameters.csv",flat)
    write_json(ROOT/"data/derived/cells.json",cells)
    write_json(ROOT/"data/derived/nmc_reference_curves.json",reference)
    write_csv(ROOT/"data/derived/nmc_reference_curves.csv",reference)
    write_csv(ROOT/"data/derived/ocp_fit_samples.csv",ocp)
    with (ROOT/"data/curated/epa/us06_schedule.transcribed.csv").open(encoding="utf-8",newline="") as stream:
        speed=[{"time_s":int(r["time_s"]),"target_speed_mph":float(r["target_speed_mph"]),
                "target_speed_m_s":float(r["target_speed_mph"])*0.44704,
                "data_kind":"prescribed_speed_not_measured_current","source_id":"S18"}
               for r in csv.DictReader(stream)]
    write_csv(ROOT/"data/derived/us06_si.csv",speed)
    stats={"parameter_records":len(parameters),"cell_parameter_sets":len(cells),
           "embedded_reference_curve_points":len(reference),"ocp_fit_samples":len(ocp),
           "prescribed_speed_points":len(speed),"simulation_runs":0,
           "warning":"Counts of derived rows are not counts of independent experimental observations."}
    write_json(ROOT/"reports/data_summary.json",stats)
    print(stats)

if __name__ == "__main__":
    main()
