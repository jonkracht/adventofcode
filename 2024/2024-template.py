import sys

infile = sys.argv[1] if len(sys.argv)>=2 else './data/3.in'

data = open(infile).read().strip()

print(data)



#print(f"{'Solution to Part 1:':<20} {p1}")
#print(f"{'Solution to Part 2:':<20} {p2}")
