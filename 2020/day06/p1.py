# extract input from file
with open('input.txt', 'r') as f:
    lines = [x.rstrip() for x in f.readlines()] + ['']

count = 0
group = set()
for line in lines:
    # line is empty
    if not line:
        # increase count
        count += len(group)
        # reset group set
        group = set()
        continue
    
    for char in line:
        # store unique characters
        group.add(char)

print(count)
