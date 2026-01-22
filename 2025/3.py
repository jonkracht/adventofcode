'''
# Problem description
## Part 1  
Find the largest two digit number that can be made from a string of digits preserving order.

Example:  
987654321111111 > 98
811111111111119 > 89

## Part 2  
Increase number of digits to twelve.
'''



import sys


infile = sys.argv[1] if len(sys.argv) >= 2 else "./inputs/3.in"

inputs = open(infile).read().strip().split('\n')
#print(input)

joltages = []

for input in inputs:
    best = 0
    for i, val in enumerate(input):
        
        remainder = input[i+1:]

        if len(remainder) == 0:
            test = int(val)
        else:
            test = int(val + max(input[i+1:]))

        if test > best:
            best = test

    joltages.append(best)

print(joltages)
p1 = sum(joltages)

print(f"{'Solution to Part 1:':<20} {p1}")
# print(f"{'Solution to Part 2:':<20} {p2}")
