def relative_rotation(north_diff, east_diff, rotation):
    ''' returns the relative difference in north and east after rotation '''
    if rotation == 0:
        return (north_diff, east_diff)
    elif rotation == 90:
        return (-east_diff, north_diff)
    elif rotation == 180:
        return (-north_diff, -east_diff)
    elif rotation == 270:
        return (east_diff, -north_diff)


if __name__ == '__main__':
    # extract input from file
    with open('input.txt', 'r') as f:
        instructions = [x.rstrip() for x in f.readlines()]

    # ship coordinates
    ship = {
        'north': 0,
        'east': 0,
    }
    # waypoint is relative to ship
    waypoint = {
        'north': 1,
        'east': 10,
    }

    for instruction in instructions:
        # extract components
        action = instruction[0]
        degree = int(instruction[1:])

        if action == 'N':
            waypoint['north'] += degree
        elif action == 'S':
            waypoint['north'] -= degree
        elif action == 'E':
            waypoint['east'] += degree
        elif action == 'W':
            waypoint['east'] -= degree
        elif action == 'L':
            rel_n, rel_e = relative_rotation(waypoint['north'], waypoint['east'], (-degree) % 360)
            waypoint['north'] = rel_n
            waypoint['east'] = rel_e
        elif action == 'R':
            rel_n, rel_e = relative_rotation(waypoint['north'], waypoint['east'], degree % 360)
            waypoint['north'] = rel_n
            waypoint['east'] = rel_e
        elif action == 'F':
            ship['north'] += waypoint['north'] * degree
            ship['east'] += waypoint['east'] * degree

    # Manhattan distance
    print(abs(ship['north']) + abs(ship['east']))
