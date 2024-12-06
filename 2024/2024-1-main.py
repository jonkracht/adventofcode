import numpy as np

with open('input/2024-1.in', 'r') as file:
    dataString = file.read()

# Split block of text into two lists
left, right = [], []
for d in dataString.split('\n'):
    if d: # exclude empty rows
        l, r = d.split()
        left.append(int(l))
        right.append(int(r))

left.sort()
right.sort()

dist = 0
for l, r in zip(left, right):
    dist += abs(l-r)

print('Part One:  Distance between lists is ' + str(dist))


# Part Two:  Compute similarity score

SS = 0

for l in left:
    SS += l * right.count(l)

print("Part Two:  Similarity score between the lists is " + str(SS))
