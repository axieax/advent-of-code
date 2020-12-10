required = sorted(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
with open("input.txt", "r") as f:
    lines = f.readlines()
    total_lines = len(lines)
    count = 0

    curr_has = []
    for row, line in enumerate(lines):
        for pair in line.split(' '):
            key = pair.split(':')[0]
            if key in required:
                curr_has.append(key)
        if line == '\n' or row == total_lines - 1:
            # check
            if sorted(curr_has) == required:
                count += 1
            # reset
            curr_has = []
            continue
    print(count)
