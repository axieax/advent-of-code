# extract input from file
with open('input.txt', 'r') as f:
    lines = [x.rstrip() for x in f.readlines()]

memory = {}
mask = 0
for line in lines:
    # mask instruction
    if line.startswith('mask'):
        # extract mask
        mask = line[7:]
    # update memory instruction
    else:
        values = line.split(' = ')
        key = int(values[0][4:-1])
        value = int(values[1])
        # calculate modified value
        modified_value = 0
        for i in range(36):
            new = mask[i]
            if new == 'X':
                # keep original bit from value
                new = (value >> (36 - i - 1)) & 1
            else:
                # use 0 or 1 respectively
                new = int(new)
            # update modified value bit by bit
            modified_value = (modified_value << 1) | new

        # update memory
        memory[key] = modified_value

# calculate sum of values
print(sum(memory.values()))
