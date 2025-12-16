import sys

infile = sys.argv[1] if len(sys.argv) >= 2 else "./inputs/1.in2"

# List comprehension remove empty list elements
input = [i for i in open(infile).read().split("\n") if i]

# print(input)
# print(len(input))

loc = 50  # starting location
dial_positions = 100
s = 10

p1, p2 = 0, 0

for i in input:
    if i[0] == "L":
        c = -1
    elif i[0] == "R":
        c = 1
    else:
        raise ValueError(f"Unexpected input:  {i}")

    temp = loc + c * int(i[1:])
    new_loc = temp % dial_positions

    if new_loc == 0:
        p1 += 1

    print(f"{loc:<{s}}{i:<{s}}{temp:<{s}}{new_loc:<{s}}{p1}")

    loc = new_loc

print(f"\n{'Solution to Part 1:':<20} {p1}")
print(f"{'Solution to Part 2:':<20} {p2}")
