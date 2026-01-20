import sys

infile = sys.argv[1] if len(sys.argv) >= 2 else "./inputs/1.in"

# Remove empty list elements via list comprehension
input = [i for i in open(infile).read().split("\n") if i]

# print(input)
# print(len(input))

loc = 50  # starting dial position
n_locs = 100  # number of total dial positions

col_width = 10  # column width of output

p1, p2 = 0, 0

d = {"R": 1, "L": -1}

for i in input:

    direction = d[i[0]]  # determine move direction

    # Compute new location without determining modulo
    new_loc = loc + direction * int(i[1:])

    # Part 1:  If new_loc is a multiple of n_locs, increment counter
    if new_loc % n_locs == 0:
        p1 += 1

    # Part 2:  Examine intermediate locations as well via list comprehension
    p2 += sum(
        x % n_locs == 0 for x in range(loc + direction, new_loc + direction, direction)
    )  # exclude current location to avoid double counting

    # Output current state
    print(
        f"{loc:<{col_width}}{loc % n_locs:<{col_width}}{i:<{col_width}}{new_loc:<{col_width}}{p1:<{col_width}}{p2}"
    )

    loc = new_loc

print(f"\n{'Solution to Part 1:':<20} {p1}")
print(f"\n{'Solution to Part 2:':<20} {p2}")
