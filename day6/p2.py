from functools import reduce

# extract input from file
with open("input.txt", "r") as f:
    lines = [x.rstrip() for x in f.readlines()] + ['']

# store everyone's responses
responses = []
count = 0
for line in lines:
    # line is empty
    if not line:
        # common (set) is the intersection of all sets in responses (list of sets)
        common = reduce(lambda x, y: x.intersection(y), responses)
        count += len(common)
        # reset responses
        responses = []
        continue

    # add set to responses
    group = set(line)
    responses.append(group)

print(count)
