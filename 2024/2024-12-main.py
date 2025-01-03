import sys

infile = sys.argv[1] if len(sys.argv)>=2 else './data/12.in'

raw = open(infile).read().strip()

data = raw.split("\n")

#print(data)


def is_adjacent(i, j, L: list):
    """Determine if a point is adjacent to any point within a list of points."""
    
    for l in L:
        ii, jj = l[0], l[1]
        if i == ii and (abs(j - jj) == 1):
            return True
        elif j == jj and (abs(i - ii) == 1):
            return True

    return False


def make_regions(L: list):
    """Construct dictionary of regions."""

    R = {}

    for i in range(len(L)):
        for j in range(len(L[0])):

            val = L[i][j]

            if val in R.keys():

                adj = []
                for ii, r in enumerate(R[val]):
                    if is_adjacent(i, j, r):
                        adj.append(ii)
                
                # Handle number of adjancencies differently
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
                    print(f"{len(adj)}:  Too many adjancencies")
                    
            else:
                R[val] = []
                R[val].append([(i, j)])

    return R


def compute_price(R: dict):
    """Compute price metric"""
    
    price = 0
    
    for key, vals in R.items():
        for v in vals:
       
            perimeter = 0
            area = len(v)

            for i, j in v:
                neighbors = 0

                if (i+1, j) in v:
                    neighbors += 1
                if (i-1, j) in v:
                    neighbors += 1
                if (i, j-1) in v:
                    neighbors += 1
                if (i, j+1) in v:
                    neighbors += 1
                
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
p2 = 0
print(f"{'Solution to Part 2:':<20} {p2}")


