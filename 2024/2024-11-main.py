import sys

infile = sys.argv[1] if len(sys.argv)>=2 else './data/11.in'

raw = open(infile).read().strip()

data = [int(x) for x in raw.split()]

# Test datasets
#data = [0, 1, 10, 99, 999]
#data = [125, 17]


def blink(stones):
    """Perform stone motion algorithm (does not use consolidation -- see blink2 definition below)"""
    
    new = []
    for s in stones:
        digits = list(str(s))
        if s == 0:
            new.append(1)
        
        elif (len(digits) % 2) == 0:
             
            # Add left digits
            l_digs = digits[0:int(0.5 * len(digits))]
            new.append(int(''.join(l_digs)))

            # Add right digits - remove leading zeros.
            r_digs = digits[int(0.5 * len(digits)):]

            while r_digs[0] == 0 and len(r_digs) > 1:
                r_digs.pop(0)

            new.append(int(''.join(r_digs)))

        else:
            new.append(s * 2024)

    return new


# Part 1:
num_blinks = 25

history = []  # track via list of lists
history.append(data)

for i in range(num_blinks):
    print(f"\nBlink {i} of {num_blinks}:")
    history.append(blink(history[-1].copy()))
    print(f"{len(history[-1])} items.")


p1 = len(history[-1])

print(f"\n{'Solution to Part 1:':<20} {p1}")


# Part 2:
# Previous scheme doesn't work as number of stones after 75 blinks is huge (ran through 40 blinks and number was in hundred of millions).
# Need to implement a pruning method.  Identify identical branches and consolidate.

num_blinks = 75

history = []
history.append({d:1 for d in data})

def blink2(stones):
    """Largely the same except uses dictionary to track count of each number to reduce list size."""
    
    new = []
    for val, ct in stones.items():
        digits = list(str(val))
        if val == 0:
            new.append((1, ct))
        
        elif (len(digits) % 2) == 0:
             
            # Add left digits
            l_digs = digits[0:int(0.5 * len(digits))]
            new.append((int(''.join(l_digs)), ct))

            # Add right digits - remove leading zeros.
            r_digs = digits[int(0.5 * len(digits)):]

            while r_digs[0] == 0 and len(r_digs) > 1:
                r_digs.pop(0)

            new.append((int(''.join(r_digs)), ct))

        else:
            new.append((val * 2024, ct))

    # Consolidate duplicates
    consolidated = {}
    for key, val in new:
        if key in consolidated.keys():
            old_val = consolidated[key]
            consolidated[key] = old_val + val
        else:
            consolidated[key] = val

    return consolidated


for i in range(num_blinks):
    
    state = blink2(history[-1].copy())

    print(f"\nBlink {i + 1} of {num_blinks}:  {str(sum(state.values())) + ' stones':<25}  ({len(state.keys())} unique)")
    
    history.append(state)


p2 = 0
for k, v in history[-1].items():
    p2 += v

print(f"\n{'Solution to Part 2:':<20} {p2}")  # 276 trillion.  Yikes.
