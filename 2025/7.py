"""
# Problem description

## Part 1  
Traverse a "maze" top-to-bottom.  When an obstacle is encountered, split.  Count how many total times a split occurs over the course of traveling the maze.


## Part 2  
Count how many distinct paths can be taken from the top of the maze to the bottom.

"""


import sys

infile = sys.argv[1] if len(sys.argv) >= 2 else "./inputs/7.in"
input = open(infile).read().strip().split("\n")
# print(input)

# Find index of 'S' character, indicating the start location in the first row of the input
start = input[0].index("S")

print(f"S is found at index:  {start}")

locs = []
locs.append({start})

splits = 0

for i, row in enumerate(input):
    if i > 0:
        temp = set()
        for loc in locs[i - 1]:
            if row[loc] == ".":
                temp.add(loc)
            elif row[loc] == "^":  # split
                splits += 1
                temp.add(loc - 1)
                temp.add(loc + 1)
            else:
                raise ValueError(f"Unexpected value:  {row[loc]}")

        locs.append(temp)

print(f"{'Solution to Part 1:':<20} {splits}")


# Part 2 solution

# Create a nested dictionary
nodes = {}

for i, row in enumerate(input):

    print(f"\n** Processing row {i} **")

    subnodes = {}
    if i == 0:
        subnodes[start] = 1

    else:
        for pt, ct in nodes[i - 1].items():
            char = row[pt]

            # Determine points to add
            if char == ".":
                temp = [(pt, ct)]

            elif char == "^":
                temp = [(pt - 1, ct), (pt + 1, ct)]

            else:
                raise ValueError(f"Unexpected value {char}")

            # Add to dictionary
            for k, v in temp:
                if k in subnodes.keys():
                    subnodes[k] += v
                else:
                    subnodes[k] = v

    nodes[i] = subnodes

# Print results
for k, v in nodes.items():
    print(f"{k}:  {v}")

p2 = sum(nodes[len(input) - 1].values())
print(f"\n{'Solution to Part 2:':<20} {p2}")
