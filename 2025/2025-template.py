import sys

infile = sys.argv[1] if len(sys.argv) >= 2 else "./inputs/1.in"

# raw = open(infile).read().strip()
input = open(infile).read().strip()

print(input)

# print(f"{'Solution to Part 1:':<20} {p1}")
# print(f"{'Solution to Part 2:':<20} {p2}")
