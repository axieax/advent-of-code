from functools import reduce
import string
alpha = string.ascii_lowercase
with open("input.txt", "r") as f:
    lines = f.readlines()
    num_lines = len(lines)
    count = 0
    # store everyone's responses
    responses = []
    for row, line in enumerate(lines):
        yes = set()
        if line != '\n':
            for char in line:
                if char in alpha:
                    yes.add(char)
            responses.append(yes)
        if line == '\n' or row == num_lines - 1:
            # count - responses is a list of sets
            common = reduce(lambda x, y: x.intersection(y), responses)
            count += len(common)
            # reset
            responses = []
    print(count)
