import sys

infile = sys.argv[1] if len(sys.argv)>=2 else './data/8.in'

data = open(infile).read()
#print(data)  # Print formatted map
data = data.split("\n")[:-1]  # last row is empty

nrows, ncols = len(data), len(data[0])
print(f"\nMap is {nrows} by {ncols}")

# Create dictionary of characters found in the map and their locations
locations = {}
for rid in range(len(data)):
    for cid in range(len(data[rid].strip())):
        val = data[rid][cid]
        if val != ".":
            if val in locations.keys():
                locations[val].append((rid, cid))
            else:
                locations[val] = [(rid, cid)]

#print(locations)  # display dictionary of antennas types and locations

def in_map(nrows, ncols, x, y):
    """Helper to determine if candidate point is within map."""
    return (0 <= x < nrows) and ( 0 <=y <ncols)

def gcd(a, b):
    """Greatest common divisor; used to compute reduced slope for part 2."""
    if a%b == 0:
        return b
    return gcd(b, a%b)


p1_antinodes, p2_antinodes = [], []

for key, locs in locations.items():

    # Iterate over transmitter combinations
    print(f"\n** '{key}' transmitters **\nLocations:  {locs}")

    for i in range(len(locs) - 1):
        for ii in range(i+1, len(locs)):
            # Compute delta
            delx, dely = locs[ii][0] - locs[i][0], locs[ii][1] - locs[i][1]

            # Compute candidate locations
            x1, y1 = locs[ii][0] + delx, locs[ii][1] + dely
            x2, y2 = locs[i][0] - delx, locs[i][1] - dely

            print(f"\n{locs[i]} and {locs[ii]}")
            #print(f"New locations:  ({x1}, {y1}) and ({x2}, {y2})")
            print(f"{'Delta:':<20}({delx}, {dely})")

            # Check if in grid and if not, append
            if in_map(nrows, ncols, x1, y1) and ((x1, y1) not in p1_antinodes):
                p1_antinodes.append((x1, y1))
            if in_map(nrows, ncols, x2, y2) and ((x2, y2) not in p1_antinodes):
                p1_antinodes.append((x2, y2))


            # Part 2:
            # All locations that have characters appears multiple times are antinodes
            if locs[i] not in p2_antinodes:
                p2_antinodes.append(locs[i])
            if locs[ii] not in p2_antinodes:
                p2_antinodes.append(locs[ii])

            # Compute a "reduced" delta/slope to capture locations between transmitter pairs
            # At least in this version of the data, all deltas have no common divisors other than 1 so turned out to be unnecessary.
            factor = gcd(abs(delx), abs(dely))
            delx, dely = int(delx/factor), int(dely/factor)

            print(f"{'Reduced delta:':<20}({delx}, {dely})")

            # Check in each direction from one of the transmitters
            xn, yn = locs[i][0], locs[i][1]
            while in_map(nrows, ncols, xn, yn):
                xn += delx
                yn += dely

                if in_map(nrows, ncols, xn, yn) and ((xn, yn) not in p2_antinodes):
                    p2_antinodes.append((xn, yn))

            xn, yn = locs[i][0], locs[i][1]
            while in_map(nrows, ncols, xn, yn):
                xn -= delx
                yn -= dely

                if in_map(nrows, ncols, xn, yn) and ((xn, yn) not in p2_antinodes):
                    p2_antinodes.append((xn, yn))


print(f"\nPart 1 antinodes:\n{sorted(p1_antinodes)}")

p1 = len(p1_antinodes)
print(f"{'Solution to Part 1:':<20} {p1}")

print(f"\nPart 2 antinodes:\n{sorted(p2_antinodes)}")
p2 = len(p2_antinodes)

print(f"{'Solution to Part 2:':<20} {p2}")
