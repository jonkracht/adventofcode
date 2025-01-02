import sys

infile = sys.argv[1] if len(sys.argv)>=2 else './data/11.in'

raw = open(infile).read().strip()

data = [int(x) for x in raw.split()]

# Test datasets
#data = [0, 1, 10, 99, 999]
#data = [125, 17]
data = list(raw[0])

print(data)

def blink(stones):
    """Perform actions."""
    
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


num_blinks = 25


history = []
history.append(data)

for i in range(num_blinks):
    print(i)
    history.append(blink(history[-1].copy()))
    #print(history[-1])


p1 = len(history[-1])

print(f"{'Solution to Part 1:':<20} {p1}")


# Part 2

num_blinks = 75

history = []
history.append(data)

for i in range(num_blinks):
    print(i)
    history.append(blink(history[-1].copy()))
    print(len(history[-1]))


p2 = len(history[-1])

print(f"{'Solution to Part 2:':<20} {p2}")
