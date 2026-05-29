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
edges, walls, edge_pts = set(), {}, set()
A = []
for i, _ in enumerate(vertices):

    # Construct 'edges' list of point tuples
    if i == len(vertices) - 1:
        p1, p2 = vertices[i], vertices[0]
    else:
        p1, p2 = vertices[i], vertices[i+1]

    edge = (p1, p2)
    edges.add(edge)

    # Construct list of boundary points (vertex + edge)
    if p1[0] == p2[0]:
        delta = p2[1] - p1[1]
        dx, dy = 0, int(delta / abs(delta))
    else:
        delta = p2[0] - p1[0]
        dx, dy = int(delta / abs(delta)), 0

    # Add points sequentially from p1 until p2 is reached
    new_pt = p1
    while True:
        new_pt = (new_pt[0] + dx, new_pt[1] + dy)
        if new_pt == p2:
            break

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
    else:
        A.append((max(p1[0], p2[0]), p1[1]))

print(f"\nEdges:\n{edges}")

print(f"\nEdge points:\n{edge_pts}")

Q = {}
for e in edge_pts:
    if e[1] in Q:
        Q[e[1]].append(e[0])
    else:
        Q[e[1]] = [e[0]]

edge_pt_dict = {}
for k, v in dict(sorted(Q.items())).items():
    edge_pt_dict[k] = sorted(v)

print(f"Edge point dict:\n{edge_pt_dict}")

interior = []
for y in range(min(edge_pt_dict.keys()), max(edge_pt_dict.keys())):
    print(f"Y={y}")

    for x in range(min(edge_pt_dict[y]), max(edge_pt_dict[y]) + 1):
        print(f"Checking point ({x}, {y})")

        if (x, y) in vertices or (x, y) in edge_pts:
            continue

        count = 0
        for edge in edges:
            if x < edge[0][0]:
                if edge[0][1] < y <= edge[1][1] or edge[1][1] < y <= edge[0][1]:
                    count += 1

        if count % 2 != 0:
            point = (x, y)
            print("Found interior point")
            interior.append(point)

print(interior)

a, b = zip(*vertices)
plt.scatter(a, b, marker='s')
c, d = zip(*edge_pts)
plt.scatter(c, d, marker='.')
g, h = zip(*interior)
plt.scatter(g, h, marker='o')
plt.show()
p2_best = 0

print(f"\n{'Solution to Part 2:':<20} {p2_best}")
