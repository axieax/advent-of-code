# circular linked list representation of cups
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# input
cups = [int(x) for x in list('135468729')] + list(range(10, 1000000 + 1))
num_cups = len(cups)
# create circular linked list for cups
cups_list = [Node(x) for x in cups]
for index, cup in enumerate(cups_list[:-1]):
    cup.next = cups_list[index + 1]
cups_list[-1].next = cups_list[0]
lookup = {cup.value: cup for cup in cups_list}

curr = cups_list[0]
for _ in range(10 * 1000000):
    # picked up cups are skipped
    a, b, c = curr.next, curr.next.next, curr.next.next.next
    curr.next = c.next
    # destination
    unavailable = [a.value, b.value, c.value, curr.value]
    destination_value = curr.value
    while destination_value in unavailable:
        destination_value -= 1
        if destination_value < 1:
            destination_value = num_cups
    dest = lookup[destination_value]
    # reconnect picked up cups, placing them after dest
    c.next = dest.next
    dest.next = a
    curr = curr.next

# calculate answer
print(lookup[1].next.value * lookup[1].next.next.value)
