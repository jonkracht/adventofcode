"""
# Problem description

## Part 1  

Parse a block of text into columns of numbers where either addition or multiplication is performed.

## Part 2  
Numbers are now said to be written vertically.  Re-read from the text block and operations redone.

"""


import sys

infile = sys.argv[1] if len(sys.argv) >= 2 else "./inputs/6.in2"

input = open(infile).read()
print(input)

input = input.split("\n")[:-1]
# print(input)


# Observation:  Looks like operator symbol lines up with left-most column of each block
ops = input[-1]

# Find indices where operator symbols exist
ids = []
for i in range(len(ops)):
    if ops[i] != " ":
        ids.append(i)

# Include index of would-be next entry at list end
ids.append(len(input[1]) + 1)

p1_totals = []
for j in range(len(ids) - 1):
    op = ops[ids[j]]

    if op == "+":
        subtotal = 0
        for jj in range(len(input) - 1):
            subtotal += int(input[jj][ids[j] : ids[j + 1]])

    elif op == "*":
        subtotal = 1
        for jj in range(len(input) - 1):
            subtotal *= int(input[jj][ids[j] : ids[j + 1]])
    else:
        raise ValueError(f"Unexpected operator:  {op}")

    p1_totals.append(subtotal)


print(f"Subtotals for Part 1:\n{p1_totals}")

p1 = sum(p1_totals)
print(f"\nSolution to Part 1:  {p1}")


## Part 2:  Perform computation reading number vertically rather than horizontally

p2_totals = []
for j in range(len(ids) - 1):
    op = ops[ids[j]]
    vals = []
    for jj in range(ids[j], ids[j + 1] - 1):
        char = []
        for r in range(len(input) - 1):
            # print(f"({r}, {jj}):  {input[r][jj]}")
            char.append(input[r][jj])

        vals.append(int("".join(char)))

    if op == "+":
        p2_totals.append(sum(vals))
    elif op == "*":
        temp = 1
        for v in vals:
            temp *= v

        p2_totals.append(temp)

    else:
        raise ValueError("Shite")

print(f"\nSubtotals for Part 2:\n{p2_totals}")

p2 = sum(p2_totals)
print(f"\nSolution to Part 2:  {p2}")
