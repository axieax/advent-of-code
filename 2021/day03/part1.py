from collections import Counter

with open("input.txt") as f:
    data = [x.strip() for x in f.readlines()]

gamma = 0
epsilon = 0
for digit_position in range(len(data[0])):
    # find most common bit
    bits = [int(line[digit_position]) for line in data]
    mcb = Counter(bits).most_common(1)[0][0]
    gamma = (gamma << 1) | mcb
    epsilon = (epsilon << 1) | (~mcb & 1)

power = gamma * epsilon
print(f"{gamma=}")
print(f"{epsilon=}")
print(f"{power=}")
