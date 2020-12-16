# extract input from file
with open('input.txt', 'r') as f:
    lines = [x.rstrip() for x in f.readlines()]

# convert rules to dict
rules = {}
for rule in lines[:20]:
    field_name = rule.split(': ')[0]
    first_criteria = rule.split(': ')[1].split(' or ')[0]
    range_one_min = int(first_criteria.split('-')[0])
    range_one_max = int(first_criteria.split('-')[1])
    second_criteria = rule.split(': ')[1].split(' or ')[1]
    range_two_min = int(second_criteria.split('-')[0])
    range_two_max = int(second_criteria.split('-')[1])
    rules[field_name] = [(range_one_min, range_one_max), (range_two_min, range_two_max)]

# absolute minimum and maximum range
min_range = min(criteria[0] for rule in rules.values() for criteria in rule)
max_range = max(criteria[1] for rule in rules.values() for criteria in rule)

# calculate ticket scanning error rate
invalid = 0
for line in lines[25:]:
    fields = [int(x) for x in line.split(',')]
    for field in fields:
        if field not in range(min_range, max_range + 1):
            invalid += field

print(invalid)
