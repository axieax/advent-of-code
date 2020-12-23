# mod to wrap around list like a circle
# input
t_cups = [int(x) for x in list('135468729')]
t_cups = [int(x) for x in list('389125467')]
cups = [i + 1 for i in range(1000000)]
cups[0:9] = t_cups

current_value = cups[0]
for i in range(10 * 1000000):
    print(i)
    # print(f'Move {i+1}\n{cups} {current_value}')
    # popped
    pick_up = [cups.pop((cups.index(current_value) + 1) % len(cups)) for _ in range(3)]
    # print(pick_up)
    # destination
    lower_values = [x for x in cups if x < current_value]
    destination_value = max(cups) if len(lower_values) == 0 else max(lower_values)
    destination_index = cups.index(destination_value)
    # print(destination_value)
    # place cups
    for cup in pick_up[::-1]:
        cups.insert(destination_index + 1, cup)
    # move to new position
    current_value = cups[(cups.index(current_value) + 1) % len(cups)]

index_of_one = cups.index(1)
print(cups[(index_of_one + 1) % 1000000] * cups[(index_of_one + 2) % 1000000])
# print(''.join([str(x) for x in cups]))
