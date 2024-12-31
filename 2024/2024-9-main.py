import sys

infile = sys.argv[1] if len(sys.argv)>=2 else './data/9.in'
temp = open(infile).read().strip()

# Test datasets
#temp = '12345'
#temp = '2333133121414131402'

data = [int(x) for x in temp]

print("Original data:\n" + str(data))


def expand(data):
    """Expand compacted representation of file system"""
    new = []
    for i, val in enumerate(data):
        if i % 2 != 0:
            for ii in range(val):
                new.append('.')
        else:
            for ii in range(val):
                new.append(str(int((i / 2))))

    return new


def rearrange(exp):
    """Part 1 rearrangement scheme"""
    while True:
        id1 = exp.index('.')  # find first blank
        # Find last populated
        for i, val in enumerate(reversed(exp)):
            if val != ".":
                id2 = len(exp) - i - 1
                break

        # Swap values
        exp[id1] = exp[id2]
        exp[id2] = '.'

        # Break when indices are separated by one (i.e. populated and unpopulated are completely separated)
        if id2 - id1 == 1:
            return exp


def check_sum(data):
    """Compute check sum."""
    cs = 0
    for i, val in enumerate(data):
        if val != '.':
            cs += i * int(val)
    return cs


def rearrange_blocks(data):
    """Part 2 rearrangement scheme (keeping contiguous block intact)"""

    start = max(data)

    for val in [int(start) - x for x in range(int(start))]:
        # Find extent of block
        id1 = data.index(str(val))
        id2 = len(data) - data[::-1].index(str(val)) - 1
        size = id2 - id1 + 1  # block size

        #print(f"{val}:  id1 = {id1}, id2 = {id2}")

        for i in range(id1):
            # Find a space large-enough to fit block
            fits = True
            for ii in range(size):
                if data[i + ii] != '.':
                    fits = False

            # Move block and replace with '.'
            if fits:
                for ii in range(size):
                    data[i + ii] = str(val)
                    data[id1 + ii] = "."

                #print(data)
                break


    return data


data2 = expand(data.copy())
#print("\nExpanded data:\n" + str(data2))

data3 = rearrange(data2.copy())

#print("\nRearranged data:\n" + str(data3))

p1 = check_sum(data3)

print(f"{'\nSolution to Part 1:':<20} {p1}")

## Part 2:
data4 = rearrange_blocks(data2.copy())

p2 = check_sum(data4)
print(f"{'Solution to Part 2:':<20} {p2}")
