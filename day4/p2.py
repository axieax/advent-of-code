def valid_byr(year):
    return len(year) == 4 and (1920 <= int(year) <= 2002)

def valid_iyr(year):
    return len(year) == 4 and (2010 <= int(year) <= 2020)

def valid_eyr(year):
    return len(year) == 4 and (2020 <= int(year) <= 2030)

def valid_hgt(height):
    measurement = height[-2:]
    if measurement != 'cm' and measurement != 'in':
        return False
    num = int(height[:-2])
    if measurement == 'cm' and (150 <= num <= 193):
        return True
    if measurement == 'in' and (59 <= num <= 76):
        return True
    return False

def valid_hcl(hair_colour):
    return hair_colour[0] == '#' and all(map(lambda x: ('0' <= x <= '9') or ('a' <= x <= 'f'), hair_colour[1:]))

def valid_ecl(eye_colour):
    valid = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return eye_colour in valid

def valid_pid(passport_id):
    # does not check it is a num
    return len(passport_id) == 9

required = sorted(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
with open("input.txt", "r") as f:
    lines = f.readlines()
    total_lines = len(lines)
    count = 0

    curr_has = []
    for row, line in enumerate(lines):
        if line != '\n':
            for pair in line.split(' '):
                key = pair.split(':')[0]
                val = pair.split(':')[1].rstrip()
                if key in required:
                    if (key == 'byr' and valid_byr(val)) or (key == 'iyr' and valid_iyr(val)) or (key == 'eyr' and valid_eyr(val)) or (key == 'hgt' and valid_hgt(val)) or (key == 'hcl' and valid_hcl(val)) or (key == 'ecl' and valid_ecl(val)) or (key == 'pid' and valid_pid(val)):
                        curr_has.append(key)
        if line == '\n' or row == total_lines - 1:
            # check
            if sorted(curr_has) == required:
                count += 1
            # reset
            curr_has = []
            continue
    print(count)
