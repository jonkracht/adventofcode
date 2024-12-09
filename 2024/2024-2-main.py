def check(report):
    """Checks individual report and return Boolean of its safety."""

    # Determine direction change of first two elements 
    delta = report[1] - report[0]
    if delta == 0:
        return False
    elif delta > 0:
        is_increasing = True
    else:
        is_increasing = False

    for i in range(1, len(report)):
        
        change = report[i] - report[i-1]

        if abs(change) > 3 or change == 0:
            return False
        
        # Check if delta is consistent
        if is_increasing != (change > 0):
            return False

    return True


def main():
    
    # Load data
    with open('data/2.in', 'r') as file:
        raw_data = file.read()

    # Format data into lists
    raw_data = raw_data.split('\n')

    # Remove empty entries
    raw_data = [x for x in raw_data if x]
    

    # Convert nested list entries integer type rather than strings
    data = []
    for r in raw_data:
        data.append([int(num) for num in r.split()])

    # Iterate over rows in data
    number_safe, number_dampened_safe = 0, 0

    for d in data:
       
        if check(d):
            number_safe += 1

        # Check Problem Dampener criteria
        dampened_safe = False

        for i in range(len(d)):

            if check(d[:i] + d[i+1:]):
                dampened_safe = True
                break

        if dampened_safe:
            number_dampened_safe += 1

    print(f"\nOf {len(data)} reports, {str(number_safe)} are safe." ) 
    print(f"\nOf {len(data)} reports, {str(number_dampened_safe)} are dampened safe." ) 


if __name__ == "__main__":
    main()
