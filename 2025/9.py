'''
# Problem description

## Part 1
Given a set of cartesian points, compute the largest rectangle that can be constructed using a pair of points as its corners.

Loop over pairs of points and compute area.


## Part 2
Now instructed that green tiles connect vertices adjacent in the given list.  Combinging green and red tiles forms a closed polygon.  All tiles within this polygon are also green.

Goal is to find largest rectangle that can be made with red tiles in opposite corner and entirely filled with green tiles.

Solution:
Cast rays from each candidate point.  If the ray intersects the polygon an odd number of times, it is an interior point;  if odd, it is exterior.

'''

import matplotlib.pyplot as plt
import logging
import sys

logging.basicConfig(level=logging.WARNING)

infile = sys.argv[1] if len(sys.argv) >= 2 else "./inputs/9.in2"

vertices = open(infile).read().strip().split("\n")
vertices = [tuple(int(ii) for ii in i.split(",")) for i in vertices]
logging.info(f"Input vertices:  {vertices}")

p1_best = 0
for id1 in range(len(vertices)):
    for id2 in range(id1):
        logging.info(f"Checking {vertices[id1]} and {vertices[id2]}.")

        # Area calculation (inclusive of endpoints)
        area = (abs(vertices[id1][0] - vertices[id2][0]) + 1) * (
            abs(vertices[id1][1] - vertices[id2][1]) + 1
        )

        logging.info(f"Area computed as:  {area}")

        if area > p1_best:
            p1_best = area
            logging.info(f"**** Found new best:  {p1_best}")

print(f"{'Solution to Part 1:':<20} {p1_best}")


# Part 2 solution
edges, walls, edge_pts = [], {}, set()

for i, _ in enumerate(vertices):
    if i == len(vertices) - 1:
        p1, p2 = vertices[i], vertices[0]
    else:
        p1, p2 = vertices[i], vertices[i+1]

    edge = (p1, p2)
    edges.append(edge)

    # Construct list of boundary points (vertex + edge)

    if p1[0] == p2[0]:
        delta = p2[1] - p1[1]
        dx, dy = 0, int(delta / abs(delta))
    else:
        delta = p2[0] - p1[0]
        dx, dy = int(delta / abs(delta)), 0

    new_pt = p1
    while new_pt != p2:
        new_pt = (new_pt[0] + dx, new_pt[1] + dy)
        edge_pts.add(new_pt)
        print(f"Added point {new_pt}")

    if p1[0] == p2[0]:
        xval = p1[0]
        miny, maxy = min(p1[1], p2[1]), max(p1[1], p2[1])

        for ii in range(miny + 1, maxy):
            if ii not in walls:
                walls[ii] = [xval]
            else:
                walls[ii].append(xval)

# Sort walls dictionary by key
walls = dict(sorted(walls.items()))
for k, v in walls.items():
    print(k, v)


'''
print("\nEdge points:\n")
for e in boundary_pts:
    print(e)
'''

x, y = zip(*vertices)
interior = []

for xx in range(min(x), max(x) + 1):
    for yy in range(min(y), max(y) + 1):

        pt = (xx, yy)
        print(f"Checking point {pt}")

        if pt not in edge_pts:
            if yy in walls:
                ct = sum(val > xx for val in walls[yy])

                if ct % 2 != 0:
                    interior.append(pt)
interior.sort()

print("\nInterior points:")
for i in interior:
    print(i)

# plt.scatter(x, y)
c, d = zip(*interior)
plt.scatter(c, d)
e, f = zip(*edge_pts)
plt.scatter(e, f)
plt.show()


p2_best = 0

print(f"\n{'Solution to Part 2:':<20} {p2_best}")
