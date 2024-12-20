import sys

infile = sys.argv[1] if len(sys.argv)>=2 else './data/7.in'

data = open(infile).read().strip().split('\n')


def next_blank(ops):
    """Find next empty blank starting from the end of list."""
    try:
        idx = len(ops) - ops[::-1].index('') - 1
        return idx
    except:
        return -1


def is_valid(subtotal, nums, ops, i, op):
    """Checks if a function is a candidate at a location."""
    
    # Get total from previously placed operations
    for ii in range(len(ops) - 1, i, -1):
        if ops[ii] == "+":
            subtotal -= nums[ii+1]

        elif ops[ii] == "*":
            subtotal = int(subtotal / nums[ii+1])
        else:
            print("Unexpected operation")
            print(op)
            return False
    
    # Check addition
    if op == "+":
        if i == 0:
            return subtotal == nums[0] + nums[1]
        else:
            return nums[i + 1] < subtotal

    # Check multiplication
    elif op == "*":
        if i == 0:
            return subtotal == nums[0] * nums[1]
        else:
            return subtotal % nums[i + 1] == 0  # must be a divisor


def solve(total, numbers, ops):
    i = next_blank(ops)

    if i == -1:
        #print(ops)
        return True

    for op in ["+", "*"]:
        if is_valid(total, numbers, ops, i, op):
            ops[i] = op
            #print(ops)

            if not solve(total, numbers, ops):
                ops[i] = ''
                #print(ops)
            else:
                return True

    return False

# Part 1:
p1 = 0

for d in data:
    total, nums = d.split(":")
    nums = [int(x) for x in nums.split()]
    total = int(total)

    operations = [''] * (len(nums) - 1)

    #print(f"\n{total}: {nums}")
    result = solve(total, nums, operations)
    #print(result)

    if result:
        p1 += total

# Test cases
#total, nums = 292, [11, 6, 16, 20]
#total, nums = 3267, [81, 40, 27]
#total, nums = 36, [4, 2, 2, 3]

#print(f"\n{total}: {nums}")
solve(total, nums, [''] * (len(nums) - 1))


print(f"{'Solution to Part 1:':<20} {p1}")


# Part 2:  A new concatenation operation is allowed

def p2Valid(total, nums, ops, i, op):
    """Checks if a function is a candidate at a location."""

    # Get total from previously placed operations
    for ii in range(len(ops) - 1, i, -1):
        if ops[ii] == "+":
            total -= nums[ii + 1]

        elif ops[ii] == "*":
            total = int(total / nums[ii + 1])

        elif ops[ii] == "|":
            num_digs = len([x for x in str(nums[ii + 1])])
            total = int("".join([x for x in str(total)][0:-num_digs]))

        else:
            print("Unexpected operation")
            print(op)
            return False

    # Check addition
    if op == "+":
        if i == 0:
            return total == nums[0] + nums[1]
        else:
            return nums[i + 1] < total

    # Check multiplication
    elif op == "*":
        if i == 0:
            return total == nums[0] * nums[1]
        else:
            return total % nums[i + 1] == 0  # must be a divisor

    # Check concatenation
    elif op == "|":
        if i == 0:
            return total == int(str(nums[0]) + str(nums[1]))
        else:
            num_digs = len([x for x in str(nums[i + 1])])
            return nums[i + 1] == int("".join(list(str(total))[-num_digs:]))



def p2solve(total, nums, ops):
    i = next_blank(ops)

    if i == -1:
        #print(ops)
        return True

    for op in ["+", "*", "|"]:
        if p2Valid(total, nums, ops, i, op):
            ops[i] = op
            #print(ops)

            if not p2solve(total, nums, ops):
                ops[i] = ''
                #print(ops)
            else:
                return True

    return False

p2 = 0

maths = {}

for d in data:
    total, nums = d.split(":")
    nums = [int(x) for x in nums.split()]
    total = int(total)

    operations = [''] * (len(nums) - 1)

    #print(f"\n{total}: {nums}")
    result = p2solve(total, nums, operations)
    #print(result)

    if result:
        p2 += total
        temp = {}

print(f"{'Solution to Part 2:':<20} {p2}")

