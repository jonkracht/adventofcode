"""
# Problem description

## Part 1  
Count the numbers in a given list which fall within a given list of number ranges.

## Part 2  
Compress the list of number ranges so that there is no overlap between them.

"""


import sys


infile = sys.argv[1] if len(sys.argv) >= 2 else "./inputs/5.in"

input = open(infile).read().strip()

fresh, ids = input.split("\n\n")
fresh = [list(map(int, f.split("-"))) for f in fresh.split()]
print(f"\nFresh list:\n{fresh}")

ids = [int(id) for id in ids.split()]
print(f"\nID numbers:\n{ids}")

p1 = 0
for id in ids:
    is_fresh = False

    for f in fresh:
        if id >= f[0] and id <= f[1]:
            is_fresh = True
            break

    if is_fresh:
        p1 += 1

print(f"\n{'Solution to Part 1:':<20} {p1}")


# Part 2


def combine(ids: list) -> list:
    """"""
    # print(f"\nCombine call with list of length {len(ids)}")

    for i, id1 in enumerate(ids):
        # print(id1)
        for j, id2 in enumerate(ids):
            if j > i:
                # Range lies entirely within another
                if id2[0] <= id1[0] <= id2[1] and id2[0] <= id1[1] <= id2[1]:
                    del ids[i]
                    # print(f"{id1} lies within {id2}")
                    return ids
                # Range completely covers another
                elif id1[0] <= id2[0] and id1[1] >= id2[1]:
                    del ids[j]
                    return ids
                # Half overlaps
                elif id1[0] <= id2[0] and id2[0] <= id1[1] <= id2[1]:
                    ids[j][0] = id1[0]
                    del ids[i]
                    return ids
                elif id2[0] <= id1[0] <= id2[1] and id1[1] >= id2[1]:
                    ids[j][1] = id1[1]
                    del ids[i]
                    return ids

    return ids


print("\n\nBeginning Part 2:")
while True:
    start_length = len(fresh)
    print(f"Current number of intervals:  {start_length}")

    combined = combine(fresh)

    if len(combined) == start_length:
        break
    fresh = combined

print(f"\nCompressed ranges:")
for c in sorted(combined):
    print(c)

print(f"\nLength of final combined list:  {len(combined)}")

p2 = 0
for id in combined:
    p2 += id[1] - id[0] + 1

print(f"\n{'Solution to Part 2:':<20} {p2}")
