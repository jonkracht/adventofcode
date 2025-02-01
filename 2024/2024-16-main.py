import sys

infile = sys.argv[1] if len(sys.argv)>=2 else './data/16.in'
data = open(infile).read().strip().split("\n")

starting_direction = (0, 1)  # problem states initial direction faces east

vertices = set()
for i, row in enumerate(data):
    for ii, val in enumerate(row):
        if val != "#":
            vertices.add((i, ii))
            if val == "S":
                starting_pt = (i, ii)
            elif val == "E":
                finish_pt = (i, ii)

motions = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}  # right, down, left, up

starting_dir_ordinal = [k for k, v in motions.items() if v == starting_direction][0]


def dijkstra(vertices, start, start_dir):
    """Use Dijkstra's algorithm to find the shortest distance/cost to each point."""

    '''
    Graph is a dictionary with keys equal to state (position, orientation) with
    values of lists containing has_been_processed Boolean, score and list of previous point(s).
    '''

    graph = {(start[0], start[1], start_dir): [False, 0, []]}

    # Iterate until all unique states have been processed
    while sum([v[0] == False for k, v in graph.items()]) > 0:

        # Find known state with the lowest score:
        min_score = 1e8
        for key, val in graph.items():
            if val[0] == False and val[1] < min_score:
                min_score, min_key = val[1], key

        print(min_score)  # display a measure of progress

        graph[min_key][0] = True  # mark state as processed

        i, j, direction = min_key
        _, score, _ = graph[min_key]

        states_to_add = {}

        # Three actions possible:
        # 1.)  Proceed straight (i.e. in current direction)
        ii, jj = i + motions[direction][0], j + motions[direction][1]

        if (ii, jj) in vertices:  # make sure candidate point is indeed a vertex
            states_to_add[(ii, jj, direction)] = [False, score + 1, [(i, j, direction)]]

        # 2.)  Turn clockwise
        states_to_add[(i, j, (direction + 1) % 4)] = [False, score + 1000, [(i, j, direction)]]

        # 3.)  Turn counter-clockwise
        states_to_add[(i, j, (direction + 3) % 4)] = [False, score + 1000, [(i, j, direction)]]

        # Check if new candidate states already exist in graph:
        for k, v in states_to_add.items():
            if k not in graph.keys():  # new state reached
                graph[k] = v

            else:
                # Better way to reach state
                if v[1] < graph[k][1]:
                    graph[k][1], graph[k][2] = v[1], v[2]

                # Equivalent way to reach state
                elif v[1] == graph[k][1]:
                    graph[k][2].append(v[2][0])

    return graph


# Create graph
graph = dijkstra(vertices, starting_pt, starting_dir_ordinal)

# Find state(s) that reaches "finish" with best score
best_score, best_finish = 1e8, []
for k, v in graph.items():
    i, j, _ = k
    if (i, j) == finish_pt:
        if v[1] < best_score:
            best_score = v[1]
            best_finish = [(k, v)]
        elif v[1] == best_score:
            best_finish.append((k, v))

print(f"\n{'Solution to Part 1:':<20} {best_score}")

print(f"({len(best_finish)} unique route(s) achieve this score.)")


'''
Part 2:  Find number of tiles in map that one or more best routes pass through

Strategy:  
Starting best finishing state found in Part 1.
Trace backwards through graph using previous state.
If multiple previous states exist, note them and process when finished current route.
'''

tiles_visited = set()
for b in best_finish:
    state = b[0]
    branches = set()

    while True:
        i, j, direction = state
        tiles_visited.add((i, j))

        _, score, previous = graph[state]

        if not previous:  # when "start" vertex is reached
            if len(branches) == 0:
                break
            else:
                state = branches.pop()
                #print(f"End of route reached.  Starting again at branching state {state}")

        # If one previous state exists, make it next state; if multiple, add extras to "branches" and process later
        if len(previous) == 1:
            state = previous[0]
        else:
            for i, p in enumerate(previous):
                if i == 0:
                    state = p
                else:
                    branches.add(p)

print(f"\n{'Solution to Part 2:':<20} {len(tiles_visited)}")
