import sys
sys.setrecursionlimit(10**6)
infile = sys.argv[1] if len(sys.argv) >= 2 else './data/16.in'

raw = open(infile).read().strip()
data = raw.split("\n")


# Implement Dijkstra's algorithm using Wikipedia pseudocode
def Dijkstra(vertices, start, starting_dir):
    """Implement Dijkstra's algorithm with turning penalty."""

    # Define a dictionary for direction
    motions = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}

    # Find key of "starting_dir"
    result = [key for key, val in motions.items() if val == starting_dir]

    graph = {}
    graph[(start[0], start[1], result[0])] = [False, 0, ""]

    while sum([g[0] == False for g in graph.values()]):

        # Find vertex with lowest score
        min_score = 1e8
        for k, v in graph.items():
            if v[0] == False and v[1] < min_score:
                key, min_score = k, v[1]

        current_state = key
        graph[key][0] = True

        # Attempt to move straight
        next_loc = (current_state[0] + motions[current_state[2]][0], current_state[1] + motions[current_state[2]][1])
        score = graph[key][1] + 1

        if next_loc in vertices:
            next_state = (next_loc[0], next_loc[1], current_state[2])
            if next_state in graph.keys():
                if score < graph[next_state][1]:
                    graph[next_state] = [False, score, current_state]
            else:
                graph[next_state] = [False, score, current_state]

        # Clockwise
        score = graph[key][1] + 1000
        next_state = (current_state[0], current_state[1], (current_state[2] + 1) % 4)
        if next_state in graph.keys():
            if score < graph[next_state][1]:
                graph[next_state][1] = score
        else:
            graph[next_state] = [False, score, current_state]

        # Counter-clockwise
        next_state = (current_state[0], current_state[1], (current_state[2] + 3) % 4)
        if next_state in graph.keys():
            if score < graph[next_state][1]:
                graph[next_state][1] = score
        else:
            graph[next_state] = [False, graph[key][1] + 1000, current_state]


        #print(graph)



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

# Find route that reach finish with lowest score
best = 1e8
for k, v in result.items():
    x, y, d = k
    if (x, y) == finish:
        print(f"{k}:  {v}")
        if v[1] < best:
            best, best_key = v[1], k

'''
print("Shortest route:")
shortest_route = [best_key]

while True:
    _, score, previous = result[shortest_route[-1]]
    shortest_route.append(previous)

    x, y, d = shortest_route[-1]
    if (x, y) == start:
        break

for s in shortest_route[::-1]:
    print(s)
'''
#print(f"\n{'Solution to Part 1:':<20} {shortest[0][3]}")

#print(f"{'Solution to Part 2:':<20} {p2}")
