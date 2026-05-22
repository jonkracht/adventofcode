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

infile = sys.argv[1] if len(sys.argv) >= 2 else "./inputs/9.in"

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


# Part 2 solution:

# Construct a list of lists containing each edge's vertex points
edges = []
for i, _ in enumerate(vertices):
    if i < len(vertices) - 1:
        edges.append([vertices[i], vertices[i+1]])
    else:
        edges.append([vertices[i], vertices[0]])

print("\nEdges:")
for e in edges:
    print(e)

print(f"\nNumber of edges:  {len(edges)}")
print(f"Number of vertices:  {len(vertices)}")


# Construct list of edge points
edge_points = []
for edge in edges:
    pt1, pt2 = edge
    print(pt1, pt2)
    if pt1[0] == pt2[0]:
        dx, dy = 0, int((pt2[1] - pt1[1]) / abs(pt2[1] - pt1[1]))
    else:
        dx, dy = int((pt2[0] - pt1[0]) / abs(pt2[0] - pt1[0])), 0

    test_pt = (pt1[0] + dx, pt1[1] + dy)
    while test_pt != pt2:
        edge_points.append(test_pt)
        test_pt = (test_pt[0] + dx, test_pt[1] + dy)


print(f"\nEdge points:\n{edge_points}")


interior = []

x, y = zip(*vertices)

print(f"Creating points:  x:[{min(x)}, {max(x)}], y:[{min(y)}, {max(y)}]")
points = [(xx, yy) for xx in range(min(x), max(x) + 1)
          for yy in range(min(y), max(y) + 1)]

for v in vertices:
    points.remove(v)
for e in edge_points:
    points.remove(e)

for point in points:
    print(point)

    # print(f"\nChecking point {point}\n")

    if point in vertices:
        # print(f"Found point {point} in 'vertices'.")
        continue
    elif point in edge_points:
        # print(f"Found point {point} in 'edge_points'.")
        continue
    else:
        # print(f"Point {point} is not a vertex or edge.")

        intersections = 0

        for edge in edges:
            # print(f"Checking edge {edge}")

            # Skip horizontal edges
            if edge[0][1] == edge[1][1]:
                continue

            id1 = min(edge[0][1], edge[1][1])
            id2 = max(edge[0][1], edge[1][1])

            # print(f"IDS:  {id1}  {id2}")

            if id1 < point[1] < id2 and point[0] < edge[0][0] and point[0] < edge[1][0]:
                # print("Intersection")
                intersections += 1

        # print(f"\n{intersections} intersections found.")

        if intersections % 2 != 0:
            # print(f"{point} is an interior point!.")
            interior.append(point)
        else:
            pass
            # print(f"{point} is not an interior point.")

print(f"Interior points:\n{interior}")

all_colored_tiles = set(vertices + edge_points + interior)
print(f"\nAll colored tiles:\n{all_colored_tiles}")


# Plot vertices, edges and interior points
a, b = zip(*vertices)
plt.scatter(a, b, marker='o')
c, d = zip(*edge_points)
plt.scatter(c, d, marker='.')
e, f = zip(*interior)
plt.scatter(e, f, marker='x')

plt.show()


# Process vertex pairs to find largest color rectangle

p2_best = 0
for i, _ in enumerate(vertices):
    corner1 = vertices[i]
    for ii in range(i):
        corner2 = vertices[ii]

        print(f"Comparing corner {corner1} and {corner2}.")

        x, y = zip(*[corner1, corner2])
        rectangle_points = [(xx, yy) for xx in list(range(min(x), max(x) + 1))
                            for yy in list(range(min(y), max(y) + 1))]

        all_tiles_colored = True
        for r in rectangle_points:
            if r not in all_colored_tiles:
                all_tiles_colored = False
                break

        if all_tiles_colored:
            new_size = len(rectangle_points)
            if new_size > p2_best:
                print(f"Found new best using {
                      corner1} and {corner2}:  {new_size}")
                p2_best = new_size


print(f"{'Solution to Part 2:':<20} {p2_best}")
