# extract input from file
with open('input.txt', 'r') as f:
    adapters = sorted([int(x) for x in f.readlines()])
    adapters = [0] + adapters + [adapters[-1] + 3]

# count number of differences of one and three respectively
differences = [x - adapters[i - 1] for i, x in enumerate(adapters) if i > 0]
print(differences.count(1) * differences.count(3))
