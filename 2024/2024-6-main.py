import sys

infile = sys.argv[1] if len(sys.argv)>=2 else './data/6.in'

raw = open(infile).read().strip()

raw = raw.split("\n")

data = []
for r in raw:
    data.append(list(r))

n_rows = len(data)
n_cols = len(data[0])

# Find starting state; assume direction is always up
for row in range(len(data)):
    if "^" in data[row]:
        starting_i, starting_j = row, data[row].index("^")

visited = []
visited.append(tuple((starting_i, starting_j)))

def next_state(data, state):
    '''Compute next state (position and orientation)'''
    
    # Compute candidate new location 
    i, j = state[0] + state[2][0], state[1] + state[2][1]
    
    # Check is border is reached
    if i < 0 or i > (n_rows - 1) or j < 0 or j > (n_cols - 1):
        return False
   
    # Check if obstacle has been reached
    if data[i][j] == "#":
        state[2] = next_dir(state[2])

    state[0] = state[0] + state[2][0]
    state[1] = state[1] + state[2][1]

    return state


def next_dir(motion):

    motions=[(-1, 0), (0, 1), (1, 0), (0, -1)]
    id = motions.index(motion)

    if id == 3:
        return motions[0]
    else:
        return motions[id + 1]


state = [starting_i, starting_j, (-1, 0)]

while True:
    state = next_state(data, state)
    
    if state == False:
        break

    loc_tuple = tuple((state[0], state[1]))
    if loc_tuple not in visited:
        visited.append(loc_tuple)

p1 = len(visited)
print(f"{'Solution to Part 1:':<20} {p1} (of {n_rows * n_cols} locations)")


'''
Part 2:  
Find locations where placing an obstacle would result in guard getting stuck in a loop.
In the solution method used, requires same state (location and motion direction) to be reached.
'''

'''
print("\nPart 2:")
obstacle_locs = []

for i in range(n_rows):
    for j in range(n_cols):

        print(f"\n(i, j) = ({i}, {j})")

        # Exclude initial position of guard as prompted in the clue:
        if i == starting_i and j == starting_j:
            continue
        
        new_data = [x[:] for x in data]

        # Check value - if an obstacle already, won't result in cycle since none arose in Part 1
        if new_data[i][j] == '#':
            print("## Obstacle ##")
            continue
        else:
            #Modify value to be an obstacle
            new_data[i][j] = "#"
            #print(new_data)
        
        # Initialize the guard's location and direction
        state = [starting_i, starting_j, (-1, 0)]
        state_list = [state.copy()]

        while True:
            state = next_state(new_data, state)
    
            if state == False:
                print('Exiting map')
                break
            
            # End loop if an identical state has been reached previously
            if state in state_list:
                print("***************** FOUND A LOOP ****************")
                obstacle_locs.append(tuple((i, j)))
                break
            else:
                state_list.append(state.copy())
        
p2 = len(obstacle_locs)

'''

p2 = 0

print(f"Starting location: ({starting_i}, {starting_j})")
print("\nVisited:")
print(visited)

looping_locs = []  # list of tuple locations where placing an obstacle results in a looping trajectory

# Check subset of visited
#visited = [(8, 3)]

#for n in range(len(visited)):
for i in range(n_rows):

    for j in range(n_cols):

        #print(f"\n** Checking {visited[n]}  ({n + 1} of {len(visited)})")
        print(f"\nLoop:  ({i}, {j})") 
        # Make a deep copy (i.e. not linked to original)
        new_data = [x[:] for x in data]
        
        # Check location is not 
        if new_data[i][j] == "#":
            print("Already a '#'.")
            continue
        else:
            new_data[i][j] = "#"

        state = [starting_i, starting_j, (-1, 0)]
        state_list = [state.copy()]

        while True:
            state = next_state(new_data, state.copy())
        
            if state == False:
                print("Exiting map.")
                break
            elif state in state_list:
                print("ooo  Looping  ooo")
                #print(state)
                #print(state_list)
                #looping_locs.append(tuple((visited[n][0], visited[n][1])))
                looping_locs.append(tuple((i, j)))
                p2 += 1
                break
            else:
                state_list.append(state)

print("Obstacle locations causing looping:")
print(looping_locs)
print(len(looping_locs))
print(f"{'Solution to Part 2:':<20} {p2}")
print(looping_locs)
