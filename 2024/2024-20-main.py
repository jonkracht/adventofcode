import sys, copy

infile = sys.argv[1] if len(sys.argv)>=2 else './data/20.in'

maze = open(infile).read().strip().split('\n')

nrows, ncols = len(maze), len(maze[0])
O, V = set(), set()  # obstacles, vertices in graph
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
    """Compute shortest distances between points in a graph."""

    graph, heap = {}, {}
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

# Create two graphs:  one of distances from each point to 'start' and the other to 'end'
forward_graph = dijkstra(V.copy(), start, 0, '', ())
backward_graph = dijkstra(V.copy(), end, 0, '', ())

original_score = forward_graph[end][0]  # solution of the un-modified maze

print("\nSolved original maze in both forward and backward directions.")
print(f"Best distance/time is:  {original_score}")


def find_cheats(fg: dict, bg: dict, cheat_size: int, base_score: int):
    """Identify cheats that reduce the distance/time."""

    cheats = {}

    for (r, c), v in forward_graph.items():
        #print(f"({r}, {c})")
        for (rr, cc), vv in backward_graph.items():
            dist = abs(rr - r) + abs(cc - c)
            if 0 < dist <= cheat_size:
                cheat_score = v[0] + vv[0] + dist
                savings = base_score - cheat_score

                if savings > 0:
                    cheats[(r, c, rr, cc)] = savings

    return cheats

def count_cheats(cheats: dict, threshold: int) -> int:
    """Count cheat number that reduce distance/time by an amount at least equal to 'threshold'."""

    savings = {}
    for k, v in cheats.items():
        if v in savings:
            savings[v] += 1
        else: 
            savings[v] = 1

    ct = 0
    for k, v in savings.items():
        if k >= threshold:
            ct += v

    return ct


# Part 1:  Find number of cheats of length at most 2 that reduce solution path length/time by 100 units or more

cheats_p1 = find_cheats(forward_graph, backward_graph, 2, original_score)

p1 = count_cheats(cheats_p1, 100)
print(f"\n{'Solution to Part 1:':<20} {p1}")


# Part 2:  Now consider cheats of length up to 20

cheats_p2 = find_cheats(forward_graph, backward_graph, 20, original_score)

p2 = count_cheats(cheats_p2, 100)
print(f"{'Solution to Part 2:':<20} {p2}")
