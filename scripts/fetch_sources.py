"""Fetch the 16 pinned public About:Energy blobs; dry-run unless explicitly executed.

The live network path was not successfully executed in the preparation environment.
This collector does not scrape portals, submit agreements, or unpack archives.
"""
from __future__ import annotations
import argparse
import base64
import datetime as dt
import hashlib
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from common import ROOT, read_json, write_json, safe_destination, git_blob_sha1

REPO = "About-Energy-OpenSource/About-Energy-BPX-Parameterisation"
PREFIX = f"https://api.github.com/repos/{REPO}/git/blobs/"
MAX_RESPONSE_BYTES = 5_000_000

class SameHostRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if urllib.parse.urlsplit(newurl).hostname != "api.github.com":
            raise ValueError("Refusing cross-host redirect")
        return super().redirect_request(req, fp, code, msg, headers, newurl)

def verify_payload(payload: bytes, item: dict) -> None:
    if len(payload) != item["expected_bytes"]:
        raise ValueError("Byte count mismatch")
    if git_blob_sha1(payload) != item["git_blob_sha1"]:
        raise ValueError("Git blob SHA-1 mismatch")

def validate_entry(item: dict) -> None:
    sha = item["git_blob_sha1"]
    if not re.fullmatch(r"[0-9a-f]{40}",sha) or item["url"] != PREFIX+sha:
        raise ValueError("Unapproved URL or blob identity")
    if not (0 < item["expected_bytes"] < 2_000_000):
        raise ValueError("Unexpected file size")
    if not item["destination"].startswith("data/raw/about_energy/"):
        raise ValueError("Unapproved output area")

def fetch(item: dict) -> bytes:
    validate_entry(item)
    opener = urllib.request.build_opener(SameHostRedirect())
    for attempt in range(3):
        request = urllib.request.Request(item["url"], headers={
            "User-Agent":"EV-Battery-Research-Collector/1.0",
            "Accept":"application/vnd.github+json"})
        try:
            with opener.open(request, timeout=30) as response:
                blob = response.read(MAX_RESPONSE_BYTES+1)
            if len(blob) > MAX_RESPONSE_BYTES:
                raise ValueError("Response exceeds size cap")
            record=json.loads(blob)
            if record.get("encoding") != "base64":
                raise ValueError("Unexpected GitHub blob encoding")
            payload=base64.b64decode("".join(record["content"].split()),validate=True)
            verify_payload(payload,item)
            return payload
        except urllib.error.HTTPError as error:
            if error.code not in (429,500,502,503,504) or attempt == 2:
                raise
        except (TimeoutError,urllib.error.URLError):
            if attempt == 2:
                raise
        time.sleep(2**attempt)
    raise RuntimeError("Unreachable retry state")

def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--execute",action="store_true",help="Perform network requests (default: dry-run)")
    parser.add_argument("--acknowledge-cc-by-sa",action="store_true",help="Confirm review of the source attribution/share-alike license")
    args=parser.parse_args()
    manifest=read_json(ROOT/"metadata/acquisition_manifest.json")
    if manifest["rights"] != "CC-BY-SA-4.0" or manifest["repo"] != REPO:
        raise SystemExit("Manifest rights or repository changed; review required")
    for item in manifest["files"]:
        validate_entry(item); safe_destination(ROOT,item["destination"])
    if not args.execute:
        print(json.dumps({"mode":"dry_run","file_count":len(manifest["files"]),
            "expected_bytes":sum(x["expected_bytes"] for x in manifest["files"]),
            "destinations":[x["destination"] for x in manifest["files"]]},indent=2))
        return
    if not args.acknowledge_cc_by_sa:
        raise SystemExit("Review source LICENSE, then supply --acknowledge-cc-by-sa. No request made.")
    results=[]
    for item in manifest["files"]:
        dest=safe_destination(ROOT,item["destination"])
        stamp=dt.datetime.now(dt.timezone.utc).isoformat()
        try:
            if dest.exists():
                payload=dest.read_bytes();verify_payload(payload,item);status="existing_verified"
            else:
                payload=fetch(item);dest.parent.mkdir(parents=True,exist_ok=True)
                tmp=dest.with_name(dest.name+".part");tmp.write_bytes(payload);tmp.replace(dest)
                status="downloaded_verified"
            results.append({"url":item["url"],"path":item["destination"],"status":status,
                "retrieved_at_utc":stamp,"sha256":hashlib.sha256(payload).hexdigest(),"bytes":len(payload)})
        except Exception as error:
            results.append({"url":item["url"],"status":"failed","retrieved_at_utc":stamp,
                            "error":f"{type(error).__name__}: {error}"})
            write_json(ROOT/"reports/live_download_results.json",results)
            raise SystemExit("Download stopped; see reports/live_download_results.json") from error
        time.sleep(1.0)
    write_json(ROOT/"reports/live_download_results.json",results)
    print(f"Verified {len(results)} blobs. Keep the downloaded LICENSE and source attribution.")

if __name__ == "__main__":
    main()
