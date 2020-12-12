def direction_degree(degree):
    # returns tuple (north, east)
    if degree == 0:
        return (1, 0)
    elif degree == 90:
        return (0, 1)
    elif degree == 180:
        return (-1, 0)
    elif degree == 270:
        return (0, -1)


with open('input.txt', 'r') as f:
    instructions = [x.rstrip() for x in f.readlines()]

east = 0
north = 0
# (north, east)
direction = 90

for instruction in instructions:
    action = instruction[0]
    degree = int(instruction[1:])

    if action == 'N':
        north += degree
    elif action == 'S':
        north -= degree
    elif action == 'E':
        east += degree
    elif action == 'W':
        east -= degree
    elif action == 'L':
        direction = (direction - degree) % 360
    elif action == 'R':
        direction = (direction + degree) % 360
    elif action == 'F':
        n, e = direction_degree(direction)
        north += n * degree
        east += e * degree

print(abs(north) + abs(east))
