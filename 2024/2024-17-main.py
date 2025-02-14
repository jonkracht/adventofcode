import sys
import numpy as np

infile = sys.argv[1] if len(sys.argv)>=2 else './data/17.in'
raw = open(infile).read().split("\n")

# Parse input
data = [r for r in raw if r != ""]
registers = data[0:3]

register = []
for r in registers:
    register.append(int(r.split(": ")[1]))

print("\n\n*** Part 1 ***")
print(f"\nInitial register:  {register}")

program = []
for d in data[3].split(": ")[1].split(","):
    program.append(int(d))

print(f"Program:  {program}")


def update(inst: tuple, reg: tuple):
    """Perform operations and return updated registers, output, and pointer."""

    code, operand = inst
    a, b, c = reg

    output, pointer = "", ""

    # Handle combo operands
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
        #b = b ^ c
        b = np.bitwise_xor(b, c)

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
    """Execute the program."""

    output = []
    p = 0  # pointer indication location in program list

    while True:
        if p >= len(prog):  # stop when pointer reaches end
            break

        reg, out, pointer = update((prog[p], prog[p + 1]), reg)
    
        if out != "":  # exclude trivial output
            output.append(out)

        if pointer  == "":
            p += 2
        else:
            p = pointer

    return output


# Part 1:  Determine output for given program and inital register
p1 = ','.join(run_program(program, register))
print(f"\n{'Solution to Part 1:':<20}\n{p1}")



# Part 2:  Find starting value of register A that produces output identical to the program
print("\n\n*** Beginning Part 2 ***\n")


'''
Method 1:  Brute force search
* Looking at printed output for small values of A, recognized number of digits printed increased when a new power of 8 was crossed
* For the output to match the 16-digit input, initial register must be between 8^15 and 8^16.
* Used a brute force method to find regions where matched the first few most significant digits.
* Initially used large step to quick sample region
* As additional digits align, reduce step size.
* Luckily, eventually stumbled upon solution.
'''

'''
a = 8**15
step = 1  # begin large until right-most digits match and reduce/hope 

while True:

    print(f"\na = {a}")

    output = [int(r) for r in run_program(program, (a, 0, 0))]
    
    print(program)
    print(output)
    
    # Save output in a dictionary

    if output == program:
        break

    a += step
'''

'''
Method 2:  Solve using octal representation and recursive search
* Observe that last digit output (right-most) is determined only by left-most digit in the octal representation of A
* Match the digit(s)
* Proceed to next digit and find possible matches.
* Repeat.
'''

# Others' program inputs:
#program = [2,4,1,2,7,5,4,1,1,3,5,5,0,3,3,0]  # solution:  37221261688308
#program = [2,4,1,7,7,5,0,3,4,4,1,7,5,5,3,0]  # solution:  267265166222235
#program = [2,4,1,2,7,5,4,5,1,3,5,5,0,3,3,0]  # solution:  37221270076916
#program = [2,4,1,2,7,5,0,3,1,7,4,1,5,5,3,0]  # solution:  190615597431823


def solve(seq: str):
    """Recursive solver"""

    digit = -(len(seq) + 1)  # determine which digit is being solved for

    if len(seq) == len(program): # add sequence to solution list if appropriate length
        solutions.append(seq)
        return True

    for n in range(8):
        new_seq = seq + str(n)

        # Convert candidate new sequence to base 10 and execute program excluding recursion step (3, 0)
        output = int(run_program(program[:-2], (int(new_seq, 8), 0, 0))[0])
        
        if output == program[digit]:
            solve(new_seq)

    return False


solutions = []
solve('')

# Display solutions
d = dict((s, int(s, 8)) for s in solutions)

print(f"{len(d)} solutions found.")
print(f"\n{40*'-'}\n{'Octal':<20}Decimal\n{40*'-'}")
for k, v in d.items():
    print(f"{k:<20}{v}")

print(f"\n*** Part 2 answer ***\nMinimum value is:")
min_val = min(d.keys())
print(f"{min_val} (oct)")
print(f"{d[min_val]}  (dec)")

'''
# Double check a value
val = 110475839891866
print(f"\nProgram is:\n{program}")
print(f"\nChecking {val}.  Output is:")
print([int(s) for s in run_program(program, (val, 0, 0))])
'''
