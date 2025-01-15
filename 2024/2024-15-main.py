import sys, copy
infile = sys.argv[1] if len(sys.argv)>=2 else './data/15.in'

raw = open(infile).read().strip()

# Parse data
warehouse, moves = raw.split("\n\n")

moves = [m for m in moves if m != "\n"]
warehouse = [[ww for ww in list(w)] for w in warehouse.split('\n')]


# Find starting location
for i, w in enumerate(warehouse):
    for j, ww in enumerate(w):
        if ww == "@":
            start = (i, j)


def make_move(move, wh, loc):
    """"""
    
    # Convert arrow character into vector
    vectors = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
    
    dir = vectors[move]

    next_loc = (loc[0] + dir[0], loc[1] + dir[1])
    char = wh[next_loc[0]][next_loc[1]]

    if char == ".":  # open space - switch robot and open space
        wh[next_loc[0]][next_loc[1]] = "@"
        wh[loc[0]][loc[1]] = "."

        return wh, next_loc

    elif char == "O":
        
        boxes = [next_loc]

        while True:
            next_loc = (boxes[-1][0] + dir[0], boxes[-1][1] + dir[1])

            next_char = wh[next_loc[0]][next_loc[1]]

            if next_char == ".":
                # Update warehouse
                wh[loc[0]][loc[1]] = "."
                wh[next_loc[0]][next_loc[1]] = "O"
                
                loc = boxes[0]
                wh[loc[0]][loc[1]] = "@"

                return wh, loc

            elif next_char == "O":
                # Add box to list of things to be moved
                boxes.append((next_loc))

            elif next_char == "#":
                # If a wall is eventually encountered, do nothing
                return wh, loc



    elif char == "#":  # wall encountered - do nothing and return 
        return wh, loc

    else:
        print(f"Unexpected character:  {char}")
        return 



def compute_gps(wh: list, char: str):
    """Compute gps score - pass "O" for Part 1 and "[" for Part 2."""
    
    gps = 0
    for i, w in enumerate(wh):
        for ii, ww in enumerate(w):
            if ww == char:
                gps += 100 * i + ii

    return gps

warehouse1 = copy.deepcopy(warehouse)
robot_loc = start


for m in moves:
    warehouse1, robot_loc = make_move(m, warehouse1, robot_loc)

gps1 = compute_gps(warehouse1, "O")

print(f"{'Solution to Part 1:':<20} {gps1}")





## Part 2

def widen_warehouse(warehose):
    """Widen warehouse by replacing one character with two specified"""
    
    d = {"#": 2 * ["#"], "O": ["["] + ["]"], ".": 2 * ["."], "@": ["@"] + ["."]}
    
    n = []
    for w in warehouse:
        nn = []
        for ww in w:
            nn += d[ww]

        n.append(nn)

    return n


warehouse2 = widen_warehouse(warehouse)
#print('\n'.join([''.join(w) for w in warehouse2]))  # print warehouse

robot_loc = start

for m in moves:
    #warehouse2 = make_move_2()
    pass


gps2 = compute_gps(warehouse2, '[')

print(f"{'Solution to Part 2:':<20} {gps2}")
