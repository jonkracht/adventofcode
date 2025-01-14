import sys

infile = sys.argv[1] if len(sys.argv)>=2 else './data/14.in'

raw = open(infile).read().strip()

# Parse raw
data = []
for r in raw.split("\n"):
    print(r)
    temp = []
    for rr in r.split(" "):
        vals = rr.split("=")[1].split(",")
        temp.append((int(vals[0]), int(vals[1])))

    data.append(temp)
    
#print(data)


def next_state(state, grid_dims):
    """Compute next state of the robots."""

    new_state = []

    for s in state:
        pos, vel = s[0], s[1]

        # Add velocity to position
        new_x, new_y = pos[0] + vel[0], pos[1] + vel[1]

        # Check if still in region; if not, wrap in appropriate way
        if new_x >= grid_dims[0]:
            new_x -= grid_dims[0]
        elif new_x < 0:
            new_x = grid_dims[0] + new_x

        if new_y >= grid_dims[1]:
            new_y -= grid_dims[1]
        elif new_y < 0:
            new_y = grid_dims[1] + new_y 
            
        new_state.append([(new_x, new_y), vel])
        
    return new_state


def compute_safety_factor(state, dims):
    """Count robots in each quadrant and multiply."""

    midx, midy = dims[0] // 2, dims[1] //2

    quad_cts = 4 * [0]  # quadrant counts

    for s in state:
        pos = s[0]

        if not (pos[0] == midx or pos[1] == midy):
            if pos[0] < midx:
                if pos[1] < midy:
                    quad_cts[0] += 1
                else:
                    quad_cts[1] += 1
            else:
                if pos[1] < midy:
                    quad_cts[2] += 1
                else:
                    quad_cts[3] += 1
    
    print(f"\nQuadrant counts:  {quad_cts}")

    sf = 1
    for q in quad_cts:
        sf *= q

    print(f"Safety factor (product of quad counts):  {sf}")

    return sf


# Part 1:  State after 100 seconds
#grid_dims, t = (11, 7), 100  # example problem
grid_dims, t = (101, 103), 100  # actual problem

state = data.copy()

for t in range(t):
    state = next_state(state, grid_dims)

locs = []
[locs.append(s[0]) for s in state]

print(f"\nState after {t} seconds:\n{sorted(locs)}")

# Compute safety factor of current state
sf = compute_safety_factor(state, grid_dims)

print(f"\n{'Solution to Part 1:':<20} {sf}")



# Part 2:  Find shortest time until robots form a Christmas tree shape

def generate_grid(state, dims):
    """Takes state representation of robots and creates a grid of current locations."""

    # Initialize grid with zeros
    grid = []
    [grid.append(dims[0] * [0]) for _ in range(dims[1])]

    for s in state:
        pos = s[0]
        grid[pos[1]][pos[0]] += 1

    return grid


def plot_grid(grid):
    """Print grid of current state row by row to stdout."""

    print(10*'\n')  # print some empty lines to visually separate each time step
    
    for g in grid:
        row = ''
        for gg in g:
            if gg == 0:
                row += '.'
            else:
                row += str(gg)

        print(row)

    return


def is_tree_shape(grid):
    """Takes x,y configuration of points and returns Boolean if might be a tree shape"""

    # Problem statement is (probably purposely) vague so unclear which conditions to check.

    is_tree = True

    '''
    Possible conditions of tree-ness:
    * Top-left and top-right of image are blank
    * Maybe bottom left and bottom right are also blank
    '''

    dim = (len(grid), len(grid[0]))
    
    # Check four corner of grid to be empty
    check = 5
    for i in range(check):
        for j in range(check):
            #print(f"{i}, {j}")
            if grid[i][j] != 0:
                is_tree = False

            if grid[i][dim[1] - j - 1] != 0:
                is_tree = False

            if grid[dim[0] - i - 1][j] != 0:
                is_tree = False

            if grid[dim[0] - i - 1][dim[1] - j - 1] != 0:
                is_tree = False
    
    return is_tree


def centrality(state, dims):
    """Compute mean horizontal spread of state."""

    centrality = 0
    for s in state:
        pos = s[0]
        centrality += abs(dims[0]//2 - pos[0])
        
    return centrality/len(state)


state2 = data.copy()
t = 0
min_c = 1e8

while True:

    t += 1
    print(t)

    state2 = next_state(state2.copy(), grid_dims)
    c = centrality(state2.copy(), grid_dims)

    if c < min_c:  # keep track of lowest centrality seen
        min_c = c

    #if is_tree_shape(grid):
    if True:

        # Assume tree shapes have less horizontal spread (though centrality measure as defined assumes shape is at or near the center of the grid - problem statement is very vague)

        if c < 15:  # pick some centrality threshold to view states to see if there's a tree
            
            grid = generate_grid(state2.copy(), grid_dims) 
            plot_grid(grid)
            
            print(f"t = {t}:  c = {c}  (min_c = {min_c})")
           
            see_a_tree = input("See a tree? (y/n) ")
            if see_a_tree == "y":
                break

print(f"\n{'Solution to Part 2:':<20} Took {t} seconds to see a tree.")

