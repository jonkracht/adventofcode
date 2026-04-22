"""
# Problem description

## Part 1

## Part 2

"""

import logging
import sys

logging.basicConfig(level=logging.INFO)

infile = sys.argv[1] if len(sys.argv) >= 2 else "./inputs/9.in"

input = open(infile).read().strip().split("\n")
input = [tuple(int(ii) for ii in i.split(",")) for i in input]
logging.info(f"Input points:  {input}")

best = 0
for i in range(len(input)):
    for ii in range(i):
        logging.info(f"Checking {input[i]} and {input[ii]}.")

        # Area calculation is inclusive of endpoints
        area = (abs(input[i][0] - input[ii][0]) + 1) * (
            abs(input[i][1] - input[ii][1]) + 1
        )
        logging.info(f"Area computed as:  {area}")

        if area > best:
            best = area
            logging.info(f"**** Found new best:  {best}")

print(best)
# print(f"{'Solution to Part 1:':<20} {p1}")
# print(f"{'Solution to Part 2:':<20} {p2}")
