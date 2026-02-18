"""
# Problem description

## Part 1  

## Part 2  

"""


import sys

infile = sys.argv[1] if len(sys.argv) >= 2 else "./inputs/6.in2"
input = open(infile).read().strip().split("\n")

vals, ops = input[:-1], input[-1].split()
# print(ops)

vals = [list(map(int, v.split())) for v in vals]
# print(vals)

num_vals = len(vals)
num_ops = len(ops)

p1 = 0
for i in range(num_ops):
    if ops[i] == "+":
        temp = 0
        for ii in range(num_vals):
            temp += vals[ii][i]

    elif ops[i] == "*":
        temp = 1
        for ii in range(num_vals):
            temp *= vals[ii][i]

    else:
        raise ValueError(f"Unexpected operation:  {ops[i]}")

    p1 += temp


print(f"{'Solution to Part 1:':<20} {p1}")

print(input)


## Part Two
v2 = input[:-1]
o2 = input[-1]

print("Check that all inputs are the same length:")
for v in v2:
    print(len(v))

n_rows = len(v2)
n_cols = len(v2[0])


id, p2, last_break = 0, 0, 0

while id < n_cols:
    # Find next break in values

    all_blank = True
    for r in range(n_rows):
        if v2[r][id] != " ":
            all_blank = False
            break

    if all_blank or id == n_cols:

        print(f"\nFound all blanks at id:  {id}\n")

        # Determine L2R numbers
        vals = []
        for ii in range(id - 1, last_break - 1, -1):

            print(f"Examining characters at {ii}")
            val = ""
            for r in range(n_rows):
                print(f"Examining locations {r} where value is: {v2[r][ii]}")

                print(type(v2[r][ii]))
                val += v2[r][ii]
                print(val)

            vals.append(int(val))

        print(f"Finished processing block:\n{vals}")

        # Perform computation
        print(f"\nLast break:  {last_break}")
        if o2[last_break] == "+":
            p2 += sum(vals)

        elif o2[last_break] == "*":
            prod = 1
            for val in vals:
                prod *= val

            p2 += prod

        else:
            raise ValueError(f"Unexpected value:  {ops[last_break]}")

        print(f"\n\nCurrent value of p2:  {p2}")

        last_break = id + 1

    id += 1

print(f"{'Solution to Part 2:':<20} {p2}")
