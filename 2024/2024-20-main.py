import sys, copy

infile = sys.argv[1] if len(sys.argv)>=2 else './data/20.in'

maze = open(infile).read().strip().split('\n')

nrows, ncols = len(maze), len(maze[0])
O, V = set(), set()
inf = 1000000

for i in range(nrows):
    for ii in range(ncols):
        val = maze[i][ii]
        if val == '#':
            O.add((i, ii))
        else:
            V.add((i, ii))
            if val == 'S':
                start = (i, ii)
            elif val == 'E':
                end = (i, ii)


def dijkstra(vertices: set, start_point: tuple, start_dist: int, previous_point: tuple, extra: tuple) -> dict:
    """"""

    graph = {}
    heap = {}
    heap[start_point] = [start_dist, previous_point]

    if len(extra) > 0:
        vertices.add(extra)

    while len(heap) > 0:

        # Find heap item with shortest distance
        min_val = inf
        for k, v in heap.items():
            if v[0] < min_val:
                min_id, min_val, previous = k, v[0], v[1]

        r, c = min_id
        heap.pop(min_id)

        graph[min_id] = [min_val, previous]

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            rr, cc = r + dr, c + dc
            if (rr, cc) in vertices and (rr, cc) not in graph:
                if (rr, cc) in heap:
                    if heap[(rr, cc)][0] > min_val + 1:
                        heap[(rr, cc)] = [min_val + 1, (r, c)]
                else:
                    heap[(rr,cc)] = [min_val + 1, (r, c)]

    return graph


# Solve maze without any cheats
og = dijkstra(V.copy(), start, 0, '', ())
orig_dist = og[end][0]
print(orig_dist)

# Construct route by backtracking via previous_pt
route = [[end, og[end][0], og[end][1]]]
while route[-1][2] != '':
    previous = route[-1][2]
    route.append([previous, og[previous][0], og[previous][1]])

route = route[::-1]

cheats = {}
for i, pt in enumerate(route):
    #print(f"\n*** Checking {pt} ***")

    VV = V.copy()
    r, c = pt[0]

    (start_loc, dist, previous) = pt

    for ii in range(i):
        VV.remove(route[ii][0])

    print(f"Number of vertices to consider:  {len(VV)}")

    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        rr, cc = r + dr, c + dc

        if rr not in [0, nrows-1] and cc not in [0, ncols-1] and (rr, cc) in O:
            new_graph = dijkstra(VV.copy(), start_loc, dist, previous, (rr, cc))
            if end in new_graph.keys():
                new_time = new_graph[end][0]
                cheats[(r, c), (rr, cc)] = new_time

# Aggregate distance/time improvement
p1_counts = {}
for k, v in cheats.items():
    delta = orig_dist - v
    if delta in p1_counts.keys():
        p1_counts[delta] += 1
    else:
        p1_counts[delta] = 1

print("\nResults:")
print("\nSavings     (count)")
print("---------------")
for k, v in dict(sorted(p1_counts.items(), reverse=True)).items():
    print(f"{k:<10}  ({v})")

p1 = 0
for k, v in p1_counts.items():
    if k >= 100:
        p1 += v

print(f"\n{'Solution to Part 1:':<20} {p1}")



# Part 2: Allow cheats up to 20 cells long 


#print(f"{'Solution to Part 2:':<20} {p2}")
