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
        original_key = int(values[0][4:-1])
        value = int(values[1])
        # list of all key combinations
        keys = [0]
        for i in range(36):
            if mask[i] == '0':
                # keep original bit from original key
                new = (original_key >> (36 - i - 1)) & 1
                # update each key combination with this bit
                keys = [(key << 1) | new for key in keys]
            elif mask[i] == '1':
                # update each key combination with the '1' bit
                keys = [(key << 1) | 1 for key in keys]
            else:
                # generate more key combinations, including existing keys with an additional
                # '0' bit as well as existing keys with an additional '1' bit
                keys = [(key << 1) | 0 for key in keys] + [(key << 1) | 1 for key in keys]

        # update memory
        for key in keys:
            memory[key] = value

# calculate sum of values
print(sum(memory.values()))
