
'''
# Problem description

## Part 1  
On a grid with paper peppered throughout, count the number of locations that have fewer than 4 obstacles among the 8 adjacent positions.

## Part 2
Find how many paper locations can be ultimately removed by repeatedly removing "assessible" (same criterion as in Part 1)

'''

import sys
import matplotlib.pyplot as plt

infile = sys.argv[1] if len(sys.argv) >= 2 else "./inputs/4.in"

input = open(infile).read().strip().split()
input = [list(i) for i in input]  # cast as list of lists


def print_grid(grid, label, axis):
    '''Function to plot configuration using plt.imshow.'''

    new_grid = []
    low_val, high_val = 0.0, 1.0


    for g in grid:
        row = []
        for gg in g:
            if gg == '.':
                row.append(low_val)
            elif gg == '@':
                row.append(high_val)

        new_grid.append(row)

    axis[0].cla()
    axis[0].imshow(new_grid)
    axis[0].set_title(label, size=40)

    #plt.show()

    return

fig, ax = plt.subplots(1, 1)

print_grid(input, "Original configuration", ax)


def find_accessible(grid, threshold):
    """Determine locations that have fewer than 'threshold' neighbors."""

    accessible = []
    
    num_rows = len(grid)
    num_cols = len(grid[0])

    #print(f"Grid of dimension:  {num_rows} by {num_cols}")

    for r in range(num_rows):
        for c in range(num_cols):

            #print(f"\n(r,c) = ({r}, {c})")
            if grid[r][c] == '@':  # check that paper exists at current location
                neighbors = 0

                for dr, dc in [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]:
                    rr, cc = r + dr, c + dc
                    #print(f"rr: {rr}, cc: {cc}")
                    if 0 <= rr < num_rows and 0 <= cc < num_cols:
                        if grid[rr][cc] == '@':
                            neighbors += 1
                        else:
                            #print(f"Off grid!  ({rr}, {cc})")
                            pass

                #print(neighbors)
                if neighbors < threshold:
                    #print(f"(r,c) = ({r}, {c})")
                    accessible.append((r, c))

    return accessible


# Part 1
print(f"\nPart 1:")
p1 = find_accessible(input, threshold=4)

print(f"Accessible points: {p1}")
print(f"\n{'Solution to Part 1:':<20} {len(p1)}")


# Part 2
print(f"\nPart 2:")

p2, loop = 0, 0

while True:
    loop += 1

    accessible = find_accessible(input, threshold=4)

    n_access = len(accessible)
    #print(n_access)
    p2 += n_access

    if n_access:
        # Remove (i.e. set to '.') all accessible positions
        for a, b in accessible:
            #print(a, b)
            input[int(a)][int(b)] = '.'

        print_grid(input, f"Loop {loop}", ax)

    else:
        break

print(f"\n{'Solution to Part 2:':<20} {p2}")
