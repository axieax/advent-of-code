from collections import Counter

with open("input.txt") as f:
    data = [x.strip() for x in f.readlines()]
    num_digits = len(data[0])

# calculate oxygen rating
oxygen_data = data.copy()
co2_data = data.copy()


def most_common_bit(data: list[str], digit_position: int) -> str:
    """
    Finds the most common bit for the given dataset at a given position

    :param data list[str]: dataset
    :param digit_position int: digit position to be compared
    :rtype str: most common bit found as a string, returning 1 as the default value
    """
    bits = [line[digit_position] for line in data]
    first, second = Counter(bits).most_common()
    equal = first[1] == second[1]
    return first[0] if not equal else "1"


for digit_position in range(num_digits):
    # oxygen or co2 dataset exhausted
    if 1 in (len(oxygen_data), len(co2_data)):
        break

    # filter oxygen data
    mcb_oxygen = most_common_bit(oxygen_data, digit_position)
    oxygen_data = [line for line in oxygen_data if line[digit_position] == mcb_oxygen]

    # filter co2 data (flip most common bit to get least common bit)
    mcb_co2 = most_common_bit(co2_data, digit_position)
    lcb_co2 = str((~int(mcb_co2)) & 1)
    co2_data = [line for line in co2_data if line[digit_position] == lcb_co2]

oxygen = int(oxygen_data[0], 2)
co2 = int(co2_data[0], 2)
power = oxygen * co2

print(f"{oxygen=}")
print(f"{co2=}")
print(f"{power=}")
