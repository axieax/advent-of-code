import math

# with open("sample.txt") as f:
with open("input.txt") as f:
    data = [x.strip() for x in f.readlines()]

# map each position
gamma = 0
epsilon = 0
for digit_position in range(len(data[0])):
    bits = [line[digit_position] for line in data]
    # find most common bit
    num0 = num1 = 0
    for bit in bits:
        num0 += bit == "0"
        num1 += bit == "1"
    gamma = (gamma << 1) | (num1 > num0)
    epsilon = (epsilon << 1) | (num0 > num1)

# get significant bit mask
# most significant bit: ceil(2 ** msb) = gamma
# msb = math.floor(math.log(gamma, 2))
# mask = int("1" * (msb + 1), 2)

# epsilon is gamma flipped (bitwise)
# epsilon = ~gamma & mask

power = gamma * epsilon

print(f"{gamma=}")
print(f"{epsilon=}")
print(f"{power=}")
