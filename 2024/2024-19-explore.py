import sys, copy

infile = sys.argv[1] if len(sys.argv)>=2 else './data/19.in'

raw = open(infile).read().strip()

pieces, whole = raw.split('\n\n')

pieces = [p.strip() for p in pieces.split(',')]
#print(f"\nPieces:\n{pieces}")

whole = whole.split('\n')
#print(f"\nWhole:\n{whole}")

for p in sorted(pieces):
    print(p)
