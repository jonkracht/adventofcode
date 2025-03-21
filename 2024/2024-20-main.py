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


def dijkstra(vertices: set, start: tuple, extra: tuple) -> dict:
    """"""
    
    graph, heap = {}, {}

    if len(extra) > 0:
        vertices.add(extra)

    r, c = start
    heap[start] = 0  # initialize heap

    while heap:

        r, c = min(heap)
        
        graph[(r, c)] = heap[(r, c)]
        vertices.remove((r,c))

        for dr, dc in [(1, 0 ), (-1, 0), (0, 1), (0, -1)]:
            rr, cc = r + dr, c + dc

            if (rr, cc) in vertices:
                if (rr, cc) in heap:
                    if heap[(r, c)] + 1 < heap[(rr, cc)]:
                        heap[(rr, cc)] = heap[(r, c)] + 1
                else:
                    heap[(rr, cc)] = heap[(r, c)] + 1

        heap.pop((r, c))

    return graph
original_graph = dijkstra(V.copy(), start, ())

print(original_graph)

original_time = original_graph[end]
print(f"Time to traverse original map:  {original_graph[end]}")  


new = dijkstra(V.copy(), start, (7, 6))
print(new[end])



count = 0

time = {}
for r, c in O:
    if r in [0, nrows - 1] or c in [0, ncols - 1]:
        continue

    new_time = dijkstra(V.copy(), start, (r, c))[end]
    
    time[(r, c)] = new_time
    if original_time - new_time >= 100:
        count += 1

    #print(f"Adding obstacle at ({r}, {c}) gave best time of {new_time}.")

#print(time)

savings = {}
for k, v in time.items():
    if v in savings:
        savings[v] += 1
    else:
        savings[v] = 1

for k, v in sorted(savings.items()):
    print(f"{original_time - k}:  {v}")

print(count)

#print(f"{'Solution to Part 1:':<20} {p1}")
#print(f"{'Solution to Part 2:':<20} {p2}")
