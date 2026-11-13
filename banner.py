import socket

def grab_banner(host, port, timeout=3):
    try:
        with socket.create_connection((host, port), timeout) as s:
            if port in (80, 8080):  # HTTP waits for us first
                s.sendall(b"HEAD / HTTP/1.0\r\nHost: "
                          + host.encode() + b"\r\n\r\n")
            return s.recv(1024).decode(errors="replace").strip()
    except OSError as e:  # timeout, refused, ...
        return f"[-] {type(e).__name__}"

for port in (21, 22, 80):
    print(port, "→", grab_banner("192.168.1.1", port)[:80])
