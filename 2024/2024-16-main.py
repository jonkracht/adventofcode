import sys
sys.setrecursionlimit(10**6)
infile = sys.argv[1] if len(sys.argv) >= 2 else './data/16.in'

raw = open(infile).read().strip()
data = raw.split("\n")


# Implement Dijkstra's algorithm using Wikipedia pseudocode
def Dijkstra(vertices, start, starting_dir):
    '''Implement Dijkstra's algorithm with turning penalty.'''

    # Initialize graph
    graph = []
    for v in vertices:
        # Format:  location tuple, has_been_seen Boolean,
        # motion direction, score/distance, previous location tuple
        if v == start:
            graph.append([v, False, starting_dir, 0, ""])
        else:
            graph.append([v, False, "", 1e8, ""])

    while sum([g[1] == False for g in graph]) > 0:
        # Find "nearest" point
        min_dist = 1e8
        for i, g in enumerate(graph):
            if g[1] == False and g[3] < min_dist:
                min_dist, min_idx = g[3], i

        graph[min_idx][1] = True
        nearest_vertex = graph[min_idx]
        #print(nearest_vertex)

        # Find un-seen neighbors of "nearest_vertex"
        for g in graph:
            distance = (nearest_vertex[0][0] - g[0][0], nearest_vertex[0][1] - g[0][1])
            if g[1] == False and distance in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if distance == nearest_vertex[2]:
                    alt = nearest_vertex[3] + 1
                else:
                    alt = nearest_vertex[3] + 1001

                if alt < g[3]:
                    g[2] = distance
                    g[3] = alt
                    g[4] = nearest_vertex[0]

    return graph




# Parse data in list of vertices, start and finish
vertices = []
for i, row in enumerate(data):
    for ii, val in enumerate(row):
        if val != "#":
            vertices.append((i, ii))
            if val == "S":
                start = (i, ii)
            elif val == "E":
                finish = (i, ii)

starting_direction = (0, 1)  # problem states that begin facing east

print(f"Input file:  '{infile}'")
print(f"Dimensions:  ({len(data)}, {len(data[0])})")
print(f"Start {start}, finish {finish}")

result = Dijkstra(vertices, start, starting_direction)

# Construct shortest path:
shortest = []
u = finish
while True:
    for r in result:
        if r[0] == u:
            shortest.append(r)
            u = r[4]
            break

    if u == '':
        break

for s in shortest[::-1]:
    print(f"{s[0]}:  {s[3]}")

print(f"\n{'Solution to Part 1:':<20} {shortest[0][3]}")

#print(f"{'Solution to Part 2:':<20} {p2}")
