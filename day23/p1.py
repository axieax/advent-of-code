# input
cups = [int(x) for x in list('135468729')]

current_value = cups[0]
for _ in range(100):
    # picked up cups
    pick_up = [cups.pop((cups.index(current_value) + 1) % len(cups)) for _ in range(3)]
    # destination
    lower_values = [x for x in cups if x < current_value]
    destination_value = max(cups) if len(lower_values) == 0 else max(lower_values)
    destination_index = cups.index(destination_value)
    # place cups in same order
    for cup in pick_up[::-1]:
        cups.insert(destination_index + 1, cup)
    # move to new position
    current_value = cups[(cups.index(current_value) + 1) % len(cups)]

# print cups after 1
index_of_one = cups.index(1)
print(''.join([str(x) for x in cups[index_of_one + 1:] + cups[:index_of_one]]))
