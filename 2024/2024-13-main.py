import sys

infile = sys.argv[1] if len(sys.argv)>=2 else './data/13.in'

raw = open(infile).read().strip().split("\n\n")

# Parse raw data; result is nested lists whose elements are direction of first joystick, second joystick, and prize location
data = []
for r in raw:
    temp = []
    for rr in r.split("\n"):
        temp1 = []
        if rr.split()[0] == 'Button':
            for rrr in rr.split(','):
                temp1.append(int(rrr.split('+')[-1]))
        else:
            for rrr in rr. split(','):
                temp1.append(int(rrr.split('=')[-1]))

        temp.append(tuple(temp1))

    data.append(temp)

#print(data)
print(data[0])


def compute_cost(data: list, shift: int):
    
    cost = 0

    for d in data:

        A, B, P = d[0], d[1], [shift + el for el in d[2]]

        #print(f"{A} {B} {P}")

        # Obtained via some algebra
        numA = B[1] * P[0] - B[0] * P[1]
        numB = A[0] * P[1] - A[1] * P[0]
        den = A[0] * B[1] - A[1] * B[0]

        nA = numA/den
        nB = numB/den

        #print(f"nA:  {nA}")
        #print(f"nB:  {nB}")
        
        # Prize is reachable if both nA and nB are integers
        is_int_soln = (int(nA) == nA) and (int(nB) == nB)

        if is_int_soln:
            cost += 3 * int(nA) + int(nB)

    return cost



print(f"{'Solution to Part 1:':<20} {compute_cost(data.copy(), 0)}")

print(f"{'Solution to Part 2:':<20} {compute_cost(data.copy(), 10000000000000)}")
