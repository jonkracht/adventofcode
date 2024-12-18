import sys

infile = sys.argv[1] if len(sys.argv)>=2 else './data/7.in2'

data = open(infile).read().strip().split('\n')

# Number of factors range from 3 to 12 

def could_total(n1, n2, total):
    """"""
    if n1 + n2 == total
        return True
    elif n1 * n2 == total
        return True
    else:
        return False

p1 = 0

for d in data:
    temp = d.split(":")
    total = int(temp[0])
    
    nums = [int(x) for x in temp[1].split()]

    new_total = total
    while len(nums) > 0:
        if new_total % nums[-1] != 0:
            # Only addition is possible
            new_total = total - nums[-1]
            nums.pop()


print(min_nums)
print(max_nums)


#print(f"{'Solution to Part 1:':<20} {p1}")
#print(f"{'Solution to Part 2:':<20} {p2}")
