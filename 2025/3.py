'''
# Problem description
## Part 1  
Find the largest two digit number that can be made from a string of digits preserving order.

Example:  
987654321111111 > 98
811111111111119 > 89

Naive solution:  Nested for loops.  Works for small number of digits but unwieldy.

## Part 2  
Look for largest 12-digit number in inputs.

Solution:  Construct a recursive function to sequentially add each digit, pruning candidates that yield smaller intermediate results.
'''

import sys

infile = sys.argv[1] if len(sys.argv) >= 2 else "./inputs/3.in"

inputs = open(infile).read().strip().split('\n')
#print(input)

def solve(current: str, choices: str, current_id: int, choice_id: int, target_length: int):
    """Recursive function to determine largest integer that can be constructed from 'input'."""

    #print(f"\nFunction call:\n{current}, {choices}, {current_id}, {choice_id}")  # debug function calls
    
    global best

    # Save value if greater than current best
    if current_id == target_length:
        val = int(current)
        if val > best:
            best = val
            return
        else:
            return

    # If reached end of input, return
    if choice_id == len(choices):
        return

    # Call function adding next candidate
    solve(current, choices, current_id, choice_id + 1, target_length)

    # Call function adding candidate if larger than current 'best'
    update = current[:current_id] + choices[choice_id] + '9' * (target_length - current_id - 1)
    
    if int(update) > best:
        solve(update, choices, current_id + 1, choice_id + 1, target_length)

    return


def run(inputs: list, target_length: int, output = False):
    """Runner."""

    global best

    best_dict = {}
    for input in inputs:
        best = 0
        solve(target_length * '9', input, 0, 0, target_length)
        best_dict[input] = best

        if output:
            for k, v in best_dict.items():
                print(f"{k}:            {v}")
    
    return best_dict

# Part 1    
print("\nPart 1:")
p1 = run(inputs, target_length=2, output=False)
print(f"\n{'Solution to Part 1:':<20} {sum(p1.values())}")

# Part 2
print("\nPart 2:")
p2 = run(inputs, target_length=12, output=False)
print(f"\n{'Solution to Part 2:':<20} {sum(p2.values())}")

