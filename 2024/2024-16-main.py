import sys
sys.setrecursionlimit(10**6)

infile = sys.argv[1] if len(sys.argv) >= 2 else './data/16.in2'

raw = open(infile).read().strip()
data = raw.split("\n")

def move(route):
    if route[-1] == finish:
        #print(f"Found a good route: {route}")
        good_routes.append(route)
        return

    # Try to move in each direction
    loc = route[-1]

    neighbors = [(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]),
                             (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)]

    for n in neighbors:
        if n not in route and data[n[0]][n[1]] != "#":
            next_route = route.copy()
            next_route.append(n)
            move(next_route)

    return

def score_moves(routes):
    """Compute score of each route"""
    scores = {}

    for i, route in enumerate(routes):
        deltas = []
        for ii in range(len(route) - 1):
            deltas.append((route[ii+1][0] - route[ii][0],
                          route[ii+1][1] - route[ii][1]))

        # Initial direction is defined to be up - if first move is not up, add a rotation.
        if deltas[0] == (0, 1):
            score = 0
        else:
            score = 1000

        for ii in range(len(deltas)):
            if deltas[ii] == deltas[ii - 1]:
                score += 1
            else:
                score += 1001

        scores[i] = (score, route)

    return scores


# Find starting and ending indices
for i, row in enumerate(data):
    for ii, val in enumerate(row):
        if val == "S":
            start = (i, ii)
        elif val == "E":
            finish = (i, ii)

good_routes = []
route = [start]

move(route)

print(f"\n{len(good_routes)} routes found through maze.")

scores = score_moves(good_routes)

best_routes, best_score = [], 1e6
for key, val in scores.items():
    #print(f"{key}: length {len(val[1])}, score {val[0]}")
    #print(val[1])

    if val[0] == best_score:
        best_routes.append(val[1])
    elif val[0] < best_score:
        best_score = val[0]
        best_routes = [val[1]]


print(f"\n{len(best_routes)} routes have lowest score of {best_score}.")
[print(b) for b in best_routes]

print(f"\n{'Solution to Part 1:':<20} {best_score}")
#print(f"{'Solution to Part 2:':<20} {p2}")
