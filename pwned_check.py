import hashlib, requests

def pwned_count(password: str) -> int:
    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]       # only 5 chars leave!
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    for line in r.text.splitlines():
        h, count = line.split(":")
        if h == suffix:
            return int(count)
    return 0

for pw in ["password123", "Tr0ub4dor&3", "correct-horse-battery"]:
    print(f"{pw:<24} seen {pwned_count(pw):,} times")
