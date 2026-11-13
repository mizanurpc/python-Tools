import ipaddress

def classify(ip: str) -> str:
    """Return 'private', 'public' or 'invalid'."""
    try:
        addr = ipaddress.ip_address(ip)
    except ValueError:
        return "invalid"
    return "private" if addr.is_private else "public"

for ip in ["192.168.1.10", "8.8.8.8", "999.1.1.1"]:
    print(f"{ip:<15} → {classify(ip)}")
