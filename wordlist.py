from pathlib import Path

def load_wordlist(path: str) -> list[str]:
    p = Path(path)
    if not p.is_file():
        raise FileNotFoundError(f"No wordlist at {p}")
    with p.open(encoding="utf-8", errors="ignore") as f:
        return [line.strip() for line in f if line.strip()]

try:
    words = load_wordlist("common.txt")
    print(f"[+] Loaded {len(words)} words")
except FileNotFoundError as e:
    print(f"[-] {e}")
