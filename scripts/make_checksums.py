"""Create a local integrity manifest after deliberate review of any file changes."""
from common import ROOT, write_json, sha256_file

def main():
    files={}
    for p in sorted(ROOT.rglob("*")):
        if not p.is_file() or "__pycache__" in p.parts or ".git" in p.parts or p.suffix==".pyc":continue
        rel=p.relative_to(ROOT).as_posix()
        if rel=="metadata/SHA256SUMS.json" or rel.startswith("data/raw/"):continue
        files[rel]=sha256_file(p)
    write_json(ROOT/"metadata/SHA256SUMS.json",{
        "scope":"Local release files only; not proof of source/capture identity",
        "exclusions":["this manifest","data/raw","__pycache__",".git","*.pyc"],"files":files})
    print(f"Indexed {len(files)} local files")

if __name__=="__main__":main()
