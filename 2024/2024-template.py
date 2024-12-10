import sys

infile = sys.argv[1] if len(sys.argv)>=2 else './data/3.in'

data = open(infile).read().strip()

print(data)
