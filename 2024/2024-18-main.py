import sys

infile = sys.argv[1] if len(sys.argv)>=2 else './data/18.in'

raw = open(infile).read().splitlines()

bytes = [tuple(int(s) for s in r.split(',')) for r in raw]
#print(bytes)

#size, nbytes = 7, 12  # example problem
size, nbytes = 71, 1024  # actual problem

start = (0, 0)  # starting location

inf = 1e8  # initialize distance value in Dijkstra


def dijkstra(vertices, start):
    """Implement Dijkstra's algorithm to found shortest path."""
    
    graph = {}
    for v in vertices:
        if v == start:
            graph[v] = [False, 0, '']
        else:
            graph[v] = [False, inf, []]

    while sum([v[0] == False for v in graph.values()]) > 0:
        
        # Identify next point to process (nearest)
        min_dist = 10 * inf
        for k, v in graph.items():
            if v[0] == False and v[1] < min_dist:
                min_dist, min_key = v[1], k

        x, y = min_key

        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in moves:
            xx, yy = x + dx, y + dy

            if (xx, yy) in graph.keys():
                if graph[(xx, yy)][0] == False:
                    distance = graph[(x, y)][1] + 1
                    if distance < graph[(xx, yy)][1]:
                        graph[(xx, yy)][1] = distance
                        graph[(xx, yy)][2] = (x, y)
                    else:
                        pass
                else:
                    pass
            else:
                pass
        

        graph[min_key][0] = True

    return graph


def make_vertex_list(bytes, nbytes, size):
    """From list of obstacles and dimensions, make vertices."""

    vertices = []
    for i in range(size):
        for ii in range(size):
            if (ii, i) not in bytes[:nbytes]:
                vertices.append((i, ii))

    return vertices


print(f"\n*** Beginning Part 1 ***")

vertices = make_vertex_list(bytes, nbytes, size)
graph = dijkstra(vertices, start)

p1 = graph[(size-1, size-1)][1]
print(f"{'Solution to Part 1:':<20} {p1}")



# Part 2: Sequentially add bytes (obstacles) to map and determine which one prevents exit
print(f"\n*** Beginning Part 2 ***")

#nb = nbytes  # start search from known possible exit in Part 1
nb = 2930  # start nearer to solution

while True:
    nb += 1

    vertices = make_vertex_list(bytes, nb, size)
    graph = dijkstra(vertices, (0, 0))

    distance = graph[(size - 1, size - 1)][1]
    print(f"Using {nb} bytes:  Distance to exit {distance}")

    if distance>= inf:
        print(f"\nPart 2:\nByte that first prevents exit:  {bytes[nb-1]}")
        break







