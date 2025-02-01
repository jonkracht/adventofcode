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
    graph[(start[0], start[1], result[0])] = [False, 0, []]

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
                    graph[next_state] = [False, score, [current_state]]
                elif score == graph[next_state][1]:
                    graph[next_state][2].append(current_state)
            else:
                graph[next_state] = [False, score, [current_state]]

        # Clockwise
        score = graph[key][1] + 1000
        next_state = (current_state[0], current_state[1], (current_state[2] + 1) % 4)
        if next_state in graph.keys():
            if score < graph[next_state][1]:
                graph[next_state][1] = score
            elif score == graph[next_state][1]:
                graph[next_state][2].append(current_state)
        else:
            graph[next_state] = [False, score, [current_state]]

        # Counter-clockwise
        next_state = (current_state[0], current_state[1], (current_state[2] + 3) % 4)
        if next_state in graph.keys():
            if score < graph[next_state][1]:
                graph[next_state][1] = score
            elif score == graph[next_state][1]:
                graph[next_state][2].append(current_state)
        else:
            graph[next_state] = [False, graph[key][1] + 1000, [current_state]]

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

# Find state(s) whose location is "finish" with lowest scores
best_score = 1e8
end_states = []

for k, v in result.items():
    row, col, dir = k
    _, score, previous = v

    if (row, col) == finish:
        if score < best_score:
            best_score = score
            end_states.append(((row, col, dir), score, previous))

print(f"\n{len(end_states)} unique end states:\n{end_states}")


print(f"\n{'Solution to Part 1:':<20} {end_states[0][1]}")
#print(best_keys)

# Part 2:  Find number of tiles that a "best" path travels through
unique_tiles = set()
branch_count = 0
for e in end_states:
    state, score, previous = e
    route = [state, previous[0]]
    branches = []
    branch_count += 1

    while True:
        # Find next state:
        #print(branches)
        _, _, pp = result[route[-1]]

        if pp == []:
            if len(branches) == 0:
                break
            else:
                pp = [branches.pop(0)];


        for i, ppp in enumerate(pp):
            if i == 0:
                route.append(ppp)
            else:
                branches.append(ppp)
                branch_count += 1


    for r in route:
        x, y, dir = r
        unique_tiles.add((x, y))

p2 = len(unique_tiles)
print(f"\n{'Solution to Part 2:':<20} {p2}")

print(f"{branch_count} unique routes exist that produce this score")
