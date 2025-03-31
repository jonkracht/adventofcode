import sys

infile = sys.argv[1] if len(sys.argv)>=2 else './data/21.in'

codes = open(infile).read().strip().split()
print(codes)


# Geometry of columns expressed in row/column notation
num_pad = {'7': (0, 0), '8': (0, 1), '9': (0, 2), '4': (1, 0), '5': (1, 1), '6': (1, 2), '1':(2, 0), '2': (2, 1), '3': (2, 2), '0': (3, 1), 'A': (3, 2)}
dir_pad = {'^': (0, 1), 'A': (0, 2), '<': (1, 0), 'v': (1, 1), '>': (1, 2)}

start_loc = (3, 2)  # 'A'


def get_numpad_actions(chars: list, loc: tuple) -> list:
    """"""
    
    cmd = []

    for cc in list(chars):

        button_loc = num_pad[cc]
        #print(f"\nCurrent location is {loc}.  Target button is {cc} which is located at {button_loc}.")

        dely, delx = button_loc[0] - loc[0], button_loc[1] - loc[1]
        #print(f"Delta is ({delx}, {dely})")
        
        if delx != 0:
            if delx > 0:
                for _ in range(delx):
                    cmd.append('>')
            else:
                for _ in range(abs(delx)):
                    cmd.append('<')
        if dely != 0:
            if dely > 0:
                for _ in range(dely):
                    cmd.append('v')
            else:
                for _ in range(abs(dely)):
                    cmd.append('^')
       
        #print(f"Command following this button:  {cmd}")   
        cmd.append('A')
        loc = button_loc

    return cmd


def get_dirpad_actions(chars: list, loc: tuple):
    """"""
        
    cmd = []

    for cc in list(chars):

        button_loc = dir_pad[cc]
        #print(f"\nCurrent location is {loc}.  Target button is {cc} which is located at {button_loc}.")

        dely, delx = button_loc[0] - loc[0], button_loc[1] - loc[1]
        #print(f"Delta is ({delx}, {dely})")
        
        if delx != 0:
            if delx > 0:
                for _ in range(delx):
                    cmd.append('>')
            else:
                for _ in range(abs(delx)):
                    cmd.append('<')
        if dely != 0:
            if dely > 0:
                for _ in range(dely):
                    cmd.append('v')
            else:
                for _ in range(abs(dely)):
                    cmd.append('^')
       
        #print(f"Command following this button:  {cmd}")   
        cmd.append('A')
        loc = button_loc

    return cmd


codes = ['029A', '980A', '179A', '456A', '379A']
#codes =  ['029A']
presses = {}

for c in codes:
    print(f"\n\n*** Code {c} ***")

    numpad_moves = get_numpad_actions(c, start_loc)
    dirpad_moves_1 = get_dirpad_actions(numpad_moves, (0, 2))
    dirpad_moves_2 = get_dirpad_actions(dirpad_moves_1, (0, 2))

    print(f"\nNumpad moves:\n{''.join(numpad_moves)}")
    print(len(numpad_moves))

    print(f"\nDirpad moves 1:\n{''.join(dirpad_moves_1)}")
    print(len(dirpad_moves_1))
    
    print(f"\nDirpad moves 2:\n{''.join(dirpad_moves_2)}")
    print(len(dirpad_moves_2))

    presses[c] = dirpad_moves_2

       
'''
p1_complexity = 0
for k, v in presses.items():
    print(f"{k}:  {len(v)}")
    p1_complexity += len(v) * int(k.split('A')[0]) 

print(p1_complexity)
'''


#print(f"{'Solution to Part 1:':<20} {p1}")
#print(f"{'Solution to Part 2:':<20} {p2}")
