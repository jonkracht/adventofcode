"""
# Problem description

## Part 1
Given a group of points in 3D space, create networks by sequentially joining together the closest pairs.  After performing a given number of connections between the nodes, perform some arithmetic on the sizes of the largest networks.


## Part 2

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


distances = {}

for i in range(len(pts)):
    for ii in range(i):
        logging.info(f"Processing ({i}, {ii})")

        temp = distance(pts[i], pts[ii])
        logging.info(f"Computed distance:  {temp}")

        distances[(i, ii)] = temp

# Create ordered list
distances = [
    [k, v] for k, v in dict(sorted(distances.items(), key=lambda item: item[1])).items()
]


# Part 1 solution:
num_connections = 1000  # given in the problem definition
networks = []

logging.info("Begin generating networks")
for n in range(num_connections):

    pt1, pt2 = distances[n][0]

    logging.info(f"\nConnection {n}: {pt1} -> {pt2} [{pts[pt1]} -> {pts[pt2]}]")

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
        if pt1 in network:
            is_contained[0] = i
            logging.info(f"Found P1={pt1} in network {i}")

        if pt2 in network:
            is_contained[1] = i
            logging.info(f"Found P2={pt2} in network {i}")

    # Case 1:  Neither point lies within a network.  Create a new one.
    if is_contained[0] == -1 and is_contained[1] == -1:
        logging.info(
            f"Case 1 (neither point found): Creating new network [{pt1}, {pt2}]"
        )
        networks.append([pt1, pt2])
        logging.info(f"{len(networks)} networks exist.")

    # Case 2:  Both points already lie within the same network.  Do nothing.
    elif (
        is_contained[0] >= 0
        and is_contained[1] >= 0
        and is_contained[0] == is_contained[1]
    ):
        logging.info(
            f"Case 2 (both points [{pt1}, {pt2}] already reside in network {is_contained[0]}):  Doing nothing."
        )
        continue

        # Case 3a:  Pt2 lies with a network.  Add Pt1 to that network
    elif is_contained[0] == -1 and is_contained[1] >= 0:
        logging.info(f"Case 3a:  Adding {pt1} to network {is_contained[1]}")
        networks[is_contained[1]].append(pt1)
        logging.info(networks[is_contained[1]])

        # Case 3b:  Pt1 lies within a network.  Add Pt2 to that network.
    elif is_contained[0] >= 0 and is_contained[1] == -1:
        logging.info(f"Case 3b:  Adding {pt2} to network {is_contained[0]}")
        networks[is_contained[0]].append(pt2)
        logging.info(networks[is_contained[0]])

        # Case 4:  Points are contained in different networks.  Combine the networks.
    elif is_contained[0] >= 0 and is_contained[1] >= 0:
        logging.info(
            f"Points ({pt1}, {pt2}) found in different networks.  Combining the networks."
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


networks.sort(key=len, reverse=True)  # sort list for readability

logging.info(
    f"Network generation complete.  After constructing {num_connections} connections, {len(networks)} networks of length creater than one exist.  Networks made:"
)

for network in networks:
    logging.info(f"{network}  ({len(network)})")

p1_n_terms, p1 = 3, 1
for i in range(p1_n_terms):
    p1 *= len(networks[i])

logging.info(f"{'Solution to Part 1:':<20} {p1}")

# print(f"{'Solution to Part 2:':<20} {p2}")
