import sys

infile = sys.argv[1] if len(sys.argv)>=2 else './data/5.in'

data = open(infile).read().strip()

data = data.split("\n\n")

rules = data[0].split("\n")
reports = data[1].split("\n")

print(f"{len(rules)} rules")
print(f"{len(reports)} reports")


# Format reports as list of lists
report_list = []
for r in reports:
    report_list.append(r.split(','))

# Format rules as a list of tuples
rule_list = []
for r in rules:
    temp = r.split("|")
    rule_list.append(tuple((temp[0], temp[1])))


def check_rule(report, rule):
    """"""
    if (rule[0] in report) and (rule[1] in report):
        if report.index(rule[0]) > report.index(rule[1]):
            return False
        else:
            return True
    else:
        return True


def check_report(report, rules):
    """"""

    for r in rules:
        if not check_rule(report, r):
            return False

    return True


correct_reports, incorrect_reports = [], []

for r in report_list:
    if check_report(r, rule_list):
        correct_reports.append(r)
    else: 
        incorrect_reports.append(r)

#print("Correct reports")
#print(correct_reports)

p1 = 0

def sum_middle_elements(report_list):
    total = 0
    for r in report_list:
        idx = int((len(r) - 1) / 2)
        total += int(r[idx])

    return total

p1 = sum_middle_elements(correct_reports)

print(f"{'Solution to Part 1:':<20} {p1}")

# Part 2:  Fix incorrect reports

def reorder_report(report, rules):
    '''Reorder a report based on information in rules'''
    
    for rule in rules:
        if not check_rule(report, rule):
            
            # If rule is violated, swap elements.  Does this generate unique solutions?

            #print(f"{report}:  {rule} violated.  Swapping elements.")
            idx1, idx2 = report.index(rule[0]), report.index(rule[1])
            
            temp = report[idx1]
            report[idx1] = report[idx2]
            report[idx2] = temp

    return report


reordered_reports = []

for i in incorrect_reports:
    while True:
        new = reorder_report(i, rule_list)
    
        if check_report(new, rule_list):
            reordered_reports.append(new)
            break

p2 = sum_middle_elements(reordered_reports)
print(f"{'Solution to Part 2:':<20} {p2}")
