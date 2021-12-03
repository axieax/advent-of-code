# with open("sample.txt") as f:
with open("input.txt") as f:
    data = [x.strip() for x in f.readlines()]

# calculate oxygen rating
oxygen_data = data
num_digits = len(oxygen_data[0])
for digit_position in range(num_digits):
    if len(oxygen_data) == 1:
        break

    # find most common bit
    bits = [line[digit_position] for line in oxygen_data]
    num0 = num1 = 0
    for bit in bits:
        num0 += bit == "0"
        num1 += bit == "1"
    # keep 1 if even as well
    most_common_bit = "1" if num1 >= num0 else "0"

    # filter data
    oxygen_data = [
        line for line in oxygen_data if line[digit_position] == most_common_bit
    ]

oxygen_rating = int(oxygen_data[0], 2)
print(oxygen_rating)


# calculate co2 rating
co2_data = data
num_digits = len(co2_data[0])
for digit_position in range(num_digits):
    if len(co2_data) == 1:
        break

    # find most common bit
    bits = [line[digit_position] for line in co2_data]
    num0 = num1 = 0
    for bit in bits:
        num0 += bit == "0"
        num1 += bit == "1"
    # keep 1 if even as well
    most_common_bit = "1" if num1 < num0 else "0"

    # filter data
    co2_data = [line for line in co2_data if line[digit_position] == most_common_bit]

co2_rating = int(co2_data[0], 2)
print(co2_rating)

power = oxygen_rating * co2_rating

print(f"{power=}")
