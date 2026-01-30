"""
Alternative solution to 2025.3
Use smarter searching to identify next digit.
i.e.  Next digits is largest in window where enough digits remain to construct the desired output length.
ex.   The most significant digit of the solution cannot be towards the right of the input string as there are not enough digits to the right to construct a satisfactory solution.
"""

import sys

infile = sys.argv[1] if len(sys.argv) >= 2 else "./inputs/3.in"

inputs = open(infile).read().strip().split('\n')
print(f"\nPuzzle inputs:\n{inputs}")


def solve(digits, target_length):
    """Monkey"""

    num_digits = len(digits)
    ans = []
    
    id_1 = 0

    while len(ans) < target_length:
        id_2 = num_digits - target_length + len(ans) + 1

        #print(f"Window indices:  {id_1}  {id_2}")

        choices = digits[id_1:id_2]
        largest = max(choices)

        id_max = choices.index(largest)

        ans.append(largest)

        id_1 += id_max + 1

    return int(''.join(map(str, ans)))  # recast from int list to int


def run(inputs, target_length):
    """Runner to execute solutions for both Parts 1 and 2."""

    print(f"\n\n*** Solving lengths of {target_length} ***")
    
    best = {}  # save input/solution pairs in a dictionary

    for input in inputs:

        print(f"\nProcessing input:  {input}")
        digits = [int(i) for i in input]  # convert to list of ints for >/< functionality

        best[input] = solve(digits, target_length)
    
    print("\n*** Individual input solutions ***")
    for k, v in best.items():
        print(f"{k}  ---->  {v}")

    return sum(best.values())


p1 = run(inputs, target_length=2)
print(f"\n*** Solution to Part 1 ***\n{p1}")

p2 = run(inputs, target_length=12)
print(f"\n*** Solution to Part 2 ***\n{p2}")

        
    
