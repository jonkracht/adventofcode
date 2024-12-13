import sys

infile = sys.argv[1] if len(sys.argv)>=2 else './data/4.in'
data = open(infile).read().strip()
data = data.split("\n")



print("Sanity check data format:")

n_rows = len(data)
print(f"Number of rows in data: {n_rows}")

n_cols = []
for d in data:
    n_cols.append(len(list(d)))

#print(f"Columns in each row:\n {n_cols}")

n_cols = len(list(data[0]))



def count_strings(string, strings_to_find):
    """Count instances of a smaller string in a longer one."""

    char_list = list(string)
    
    count = 0

    for i in range(len(char_list)):
        if ''.join(char_list[i:i+4]) in strings_to_find:
            count += 1

    return count


strings_to_find = ['XMAS', 'SAMX']

p1 = 0


# Rows

for row in data:
    p1 += count_strings(''.join(row), strings_to_find)

print(f"Found {p1} instances in rows")

# Columns
for j in range(n_cols):
    col = []
    for i in range(n_rows):
        col.append(list(data[i])[j])

    p1 += count_strings(''.join(col), strings_to_find)



# Diaganols

# / diagonals - sum of indices are equal on these diagonals

for idx_sum in range(0, (n_rows - 1) + (n_cols - 1)):
    diag = ''
    i, j = idx_sum, 0

    while True:

        if i > n_rows - 1:
            j = i - (n_rows - 1)
            i = n_rows - 1
 
        # Break when reach edge of data
        if i < 0 or j > n_cols - 1:
            break

        diag += data[i][j]
        
        # Increment indices
        i += -1
        j += 1

    #print(diag)
    p1 += count_strings(diag, strings_to_find)


# \ diagonals - difference in indices are equal on these diaganols

for idx_diff in range(-(n_rows-1), n_rows):
    diag = ''

    #print(idx_diff)
    if idx_diff <= 0:
        i, j = 0, -idx_diff
    else:
        i, j = idx_diff, 0


    while True:
        if i > n_rows - 1 or j > n_cols - 1:
           break
        
        diag += data[i][j]
        
        i += 1
        j += 1


    p1 += count_strings(diag, strings_to_find)

print(f"Answer to Part 1: {p1}")



# Part 2:  Find instances of crossed "MAS" pattern, in any of four configurations

'''  
M.S
.A.
M.S
'''

p2 = 0

# Raster scan for top left character of pattern
for i in range(n_rows - 2):
    for j in range(n_cols - 2):
        
        # Check for pattern with top row "M.S"
        if data[i][j] == "M" and data[i + 1][j + 1] == "A" :
            if data[i][j+2] == "S" and data[i+2][j] == "M" and data[i+2][j+2] == "S":
                p2 += 1

        # Check for pattern with top row "S.S"
        if data[i][j] == "S" and data[i + 1][j + 1] == "A" :
            if data[i][j+2] == "S" and data[i+2][j] == "M" and data[i+2][j+2] == "M":
                p2 += 1


        # Check for pattern with top row "S.M"
        if data[i][j] == "S" and data[i + 1][j + 1] == "A":
           if data[i][j+2] == "M" and data[i+2][j] == "S" and data[i+2][j+2] == "M":
                p2 += 1

        # Check for pattern with top row "M.M"
        if data[i][j] == "M" and data[i + 1][j + 1] == "A" :
            if data[i][j+2] == "M" and data[i+2][j] == "S" and data[i+2][j+2] == "S":
                p2 += 1

       
# An alternative strategy is to rotate the puzzle by 90 degrees and search for the pattern rather than searching for rotated versions of the pattern
        
print(f"Part 2 answer: {p2}")
