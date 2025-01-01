import sys

infile = sys.argv[1] if len(sys.argv)>=2 else './data/10.in'

raw = open(infile).read().strip().split('\n')

data = []
for r in raw:
    data.append([int(x) for x in r])


rows = len(data)
cols = len(data[0])


def find_next(data, i, j):
    """Recursive function to identified candidate next path locations"""

    # Base case:  save trail endpoint to a list/set
    if data[i][j] == 9:
        #print(f"{i=}, {j=}")
        p1_visited.add((i, j))
        p2_visited.append((i, j))

    # Check left
    if 0 <= j - 1 < len(data[0]):
        if data[i][j - 1] == data[i][j] + 1:
            if find_next(data.copy(), i, j - 1):
                return True

    # Check right
    if 0 <= j + 1 < len(data[0]):
        if data[i][j + 1] == data[i][j] + 1:
            if find_next(data.copy(), i, j + 1):
                return True

    # Check down
    if 0 <= i + 1 < len(data):
        if data[i + 1][j] == data[i][j] + 1:
            if find_next(data.copy(), i + 1, j):
                return True
    # Check up
    if 0 <= i - 1 < len(data):
        if data[i - 1][j] == data[i][j] + 1:
            if find_next(data.copy(), i - 1, j):
                return True

    return



p1_score = 0
p1_visited = set()  # Part 1 is path independent so set is fine 
p2_visited = []  # Part 2 requires a list where path are treated individually

for r in range(rows):
    for c in range(cols):
        if data[r][c] == 0:

            p1_visited.clear()
            
            find_next(data.copy(), r, c)
            
            p1_score += len(p1_visited)
                                

print(f"{'Solution to Part 1:':<20} {p1_score}")

p2_score = len(p2_visited)
print(f"{'Solution to Part 2:':<20} {p2_score}")
