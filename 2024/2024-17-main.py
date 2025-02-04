import sys
import numpy as np
from scipy.optimize import minimize
import itertools

infile = sys.argv[1] if len(sys.argv)>=2 else './data/17.in'

raw = open(infile).read().split("\n")

# Parse input
data = [r for r in raw if r != ""]
registers = data[0:3]

register = []
for r in registers:
    register.append(int(r.split(": ")[1]))

print(f"\nInitial register:  {register}")

program = []
for d in data[3].split(": ")[1].split(","):
    program.append(int(d))

print(f"Program:  {program}")


def update(inst: tuple, reg: tuple):
    """Perform operations and return updated registers and output."""

    #print(f"Inside function:  {inst}")

    code, operand = inst
    a, b, c = reg

    output, pointer = "", ""

    # Handle non-literal operand values
    combo = {0: 0, 1: 1, 2: 2, 3: 3, 4: a, 5: b, 6: c}

    if code == 0:
        a = int(a / (2 ** combo[operand]))

    elif code == 1:
        #b = b ^ operand  # problematic for large values
        b = np.bitwise_xor(b, operand)

    elif code == 2:
        b = combo[operand] % 8

    elif code == 3:
        if a != 0:
            pointer = operand

    elif code == 4:
        b = b ^ c

    elif code == 5:
        output = str(combo[operand] % 8)
        #print(output)

    elif code == 6:
        b = int(a / (2 ** combo[operand]))

    elif code == 7:
        c = int(a / (2 ** combo[operand]))

    else:
        print(f"Unexpected code:  {code}")
        return


    return (a, b, c), output, pointer


def run_program(prog, reg):
    """"""

    output = []
    p = 0  # pointer indication location in program list

    while True:

        if p >= len(prog):
            break

        #print(f"\np = {p}, program:  ({prog[p]}, {prog[p + 1]}), register = {reg}, output:  {output}")

        reg, out, pointer = update((prog[p], prog[p + 1]), reg)
    
        if out != "":
            output.append(out)

        if pointer  == "":
            p += 2
        else:
            p = pointer

        #input()

    return output


# Part 1:  Determine output for given program and register state
p1 = ','.join(run_program(program, register))
print(f"\n{'Solution to Part 1:':<20}\n{p1}")





# Part 2:  Find starting value of register A whose output is identical to the program

#a = 100000000200000  # starting point
#a = 100000007000000  # ran til around




'''
## Optimization
def compute_error(a):

    output = run_program(program, (int(a), 0, 0))

    error = 0
    for o, p in itertools.zip_longest(output, program, fillvalue=0):
        error += (int(o) - int(p)) ** 2

    return error


#a0 = 100000007000000
a0 = 10000000000000
res = minimize(compute_error, a0, method='nelder-mead',
               options={'xatol': 1e-8, 'disp': True})

print(res.x)

'''



## Brute force search
#a = 16316996450914
#a = 100000
a = 1

m = {}

while True:
    a += 1

    output = [int(r) for r in run_program(program, (a, 0, 0))]

    #print(f"a = {a}:  {output}")
    #print(f"             {program}")

    m[a] = int(''.join([str(o) for o in output]))

    if output == program or a == 100000:
        break

for k, v in m.items():
    print(f"{k}:  {v}")

#print(f"\nSolution is: {a}")




#print(program)
#print(run_program(program, (117440, 0, 0)))

#print(f"{'Solution to Part 2:':<20} {a}")
