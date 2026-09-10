"""Integrate only retained reference intervals and a prescribed schedule.

This is a numerical data audit, not a battery or vehicle simulation. It does
not extrapolate to cutoff, estimate thermal states, or infer vehicle range.
"""
from __future__ import annotations

import csv
from typing import Any

from common import ROOT, read_json, write_json


def audit() -> dict[str, Any]:
    curves = read_json(ROOT / "data/derived/nmc_reference_curves.json")
    integrals: list[dict[str, Any]] = []
    for protocol in sorted({row["protocol_id"] for row in curves}):
        rows = [row for row in curves if row["protocol_id"] == protocol]
        if len(rows) < 2:
            raise ValueError(f"Insufficient samples for {protocol}")
        q_ah = 0.0
        energy_wh = 0.0
        for previous, current in zip(rows, rows[1:]):
            dt = current["time_s"] - previous["time_s"]
            if dt <= 0:
                raise ValueError(f"Non-increasing time in {protocol}")
            q_ah += (current["current_discharge_A"] + previous["current_discharge_A"]) / 2 * dt / 3600
            energy_wh += (current["current_discharge_A"] * current["voltage_V"]
                          + previous["current_discharge_A"] * previous["voltage_V"]) / 2 * dt / 3600
        integrals.append({
            "protocol_id": protocol,
            "points": len(rows),
            "duration_s": rows[-1]["time_s"] - rows[0]["time_s"],
            "initial_voltage_V": rows[0]["voltage_V"],
            "final_voltage_V": rows[-1]["voltage_V"],
            "integrated_available_interval_Ah": q_ah,
            "trapezoidal_available_interval_Wh": energy_wh,
            "interpretation": "Integral over captured reference interval; not certified full-test capacity or energy."
        })
    with (ROOT / "data/derived/us06_si.csv").open(encoding="utf-8", newline="") as stream:
        schedule = list(csv.DictReader(stream))
    if len(schedule) < 2:
        raise ValueError("Insufficient prescribed speed samples")
    distance_m = 0.0
    for previous, current in zip(schedule, schedule[1:]):
        dt = int(current["time_s"]) - int(previous["time_s"])
        if dt <= 0:
            raise ValueError("Non-increasing prescribed schedule time")
        distance_m += (float(current["target_speed_m_s"]) + float(previous["target_speed_m_s"])) / 2 * dt
    return {
        "nmc_reference_integrals": integrals,
        "us06": {
            "points": len(schedule),
            "duration_s": int(schedule[-1]["time_s"]) - int(schedule[0]["time_s"]),
            "max_mph": max(float(row["target_speed_mph"]) for row in schedule),
            "trapezoidal_distance_m": distance_m,
            "interpretation": "Derived prescribed-schedule distance, not a measured trip or EV range."
        },
        "assumptions": [
            "Linear interpolation between retained samples for the trapezoidal integrals",
            "No extrapolation to the BPX cutoff voltage",
            "No cell thermal sensor inferred from constant reference temperature"
        ]
    }


def main() -> None:
    result = audit()
    write_json(ROOT / "reports/numeric_audit.json", result)
    print("Wrote reports/numeric_audit.json; no simulation or physical validation performed.")


if __name__ == "__main__":
    main()
