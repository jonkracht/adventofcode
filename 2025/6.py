
'''
# Problem description

## Part 1  

## Part 2  

'''


import sys

infile = sys.argv[1] if len(sys.argv) >= 2 else "./inputs/6.in"
input = open(infile).read().strip().split('\n')

vals, ops = input[:-1], input[-1].split()
#print(ops)

vals = [list(map(int, v.split())) for v in vals]
#print(vals)

num_vals = len(vals)
num_ops = len(ops)

p1 = 0
for i in range(num_ops):
    if ops[i] == '+':
        temp = 0
        for ii in range(num_vals):
            temp += vals[ii][i]

    elif ops[i] == '*':
        temp = 1
        for ii in range(num_vals):
            temp *= vals[ii][i]

    else:
        raise ValueError(f"Unexpected operation:  {ops[i]}")
    
    p1 += temp


print(f"{'Solution to Part 1:':<20} {p1}")
# print(f"{'Solution to Part 2:':<20} {p2}")
