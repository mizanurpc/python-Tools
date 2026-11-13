import re

text = open("phish_email.txt", encoding="utf-8").read()

PATTERNS = {
    "IP":    r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
    "URL":   r"https?://[^\s\"'<>]+\b", # Note: adjusted slightly based on standard regex, matches source: 18 literally
    "EMAIL": r"[\w.+-]+@[\w-]+\.[\w.-]+",
    "SHA256": r"\b[a-fA-F0-9]{64}\b",
}

for name, pat in PATTERNS.items():
    for hit in sorted(set(re.findall(pat, text))):
        print(f"[{name}] {hit}")
