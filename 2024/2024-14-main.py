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


def next_state(state, xdim, ydim):
    """"""

    new_state = []

    for s in state:
        pos, vel = s[0], s[1]

        # Add velocity to position
        new_x, new_y = pos[0] + vel[0], pos[1] + vel[1]

        # Check if still in region; if not, wrap
        if new_x > xdim:
            new_x -= xdim + 1
        elif new_x < 0:
            new_x = xdim + new_x + 1

        if new_y > ydim:
            new_y -= ydim + 1
        elif new_y < 0:
            new_y = ydim + new_y + 1
            

        temp = []
        temp.append((new_x, new_y))
        temp.append(vel)

        new_state.append(temp)
        

    return new_state


def compute_safety_factor(state, xdim, ydim):
    """"""

    midx, midy = xdim // 2, ydim //2

    quad_cts = 4 * [0]

    for s in state:
        pos = s[0]

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
    
    print(quad_cts)

    sf = 1
    for q in quad_cts:
        sf *= q

    return sf


# Part 1:  State after 100 seconds
t = 2  # number of state updates to perform
xdim, ydim = 11, 7  # dimensions of the space, given in problem text
#xdim, ydim = 101, 103  # dimensions of the space, given in problem text

state = data.copy()

for _ in range(t):
    state = next_state(state, xdim - 1, ydim - 1)
    print(state)

# Compute safety factor of current state
sf = compute_safety_factor(state, xdim - 1, ydim - 1)


print(f"{'Solution to Part 1:':<20} {sf}")


# Part 2:

#print(f"{'Solution to Part 2:':<20} {p2}")
