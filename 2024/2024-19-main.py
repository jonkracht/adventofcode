import sys, copy

infile = sys.argv[1] if len(sys.argv)>=2 else './data/19.in'

raw = open(infile).read().strip()

d, s = raw.split('\n\n')

dictionary = [dd.strip() for dd in d.split(',')]
print(f"\nDictionary:\n{dictionary}")

strings = s.split('\n')
print(f"\nStrings to assemble:\n{strings}")


def ways(s: str):
    """Compute number of ways string can be formed from dictionary words using dynamic programming (memoization)."""

    #print(f"\nWays called with '{s}'.")

    # Base case (simply lookup states previously computed)
    if s in seen:
        #print(f"Previously seen:  {s}")
        return seen[s]

    counts[s] = 0

    # Check beginning of against dictionary
    for d in dictionary:
        if d == s[:len(d)]:
            
            #print(f"Match found:  {d}")
            
            if len(d) != len(s):
                counts[s] += ways(s[len(d):])
            
            else:
                counts[s] += 1

    seen[s] = counts[s]

    return counts[s]


seen, counts, unique_ways = dict(), dict(), dict()

for s in strings:
    #print(f"\nConstructing '{w}'\n")
    unique_ways[s] = ways(s)

p1 = sum([x != 0 for x in unique_ways.values()])
p2 = sum([x for x in unique_ways.values()])

print(f"\n{'Solution to Part 1:':<20} {p1}")
print(f"{'Solution to Part 2:':<20} {p2}")
