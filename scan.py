import argparse

parser = argparse.ArgumentParser(description="Tiny port scanner")
parser.add_argument("target", help="IP or host (authorized only)")
parser.add_argument("-p", "--ports", default="1-1024",
                    help="range, e.g. 20-443")
parser.add_argument("-t", "--timeout", type=float, default=0.5)
parser.add_argument("-v", "--verbose", action="store_true")
args = parser.parse_args()

start, end = map(int, args.ports.split("-"))
print(args.target, start, end, args.timeout)

# $ python3 scan.py 127.0.0.1 -p 20-100 -v
