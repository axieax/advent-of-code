# extract input from file
with open('input.txt', 'r') as f:
    lines = [x.rstrip() for x in f.readlines()] + ['']

# required fields
required = sorted(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
count = 0
current_passport = []
for line in lines:
    # empty line
    if not line:
        # check passport contains all the required keys
        if sorted(current_passport) == required:
            count += 1
        # reset current_passport fields
        current_passport = []
        continue
    # attempt to find keys
    for pair in line.split(' '):
        # pair is in the format 'field:value'
        key = pair.split(':')[0]
        # append required keys to current_passport
        if key in required:
            current_passport.append(key)
print(count)
