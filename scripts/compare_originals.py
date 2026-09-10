"""Compare curated semantic BPX captures with verified raw files after acquisition."""
from common import ROOT, read_json, write_json

def main():
    results=[]
    for chem,filename in [("LFP","lfp_18650_cell_BPX.json"),("NMC","nmc_pouch_cell_BPX.json")]:
        raw=ROOT/"data/raw/about_energy"/chem/filename
        curated=ROOT/"data/curated/about_energy"/("lfp_18650_bpx_0_1.reserialized.json" if chem=="LFP" else "nmc_pouch_bpx_0_1.reserialized.json")
        if not raw.exists():
            results.append({"chemistry":chem,"status":"not_checked_raw_file_missing"})
        else:
            results.append({"chemistry":chem,"status":"semantically_equal" if read_json(raw)==read_json(curated) else "different_review_required"})
    write_json(ROOT/"reports/original_comparison.json",results)
    print(results)
    if any(x["status"]=="different_review_required" for x in results):
        raise SystemExit(1)

if __name__=="__main__": main()
