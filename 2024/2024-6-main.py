import sys

infile = sys.argv[1] if len(sys.argv) >= 2 else './data/6.in'
data = open(infile).read().strip().split()

ROWS, COLS = len(data), len(data[0])

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # motions

# Find starting point i.e. location of '^'
sr, sc = 0, 0
for row in range(ROWS):
    for col in range(COLS):
        if data[row][col] == "^":
            sr, sc = row, col

# Part 1:
r, c, dd = sr, sc, 0  # initial state
visited = set()  # seems computationally much more efficient to use sets rather than lists

while True:
    visited.add((r, c))

    # Compute candidate next location
    rr, cc = r + d[dd][0], c + d[dd][1]

    if not (0 <= rr < ROWS and 0 <= cc < COLS):
        print("Exiting map")
        break

    # If obstacle is encountered, simply change direction (don't take a step in new direction)
    if data[rr][cc] == "#":
        dd += 1
        if dd > 3:
            dd = 0
    else:
        r, c = rr, cc

p1 = len(visited)

# Part 2:  Determine which obstacle locations would cause looping
loops = set()

for i in range(ROWS):
    for j in range(ROWS):
        # print(f"({i},{j})")  # Monitor progress

        # Know original layout does not cause looping so skip
        if data[i][j] == "#":
            continue

        r, c, dd = sr, sc, 0  # initial state
        visited = set()

        while True:
            if (r, c, dd) in visited:
                #print("Looping.")
                loops.add((i, j))
                break

            visited.add((r, c, dd)) # need to include motion direction

            # Compute candidate next location
            rr, cc = r + d[dd][0], c + d[dd][1]

            if not (0 <= rr < ROWS and 0 <= cc < COLS):
                #print("Exiting map")
                break

            # If obstacle is encountered, simply change direction (don't take a step in new direction)
            if data[rr][cc] == "#" or (rr == i and cc == j):
                dd += 1
                if dd > 3:
                    dd = 0
            else:
                r, c = rr, cc

p2 = len(loops)

print(f"{'Solution to Part 1:':<20} {p1}")
print(f"{'Solution to Part 2:':<20} {p2}")
