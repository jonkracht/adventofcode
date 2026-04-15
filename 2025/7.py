"""
# Problem description

## Part 1  
Traverse a "maze" top-to-bottom.  When an obstacle is encountered, split.  Count how many times a split occurs.


## Part 2  
Count how many distinct paths can be taken from the top of the maze to the bottom.

"""


import sys


infile = sys.argv[1] if len(sys.argv) >= 2 else "./inputs/7.in"
input = open(infile).read().strip().split("\n")
# print(input)

# Find index of 'S' (the starting location in first row)
start = input[0].index("S")
print(f"S is found at index:  {start}")

locs = []
locs.append({start})

splits = 0

for i, row in enumerate(input):
    if i > 0:
        temp = set()
        for l in locs[i - 1]:
            if row[l] == ".":
                temp.add(l)
            elif row[l] == "^":
                splits += 1
                temp.add(l - 1)
                temp.add(l + 1)
            else:
                raise ValueError(f"Unexpected value:  {row[l]}")

        locs.append(temp)

print(f"{'Solution to Part 1:':<20} {splits}")


## Part 2 solution

# print(f"{'Solution to Part 2:':<20} {p2}")
