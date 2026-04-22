"""
# Problem description

## Part 1
Given a group of points in 3D space, create networks by sequentially joining together the closest pairs.  After performing a given number of connections between the nodes, perform some arithmetic on the sizes of the largest networks.


## Part 2
Continue connecting points using the previous method until all are contained within the same network.  Perform some arithmetic on the final two points' positions.

"""

import logging
import math
import sys

infile = sys.argv[1] if len(sys.argv) >= 2 else "./inputs/8.in"
input = open(infile).read().strip().split("\n")

pts = [tuple(int(ii) for ii in i.split(",")) for i in input]
print(pts)

# Setup logger
logging.basicConfig(level=logging.INFO)


def distance(p1: tuple, p2: tuple) -> float:
    """Compute Euclidean distance between two points in 3D space."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)


monkey = {}

for i in range(len(pts)):
    for ii in range(i):
        logging.info(f"Processing ({i}, {ii})")

        temp = distance(pts[i], pts[ii])
        logging.info(f"Computed distance:  {temp}")

        monkey[(i, ii)] = temp

# Create ordered list
distances = [
    [k, v] for k, v in dict(sorted(monkey.items(), key=lambda item: item[1])).items()
]


# Part 1 solution:
num_connections = 1000  # given in the problem definition


def connect(distance_list, num_connections, problem_part):
    """Create connections between points to form networks."""

    logging.info("Begin generating networks")
    networks = []

    n = -1
    while True:
        n += 1
        id1, id2 = distance_list[n][0]

        logging.info(f"\nConnection {n}: {id1} -> {id2} [{pts[id1]} -> {pts[id2]}]")

        """
        Check known networks to see if either point resides within.  Four(-ish) possibilities:
        * Case 1:  Neither point resides in any network
        * Case 2:  Both points already reside in the same network
        * Case 3:  Only one point resides within a network
        * Case 4:  Each point resides within different networks.
        """

        # Determine which network each point may lie within
        is_contained = [-1, -1]
        for i, network in enumerate(networks):
            if id1 in network:
                is_contained[0] = i
                logging.info(f"Found P1={id1} in network {i}")

            if id2 in network:
                is_contained[1] = i
                logging.info(f"Found P2={id2} in network {i}")

        # Case 1:  Neither point lies within a network.  Create a new one.
        if is_contained[0] == -1 and is_contained[1] == -1:
            logging.info(
                f"Case 1 (neither point found): Creating new network [{id1}, {id2}]"
            )
            networks.append([id1, id2])
            logging.info(f"{len(networks)} networks exist.")

        # Case 2:  Both points already lie within the same network.  Do nothing.
        elif (
            is_contained[0] >= 0
            and is_contained[1] >= 0
            and is_contained[0] == is_contained[1]
        ):
            logging.info(
                f"Case 2 (both points [{id1}, {id2}] already reside in network {is_contained[0]}):  Doing nothing."
            )

            # Case 3a:  Pt2 lies with a network.  Add Pt1 to that network
        elif is_contained[0] == -1 and is_contained[1] >= 0:
            logging.info(f"Case 3a:  Adding {id1} to network {is_contained[1]}")
            networks[is_contained[1]].append(id1)
            logging.info(networks[is_contained[1]])

            # Case 3b:  Pt1 lies within a network.  Add Pt2 to that network.
        elif is_contained[0] >= 0 and is_contained[1] == -1:
            logging.info(f"Case 3b:  Adding {id2} to network {is_contained[0]}")
            networks[is_contained[0]].append(id2)
            logging.info(networks[is_contained[0]])

            # Case 4:  Points are contained in different networks.  Combine the networks.
        elif is_contained[0] >= 0 and is_contained[1] >= 0:
            logging.info(
                f"Points ({id1}, {id2}) found in different networks.  Combining the networks."
            )

            temp = networks[is_contained[1]].copy()
            networks[is_contained[0]].extend(temp)
            del networks[is_contained[1]]

            logging.info(f"{len(networks)} networks exist.")

        else:
            logging.error(
                f"Unexpected combination of points contained in networks:  {is_contained}"
            )
            raise ValueError

        ## Break conditions
        # Part 1:  Stop after generating a certain number of connections
        if problem_part == 1 and n == num_connections - 1:
            break

        # Part 2:  Stop when all points are contained within a single network
        if problem_part == 2 and len(networks) == 1 and len(networks[0]) == len(pts):
            logging.info(
                f"All points connected.  Breaking.  Last point:  ({pts[id1]}, {pts[id2]})"
            )
            break

    return networks, (id1, id2)


# Part 1
p1_networks, _ = connect(distances, num_connections=num_connections, problem_part=1)
p1_networks.sort(key=len, reverse=True)

# Compute Part 1 answer
p1_n_terms, p1 = 3, 1
for i in range(p1_n_terms):
    p1 *= len(p1_networks[i])

logging.info(f"{'Solution to Part 1:':<20} {p1}")

# Part 2
p2_networks, last_points = connect(distances, num_connections=-1, problem_part=2)
p2_networks.sort(key=len, reverse=True)

# Compute Part 2 answer
p2 = pts[last_points[0]][0] * pts[last_points[1]][0]
logging.info(f"{'Solution to Part 2:':<20} {p2}")
