"""Validate local structure and data; not a scientific-solver validation."""
from __future__ import annotations
import argparse
import csv
import json
import math
import re
import sys
import urllib.parse
from pathlib import Path
from common import ROOT, read_json, write_json, sha256_file

def validate(verify_checksums: bool = False) -> dict:
    errors=[]
    sources=read_json(ROOT/"metadata/sources.json")
    resources=read_json(ROOT/"catalog/resources.json")
    requirements=read_json(ROOT/"catalog/parameter_requirements.json")
    ids={s["source_id"] for s in sources}
    if len(ids)!=len(sources):errors.append("Duplicate source IDs")
    if len({r["dataset_id"] for r in resources})!=len(resources):errors.append("Duplicate resource IDs")
    if len({r["parameter_id"] for r in requirements})!=len(requirements):errors.append("Duplicate requirement IDs")
    for r in resources:
        if not set(r["source_ids"]).issubset(ids):errors.append("Unresolved resource source")
        for lang in ("en","ko"):
            if not (ROOT/"catalog/cards"/lang/(r["dataset_id"]+".md")).exists():errors.append("Missing bilingual card")
    for r in requirements:
        if not set(r["source_ids"].split(";")).issubset(ids):errors.append("Unresolved requirement source")
        if r["target_cell_value"] is not None:errors.append("Requirement wrongly presented as collected target value")
    if {p.name for p in (ROOT/"docs/en").glob("*.md")} != {p.name for p in (ROOT/"docs/ko").glob("*.md")}:
        errors.append("Research document language mismatch")
    md_count=0
    for path in ROOT.rglob("*.md"):
        if "data/raw" in path.as_posix():continue
        md_count+=1
        text=path.read_text(encoding="utf-8")
        for match in re.finditer(r"\]\(([^)\s]+)(?:\s+[^)]*)?\)",text):
            url=match.group(1)
            if url.startswith(("http:","https:","mailto:","#")):continue
            rel=urllib.parse.unquote(url.split("#",1)[0])
            if rel and not (path.parent/rel).resolve().exists():
                errors.append(f"Broken local link: {path.relative_to(ROOT)} -> {rel}")
        if "turn" in text and re.search(r"turn\d+(?:view|file|search)\d+",text):
            errors.append("Internal tool citation leaked into artifact")
    # Full structural checks with a declared dependency; no fallback claiming validation.
    try:
        import jsonschema
        schema_items=[("cell_metadata.schema.json","data/derived/cells.json"),
            ("parameter_record.schema.json","data/derived/parameters.json"),
            ("normalized_timeseries.schema.json","data/derived/nmc_reference_curves.json")]
        for schemafile,datafile in schema_items:
            schema=read_json(ROOT/"schemas"/schemafile)
            jsonschema.Draft202012Validator.check_schema(schema)
            validator=jsonschema.Draft202012Validator(schema)
            for index,row in enumerate(read_json(ROOT/datafile)):
                for error in validator.iter_errors(row):
                    errors.append(f"Schema {datafile}:{index}: {error.message}")
        for path in (ROOT/"schemas").glob("*.json"):
            jsonschema.Draft202012Validator.check_schema(read_json(path))
        schema_status="passed" if not any(e.startswith("Schema") for e in errors) else "failed"
    except ImportError:
        errors.append("jsonschema dependency missing; install requirements.txt")
        schema_status="not_executed"
    curves=read_json(ROOT/"data/derived/nmc_reference_curves.json")
    if len(curves)!=114:errors.append("Reference curve count mismatch")
    for protocol in {x["protocol_id"] for x in curves}:
        group=[x for x in curves if x["protocol_id"]==protocol]
        times=[x["time_s"] for x in group]
        if any(b<=a for a,b in zip(times,times[1:])):errors.append("Reference time order")
        for x in group:
            if x["current_discharge_A"] != -x["current_raw_A"]:errors.append("Current sign conversion")
            if x["surface_temperature_K"] is not None or x["core_temperature_K"] is not None:
                errors.append("Invented measured temperature")
    with (ROOT/"data/derived/us06_si.csv").open(encoding="utf-8",newline="") as f:speeds=list(csv.DictReader(f))
    if len(speeds)!=601 or [int(x["time_s"]) for x in speeds]!=list(range(601)):errors.append("US06 time/count mismatch")
    for x in speeds:
        if not math.isclose(float(x["target_speed_m_s"]),float(x["target_speed_mph"])*0.44704,abs_tol=1e-12):
            errors.append("Speed conversion")
    if verify_checksums:
        index=read_json(ROOT/"metadata/SHA256SUMS.json")
        for rel,expected in index["files"].items():
            p=ROOT/rel
            if not p.is_file() or sha256_file(p)!=expected:errors.append(f"Checksum mismatch: {rel}")
    return {"status":"passed" if not errors else "failed","scope":"Local package/schema/data QA only",
        "source_count":len(sources),"resource_count":len(resources),"requirement_count":len(requirements),
        "research_chapters_per_language":len(list((ROOT/"docs/en").glob("*.md"))),
        "markdown_files_checked":md_count,"json_schema_status":schema_status,
        "embedded_reference_points":len(curves),"prescribed_speed_points":len(speeds),
        "checksum_verification":"performed" if verify_checksums else "not_requested",
        "not_validated":["upstream-versus-capture semantic identity","physical model accuracy","live download success","OEM pack fidelity"],
        "errors":errors}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify-checksums",action="store_true")
    parser.add_argument("--write-report",action="store_true")
    args=parser.parse_args();report=validate(args.verify_checksums)
    if args.write_report:write_json(ROOT/"reports/package_validation.json",report)
    print(json.dumps(report,indent=2,ensure_ascii=False))
    if report["errors"]:sys.exit(1)

if __name__=="__main__":main()
