from collections import Counter

ips = ["10.0.0.5", "10.0.0.9", "10.0.0.5", "10.0.0.5"]

unique = set(ips)              # {'10.0.0.5', '10.0.0.9'}
counts = Counter(ips)          # how many times each IP
print(counts.most_common(1))   # [('10.0.0.5', 3)]

headers = {"Server": "nginx/1.18", "X-Powered-By": "PHP/7.4"}
for name, value in headers.items():
    print(f"[i] {name}: {value}")  # version leak!

