import sys

infile = sys.argv[1] if len(sys.argv) >= 2 else "./inputs/2.in"

input = open(infile).read().strip()
# print(input)

ranges = [[int(x) for x in i.split("-")] for i in input.split(",")]


def p1_valid(n: int):
    """Part 1:  Determine if a number is "symmetric"."""

    n_str = str(n)
    if len(n_str) % 2 != 0:  # odd number of digits cannot be symmetric
        return True
    else:
        if 2 * n_str[0 : int(len(n_str) / 2)] == n_str:
            return False
        else:
            return True


def p2_valid(n: int):
    """Part 2:  Determine if number can be created by repeating a smaller number some integer number of times."""

    n_str = str(n)
    l_str = len(n_str)

    for l in range(1, l_str // 2 + 1):
        if l_str % l == 0:
            if int(l_str / l) * n_str[0:l] == n_str:
                return False

    return True


d1, d2 = {}, {}  # dynamic programming dictionaries containing number validities
not_valid_1, not_valid_2 = [], []

# Iterate of input number ranges
for r in ranges:

    # print("\nRange:  " + str(r))

    assert (
        r[1] >= r[0]
    ), "Second element in range should be greater than or equal to first."

    for rr in range(r[0], r[1] + 1):

        # Check unseen states
        if rr not in d1.keys():
            d1[rr] = p1_valid(rr)
        if rr not in d2.keys():
            d2[rr] = p2_valid(rr)

        if d1[rr] == False:
            # print(f"Adding {rr} to invalid.")
            not_valid_1.append(rr)

        if d2[rr] == False:
            not_valid_2.append(rr)

p1 = sum(not_valid_1)
p2 = sum(not_valid_2)

print(f"\n{'Solution to Part 1:':<20} {p1}")
print(f"\n{'Solution to Part 2:':<20} {p2}")
