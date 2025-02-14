import sys

infile = sys.argv[1] if len(sys.argv)>=2 else './data/19.in'

raw = open(infile).read().strip()

pieces, whole = raw.split('\n\n')

pieces = [p.strip() for p in pieces.split(',')]
#print(pieces)

whole = whole.split('\n')
#print(whole)

answers = {}

def solve(partials: list, word: str):
    
    #print(f"\nSolve called with: {partials}")

    temp = ''.join(partials)
    if temp == word:
        answers[word].append(partials)
        return True
    
    if len(temp) > len(word):
        return False
    
    char = len(partials)

    for p in pieces:
        #print(f"Checking {p}")
        test = ''.join(partials) + p
        #print(f"Fragment so far:  {test}")
        if word[:len(test)] == test:
            new = partials.copy()
            new.append(p)
            #print(f"Matches.  Calling solve with: {new}")
            #print(new)
            solve(new, word)
        

    return False


print(f"\n*** Beginning Part 1 ***\n")
for w in whole:
    print(f"\nSolving for:  {w}")
    answers[w] = []

    a = []
    solve(a, w)

ct = 0
for k, v in answers.items():
    print(f"{k}:  {v}")
    if len(v) > 0:
        ct += 1

print(f"\n{'Solution to Part 1:':<20} {ct}")
#print(f"{'Solution to Part 2:':<20} {p2}")
