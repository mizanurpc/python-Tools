import socket
from concurrent.futures import ThreadPoolExecutor

def check(host, port, timeout=0.5):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        return port, s.connect_ex((host, port)) == 0

def scan(host, ports, workers=100):
    ip = socket.gethostbyname(host)
    with ThreadPoolExecutor(max_workers=workers) as pool:
        results = pool.map(lambda p: check(ip, p), ports)
    return [p for p, is_open in results if is_open]

if __name__ == "__main__":
    print(scan("scanme.nmap.org", range(1, 1025)))
