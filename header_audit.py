import requests

REQUIRED = ["Strict-Transport-Security", "Content-Security-Policy",
            "X-Content-Type-Options", "X-Frame-Options",
            "Referrer-Policy", "Permissions-Policy"]
LEAKY = ["Server", "X-Powered-By", "X-AspNet-Version"]

def audit(url):
    r = requests.get(url, timeout=10)
    print(f"[i] {r.url} → {r.status_code}")
    for h in REQUIRED:
        print(("[+] " if h in r.headers else "[-] MISSING ") + h)
    for h in LEAKY:
        if h in r.headers:
            print(f"[!] Info leak  {h}: {r.headers[h]}")

audit("http://bytecapsuleit.com")  # e.g. OWASP Juice Shop
