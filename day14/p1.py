with open('input.txt', 'r') as f:
    lines = [x.rstrip() for x in f.readlines()]

memory = {}
mask = 0
for line in lines:
    # mask
    if line.startswith('mask'):
        mask = line[7:]
    # mem
    else:
        values = line.split(' = ')
        key = int(values[0][4:-1])
        value = int(values[1])
        modified = 0
        for i in range(36):
            new = mask[i]
            if new == 'X':
                new = (value >> (36 - i - 1)) & 1
            else:
                new = int(new)
            modified = (modified << 1) | new
        memory[key] = modified
# calculate sum
print(sum(memory.values()))
