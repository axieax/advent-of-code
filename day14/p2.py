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
        original_key = int(values[0][4:-1])
        value = int(values[1])
        keys = [0]
        address = 0
        for i in range(36):
            if mask[i] == '0':
                new = (original_key >> (36 - i - 1)) & 1
                keys = [(key << 1) | new for key in keys]
            elif mask[i] == '1':
                keys = [(key << 1) | 1 for key in keys]
            else:
                keys = [(key << 1) | 1 for key in keys] + [(key << 1) | 0 for key in keys]
        for key in keys:
            memory[key] = value
# calculate sum
print(sum(memory.values()))
