"""
# Problem description

## Part 1  

## Part 2  

"""


import sys


infile = sys.argv[1] if len(sys.argv) >= 2 else "./inputs/5.in"

input = open(infile).read().strip()

fresh, ids = input.split("\n\n")
fresh = [tuple(map(int, f.split("-"))) for f in fresh.split()]
# print(fresh)

ids = [int(id) for id in ids.split()]
print(ids)

p1 = 0
for id in ids:
    is_fresh = False

    for f in fresh:
        if id >= f[0] and id <= f[1]:
            is_fresh = True
            break

    if is_fresh:
        p1 += 1

print(f"{'Solution to Part 1:':<20} {p1}")
# print(f"{'Solution to Part 2:':<20} {p2}")
