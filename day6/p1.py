import string
alpha = string.ascii_lowercase
with open("input.txt", "r") as f:
    lines = f.readlines()
    num_lines = len(lines)
    count = 0
    yes = set()
    for row, line in enumerate(lines):
        if line != '\n':
            for char in line:
                if char in alpha:
                    yes.add(char)
        if line == '\n' or row == num_lines - 1:
            # count
            count += len(yes)
            # reset
            yes = set()
    print(count)
