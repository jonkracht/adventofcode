import sys, copy

infile = sys.argv[1] if len(sys.argv)>=2 else './data/19.in'

raw = open(infile).read().strip()

pieces, whole = raw.split('\n\n')

pieces = [p.strip() for p in pieces.split(',')]
print(f"\nPieces:\n{pieces}")

whole = whole.split('\n')
print(f"\nWhole:\n{whole}")


def solve(state: list, goal: str, part_1: bool):
    """"""   
    print(f"{len(''.join(state))}  {len(answers[goal])}")

     # Truncate search to only find one solution
    if part_1 and len(answers[goal]) > 0:
        return False

    temp = ''.join(state)
    
    if len(temp) == len(goal):
        if temp == goal:
            if state in answers[goal]:
                print(state)
                input()
            else:
                answers[goal].append(state)
                print(temp)
                print(goal)
                print(state)
                #input()
            
            return True
        
        else:
            return False

    elif len(temp) > len(goal):
        return False

    for p in pieces:
        test = ''.join(state) + p
        if goal[:len(test)] == test:
            new = copy.deepcopy(state)
            new.append(p)
            solve(new, goal, part_1)
        

    return False


answers = {}

print(f"\n*** Beginning Part 1 ***\n")
for w in whole:
    print(f"\nSolving for:  {w}")
    answers[w] = []

    a = []
    solve(a, w, False)

ct = 0


print("\nCombinations to create words")
for k, v in answers.items():
    #print(f"{k}:  {v}")
    if len(v) > 0:
        ct += 1

print(f"\n{'Solution to Part 1:':<20} {ct}")
#print(f"{'Solution to Part 2:':<20} {p2}")
