"""Offline unit tests. No network request, simulator or model accuracy test."""
import csv
import math
import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from common import ROOT, git_blob_sha1, safe_destination, discharge_positive, celsius_to_kelvin, sample_expression, read_json
from fetch_sources import verify_payload, validate_entry, PREFIX

class Helpers(unittest.TestCase):
    def test_empty_git_blob(self):
        self.assertEqual(git_blob_sha1(b""),"e69de29bb2d1d6434b8b29ae775ad8c2e48c5391")
    def test_current_sign(self):
        self.assertEqual(discharge_positive(-12.5,"charge"),12.5)
        self.assertEqual(discharge_positive(12.5,"discharge"),12.5)
    def test_unknown_sign_rejected(self):
        with self.assertRaises(ValueError):discharge_positive(1,"unknown")
    def test_nonfinite_current(self):
        with self.assertRaises(ValueError):discharge_positive(float("nan"),"charge")
    def test_temperature(self):
        self.assertAlmostEqual(celsius_to_kelvin(25),298.15)
    def test_invalid_temperature(self):
        with self.assertRaises(ValueError):celsius_to_kelvin(-300)
    def test_path_escape(self):
        with self.assertRaises(ValueError):safe_destination(ROOT,"../outside.txt")
    def test_absolute_path(self):
        with self.assertRaises(ValueError):safe_destination(ROOT,"/tmp/outside.txt")
    def test_windows_escape(self):
        with self.assertRaises(ValueError):safe_destination(ROOT,"..\\outside.txt")
    def test_valid_path(self):
        self.assertEqual(safe_destination(ROOT,"data/derived/x.json"),ROOT/"data/derived/x.json")
    def test_expression_math(self):
        self.assertAlmostEqual(sample_expression("2*x+exp(0)+tanh(0)",.5,0,1),2)
    def test_expression_import_rejected(self):
        with self.assertRaises(ValueError):sample_expression("__import__('os').system('echo no')",.5,0,1)
    def test_expression_attribute_rejected(self):
        with self.assertRaises(ValueError):sample_expression("x.real",.5,0,1)
    def test_expression_outside_domain(self):
        with self.assertRaises(ValueError):sample_expression("x",1.1,0,1)
    def test_exponent_budget(self):
        with self.assertRaises(ValueError):sample_expression("2**1000000",.5,0,1)
    def test_blob_integrity(self):
        p=b"test\n";verify_payload(p,{"expected_bytes":len(p),"git_blob_sha1":git_blob_sha1(p)})
    def test_blob_tamper_rejected(self):
        with self.assertRaises(ValueError):verify_payload(b"bad",{"expected_bytes":3,"git_blob_sha1":"0"*40})
    def test_unapproved_url(self):
        with self.assertRaises(ValueError):validate_entry({"url":"https://example.com/x","git_blob_sha1":"0"*40,"expected_bytes":1,"destination":"data/raw/about_energy/a"})

class CapturedData(unittest.TestCase):
    def test_reference_count(self):
        self.assertEqual(len(read_json(ROOT/"data/derived/nmc_reference_curves.json")),114)
    def test_parameters_count(self):
        self.assertEqual(len(read_json(ROOT/"data/derived/parameters.json")),104)
    def test_required_not_measured(self):
        r=read_json(ROOT/"catalog/parameter_requirements.json")
        self.assertEqual(len(r),139)
        self.assertTrue(all(x["target_cell_value"] is None for x in r))
    def test_no_invented_sensor(self):
        self.assertTrue(all(x["surface_temperature_K"] is None and x["core_temperature_K"] is None for x in read_json(ROOT/"data/derived/nmc_reference_curves.json")))
    def test_us06_rows(self):
        with (ROOT/"data/curated/epa/us06_schedule.transcribed.csv").open(newline="",encoding="utf-8") as f:r=list(csv.DictReader(f))
        self.assertEqual([int(x["time_s"]) for x in r],list(range(601)))
        self.assertEqual(max(float(x["target_speed_mph"]) for x in r),80.3)
    def test_ocp_finite(self):
        with (ROOT/"data/derived/ocp_fit_samples.csv").open(newline="",encoding="utf-8") as f:r=list(csv.DictReader(f))
        self.assertEqual(len(r),404)
        self.assertTrue(all(math.isfinite(float(x["ocp_V_vs_Li"])) for x in r))
    def test_no_claim_of_raw_download(self):
        self.assertTrue(all(not x["downloaded_in_this_delivery"] for x in read_json(ROOT/"metadata/acquisition_manifest.json")["files"]))
    def test_legacy_bpx_preserved(self):
        for p in (ROOT/"data/curated/about_energy").glob("*.reserialized.json"):
            self.assertEqual(read_json(p)["Header"]["BPX"],0.1)

if __name__=="__main__":unittest.main()
