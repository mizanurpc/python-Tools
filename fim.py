import sys
import hashlib, json, sys
if len(sys.argv) < 3:
    print("[-] python3 fim.py <baseline|check> <folder_path>")
    sys.exit(1)

mode, folder = sys.argv[1], sys.argv[2]  # baseline | check

from pathlib import Path

def snapshot(folder):
    return {str(p): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in Path(folder).rglob("*") if p.is_file()}

mode, folder = sys.argv[1], sys.argv[2]  # baseline | check
if mode == "baseline":
    data = json.dumps(snapshot(folder), indent=2)
    Path("baseline.json").write_text(data)
else:
    old = json.loads(Path("baseline.json").read_text())
    new = snapshot(folder)
    for f in new.keys() - old.keys(): print("[+] ADDED   ", f)
    for f in old.keys() - new.keys(): print("[-] DELETED ", f)
    for f in new.keys() & old.keys():
        if new[f] != old[f]: print("[!] MODIFIED", f)