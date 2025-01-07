import sys

infile = sys.argv[1] if len(sys.argv)>=2 else './data/12.in3'

raw = open(infile).read().strip()

data = raw.split("\n")

print(data)


def make_regions(L: list):
    """Construct dictionary of regions."""

    R = {}

    for i in range(len(L)):
        for j in range(len(L[0])):

            val = L[i][j]

            if val in R.keys():

                adj = []
                for ii, r in enumerate(R[val]):
                    if count_neighbors(i, j, r) > 0:
                        adj.append(ii)
                
                # Handle number of adjacents differently
                if len(adj) == 0:
                    R[val].append([(i, j)])

                elif len(adj) == 1:
                    R[val][adj[0]].append((i, j))
                
                elif len(adj) == 2:
                    R[val][adj[0]].append((i, j))

                    l1 = R[val][adj[0]]
                    l2 = R[val][adj[1]]

                    R[val][adj[0]] = l1 + l2
                    R[val].pop(adj[1])
                        
                else:
                    print(f"{len(adj)}:  Impossible number of adjacents found.")
                    
            else:
                # If value does not exist in dictionary, initialize
                R[val] = []
                R[val].append([(i, j)])

    return R


def count_neighbors(i, j, l):
    """"""
    neighbors = 0

    if (i + 1, j) in l:
        neighbors += 1
    if (i - 1, j) in l:
        neighbors += 1
    if (i, j - 1) in l:
        neighbors += 1
    if (i, j + 1) in l:
        neighbors += 1

    return neighbors


def compute_price(R: dict):
    """Compute price metric"""
    
    price = 0
    
    for key, vals in R.items():
        for v in vals:
       
            perimeter = 0
            area = len(v)

            for i, j in v:
                neighbors = count_neighbors(i, j, v)
                perimeter += 4 - neighbors
        
            price += area * perimeter

    return price


# Part 1:
regions = make_regions(data.copy())

'''
# Print regions
for k, v in regions.items():
    print(f"\n{k}({len(v)}):")
    for vv in v:
        print(f"({len(vv)}) {vv}")
'''

p1 = compute_price(regions)

print(f"{'Solution to Part 1:':<20} {p1}")


# Part 2:

def compute_sides(L: list):
    """Takes list of points making up a region and returns number of sides."""
   
    print(f"\nRegion:\n{L}")

    # Create a list of points that are midpoints of cell edges
    edges = []

    for l in L:
        edges.append((l[0] - 0.5, l[1]))
        edges.append((l[0], l[1] + 0.5))
        edges.append((l[0] + 0.5, l[1]))
        edges.append((l[0], l[1] - 0.5))

    print(f"Edges:  {edges}")
    
    # Find edges exterior to the region (i.e. only appear once)
    exterior = set(edges)
    print(f"Exterior: {exterior}")

    # Travel around perimeter clockwise
    unorder = list(exterior)
    order = [unorder[0]]
    unorder.pop(0)

    print(f"\nUnordered:  {unorder}")
    print(f"Ordered: {order}")

    
    # Find possible next points
    candidates = []
    for u in unorder:
        if int(abs(order[0][0] - u[0]) + abs(order[0][1] - u[1])) == 1:
            candidates.append(u)

    print(f"Candidates:  {candidates}")

        


    sides = 0
    return sides


price2 = 0

for k, v in regions.items():
    print(f"\nRegion {k}:")
    for vv in v:
        sides = compute_sides(vv.copy())
        area = len(vv)

        price2 += sides * area

print(f"{'Solution to Part 2:':<20} {price2}")
