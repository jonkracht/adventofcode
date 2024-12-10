import sys
import re

# Load data
infile = sys.argv[1] if len(sys.argv)>=2 else './data/3.in'
data = open(infile).read().strip()


def multiply(string):
    """Perform multiplication on formatted strings"""

    halves = string.split(',')
    
    return int(halves[0].split('(')[1]) * int(halves[1].split(')')[0])


def find_patterns(string):
    return re.findall("mul\([0-9]*[0-9],[0-9]*[0-9]\)", string) 


# Part 1:
matches = find_patterns(data)

p1 = 0
for m in matches:
    p1 += multiply(m)

print("Part 1 answer: " + str(p1))


# Part 2:
p2 = 0
block = data

while True:
    dont_split = block.split("don\'t", 1)

    for pattern in find_patterns(dont_split[0]):
        p2 += multiply(pattern)
    
    # Break if "don't()" does not appear in block
    if len(dont_split) == 1:
        break
    else:
        do_split = split[1].split("do()", 1)
        
        # If 'do()' does not appear in string break
        if len(do_split) == 1:
            break
        else:
            block = do_split[1]


print("Part 2 answer: " + str(p2))
