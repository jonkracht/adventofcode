import sys, copy
import time

infile = sys.argv[1] if len(sys.argv)>=2 else './data/15.in'

raw = open(infile).read().strip()

# Parse data
warehouse, moves = raw.split("\n\n")

moves = [m for m in moves if m != "\n"]
warehouse = [[ww for ww in list(w)] for w in warehouse.split('\n')]

# Find starting robot location
for i, w in enumerate(warehouse):
    for j, ww in enumerate(w):
        if ww == "@":
            start = (i, j)


def make_move_p1(move, wh, loc):
    """Update warehouse based on next move"""
    
    # Convert arrow character into vector
    vectors = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
    dir = vectors[move]

    next_loc = (loc[0] + dir[0], loc[1] + dir[1])
    char = wh[next_loc[0]][next_loc[1]]

    if char == ".":  # open space:  move robot there and set previous location to '.'
        wh[next_loc[0]][next_loc[1]] = "@"
        wh[loc[0]][loc[1]] = "."

        return wh, next_loc

    elif char == "O":  # box is encountered
        boxes = [next_loc]  # list of boxes to be moved in appropriate direction

        while True:
            # Compute candidate next location/character
            next_loc = (boxes[-1][0] + dir[0], boxes[-1][1] + dir[1])
            next_char = wh[next_loc[0]][next_loc[1]]

            if next_char == ".":  # Empty space at end of boxes - move them and robot
                wh[loc[0]][loc[1]] = "."
                wh[next_loc[0]][next_loc[1]] = "O"
                
                loc = boxes[0]
                wh[loc[0]][loc[1]] = "@"

                return wh, loc

            elif next_char == "O":
                # Add box to list of things to be moved
                boxes.append((next_loc))

            elif next_char == "#":  # wall encountered - do nothing
                return wh, loc

    elif char == "#":  # wall encountered - do nothing
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
    warehouse1, robot_loc = make_move_p1(m, warehouse1, robot_loc)

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


def make_move_p2(move, wh, loc):
    """Update warehouse for widened warehouse in Part 2."""
    
    # Convert arrow character into vector
    vectors = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
    dir = vectors[move]

    next_loc = (loc[0] + dir[0], loc[1] + dir[1])
    next_char = wh[next_loc[0]][next_loc[1]]

    print(f"Robot at {loc}.  Move direction is {move} ({dir}) where character is '{next_char}'.")

    if next_char == ".":
        print("Empty space.  Moving into it and updating warehouse.")
        #print(loc)
        #print(next_loc)
        wh[next_loc[0]][next_loc[1]] = "@"
        wh[loc[0]][loc[1]] = '.'
        return wh, next_loc

    if next_char == "#":
        print("Hit a wall.  Doing nothing.")
        return wh, loc

    boxes_to_move = set()
    
    # Hit one or more boxes.  Handle horizontal and vertical moves separately.
    if dir[0] == 0:  # horizontal move - only lines of boxes move
        if next_char == "[":
            boxes_to_move.add(next_loc)
        elif next_char == "]":
            boxes_to_move.add((next_loc[0], next_loc[1] - 1))
            next_loc = (next_loc[0], next_loc[1] - 1)
        else:
            print(f"Unexpected character:  {next_char}")
            return
       
        print(f"Initialized boxes_to_move:  {boxes_to_move}")
        while True:

            next_loc = (next_loc[0] + dir[0], next_loc[1] + 1 * dir[1])
            next_char = wh[next_loc[0]][next_loc[1]]

            if next_char == "#":
                print("Hit a wall. Do nothing.")
                return wh, loc

            elif next_char == "[":
                boxes_to_move.add(next_loc)

            elif next_char == ".":
                print(f"Moving boxes:  {boxes_to_move}")
                for box in boxes_to_move:
                    wh[box[0]][box[1] + dir[1]] = "[" 
                    wh[box[0]][box[1] + dir[1] + 1]  = "]" 

                wh[loc[0] + dir[0]][loc[1] + dir[1]] = "@"
                wh[loc[0]][loc[1]] = "."

                return wh, (loc[0] + dir[0], loc[1] + dir[1])


    # Vertical moves - clusters of blocks may need to be moved. 
    elif dir[1] == 0:
        #print("Moving vertically")
        if next_char == "[":
            boxes_to_move.add(next_loc)
            const = 1
        elif next_char == "]":
            boxes_to_move.add((next_loc[0], next_loc[1] - 1))
            const = -1
        else:
            print(f"Unexpected character: {next_char}")
            return

        print(f"Initialized boxes_to_move:  {boxes_to_move}")

        all_boxes = set()
        
        while True:
            #print(f"All boxes:  {boxes_to_move}")
            canMove = True
            next_boxes = set()
            
            for box in boxes_to_move:
                #print(box)
                
                next_boxes.add(box)
                
                # For each box, check two points it touches
                check1 = (box[0] + dir[0], box[1] + dir[1])
                check2 = (box[0] + dir[0], box[1] + dir[1] + 1)

                char1 = wh[check1[0]][check1[1]]
                char2 = wh[check2[0]][check2[1]]

                #print(f"\nBox {box}: check 1:  {check1}, check 2: {check2}")
                #print(f"\nchar 1:  {char1}, char 2: {char2}")

                if (char1 == "#") or (char2 == "#"):
                    print("Hit a wall.  Stopping")
                    return wh, loc 
                if char1 == "[":
                    if check1 not in all_boxes:
                        canMove = False
                    next_boxes.add(check1)
                if char1 == "]":
                    temp = (check1[0], check1[1] - 1)
                    if temp not in all_boxes:
                        canMove = False
                    next_boxes.add(temp)
                if char2 == "[":
                    if check2 not in all_boxes:
                        canMove = False
                    next_boxes.add(check2)
                    
            boxes_to_move = next_boxes

            for n in next_boxes:
                all_boxes.add(n)
           
            # If no obstacle is found:
            if canMove:
                #print(f"Moving boxes: {all_boxes}") 
                # Remove boxes and later add them in at their new locations 
                for n in all_boxes:
                    wh[n[0]][n[1]] = "." 
                    wh[n[0]][n[1] + 1] = "."

                wh[loc[0]][loc[1]] = "." 
                
                for n in all_boxes:
                    wh[n[0] + dir[0]][n[1]] = "[" 
                    wh[n[0] + dir[0]][n[1] + 1] = "]"

                     
                wh[loc[0] + dir[0]][loc[1] + dir[1]] = "@" 
                    

                return wh, (loc[0] + dir[0], loc[1] + dir[1])
                


        return wh, loc

'''

warehouse2 = widen_warehouse(copy.deepcopy(warehouse))
print("\nInitial configuration:")
print('\n'.join([''.join(w) for w in warehouse2]))  # print warehouse

# Find starting robot location
for i, w in enumerate(warehouse2):
    for j, ww in enumerate(w):
        if ww == "@":
            start2 = (i, j)

robot_loc = start2

for i, m in enumerate(moves[:]):
    print(f"\nMove {i}:")
    warehouse2, robot_loc = make_move_p2(moves[i], copy.deepcopy(warehouse2), robot_loc)
    
    print('\n'.join([''.join(w) for w in warehouse2]))  # print warehouse
    
    input("")  # press enter to display next
    #time.sleep(0.25)
    
gps2 = compute_gps(warehouse2.copy(), '[')
print(f"\n{'Solution to Part 2:':<20} {gps2}")

'''


# Part 2 revisited:  Use a recursive function to identify block chunks
def able_to_move(move, wh, loc):
    """Checks if motion is possible in a given direction."""

    next_loc = (loc[0] + move[0], loc[1] + move[1])
    next_char = wh[next_loc[0]][next_loc[1]]

    if next_char == ".":
        return True
    
    elif next_char == "#":
        return False
    
    elif next_char == "[":
        to_move.add((next_loc, next_char))
        to_move.add(((next_loc[0], next_loc[1] + 1), "]"))

        if move[0] == 0:  # horizontal move
            return able_to_move(move, wh, (next_loc[0], next_loc[1] + 1))

        else:  # vertical move
            return able_to_move(move, wh, next_loc) and \
                    able_to_move(move, wh, (next_loc[0], next_loc[1] + 1))
    
    elif next_char == "]":
        to_move.add((next_loc, next_char))
        to_move.add(((next_loc[0], next_loc[1] - 1), "["))

        if move[0] == 0:  # horizontal move
            return able_to_move(move, wh, (next_loc[0], next_loc[1] - 1))

        else:  # vertical move
            return able_to_move(move, wh, next_loc) and able_to_move(move, wh, (next_loc[0], next_loc[1] - 1))

    else:
        print(f"Unexpected character:  {next_char}")
        return



warehouse3 = widen_warehouse(copy.deepcopy(warehouse))
vectors = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

print("Initial warehouse configuration:")
print('\n'.join([''.join(w) for w in warehouse3]))  # print warehouse

for i, w in enumerate(warehouse3):
    for ii, ww in enumerate(w):
        if ww == "@":
            robot_loc = (i, ii)

for i, arrow in enumerate(moves[:]):
    print(f"\nMove {i}:  '{arrow}'.  Robot location:  {robot_loc}.") 
    
    # Convert arrow character into vector
    move = vectors[arrow]

    to_move = set()
    to_move.add((robot_loc, "@"))

    if able_to_move(move, warehouse3, robot_loc):
        print(f"Motion can be performed.  Moving {len(to_move)} items:  {to_move}")
       
        # Blank spaces previously occupied by boxes and robot
        for t in to_move:
            #print(t)
            warehouse3[t[0][0]][t[0][1]] = "."

        
        for t in to_move:
            warehouse3[t[0][0] + move[0]][t[0][1] + move[1]] = t[1]
        
        robot_loc = (robot_loc[0] + move[0], robot_loc[1] + move[1])
        warehouse3[robot_loc[0]][robot_loc[1]] = "@"
    
    else:
        print("Hit a wall.  Doing nothing")

    print('\n'.join([''.join(w) for w in warehouse3]))  # print warehouse
    input("\n(Enter to continue)")


    
gps2 = compute_gps(warehouse3.copy(), '[')
print(f"\n{'Solution to Part 2:':<20} {gps2}")





