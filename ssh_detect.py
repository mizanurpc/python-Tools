import re
from collections import Counter

PAT = re.compile(r"Failed password for (?:invalid user )?(\S+) "
                 r"from (\d+\.\d+\.\d+\.\d+)")
THRESHOLD = 5
fails, users = Counter(), {}
with open("auth.log", errors="ignore") as log:
    for line in log:
        if m := PAT.search(line):
            user, ip = m.groups()
            fails[ip] += 1
            users.setdefault(ip, set()).add(user)

for ip, n in fails.most_common():
    if n >= THRESHOLD:
        print(f"[ALERT] {ip}: {n} fails, users={sorted(users[ip])}")
