import sys
import re
from collections import defaultdict, Counter, deque
#import pyperclip as pc
def pr(s):
    print(s)
    #pc.copy(s)
sys.setrecursionlimit(10**6)
infile = sys.argv[1] if len(sys.argv)>=2 else 'data/6.in'
p1 = 0
p2 = 0
D = open(infile).read().strip()

G = D.split('\n')
R = len(G)
C = len(G[0])

# Locate starting position/direction
for r in range(R):
    for c in range(C):
        if G[r][c] == '^':
            sr,sc = r,c

# Loops are over potential locations of obstacle to cause looping
for o_r in range(R):
    for o_c in range(C):
        r,c = sr,sc
        d = 0 # 0=up, 1=right, 2=down, 3=left
        
        # Initialize some sets to hold route points
        SEEN = set()
        SEEN_RC = set()
        while True:

            # Check if configuration has previously existed
            if (r,c,d) in SEEN:
                p2 += 1
                break
            
            # If loop is not broken at previous step, add state to previous
            SEEN.add((r,c,d))
            SEEN_RC.add((r,c))

            # Define position changes
            dr,dc = [(-1,0),(0,1),(1,0),(0,-1)][d]
            
            # Compute potential next location
            rr = r+dr
            cc = c+dc
            
            # If new location is exiting map            
            if not (0<=rr<R and 0<=cc<C):
                if G[o_r][o_c]=='#':
                    p1 = len(SEEN_RC)
                break
            
            # If new location has obstacle, change direction
            if G[rr][cc]=='#' or rr==o_r and cc==o_c:
                d = (d+1)%4
            else:
                r = rr
                c = cc
pr(p1)
pr(p2)
