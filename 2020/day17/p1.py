def coord_neighbours(active_coords, coord):
    ''' returns the neighbour coords for specified coord '''
    # find neighbours
    neighbours = []
    for x_diff in range(-1, 2, 1):
        for y_diff in range(-1, 2, 1):
            for z_diff in range(-1, 2, 1):
                x, y, z = coord
                new_coord = (x + x_diff, y + y_diff, z + z_diff)
                if x_diff == y_diff == z_diff == 0:
                    # same coord / not neighbour
                    continue
                neighbours.append(new_coord)
    return neighbours

if __name__ == '__main__':
    # extract input from file
    with open('input.txt', 'r') as f:
        lines = [list(x.rstrip()) for x in f.readlines()]

    # extract initially active coordinates
    active_coords = []
    for i, line in enumerate(lines):
        for j, x in enumerate(line):
            if x == '#':
                active_coords.append((i, j, 0))

    # six cycles
    for _ in range(6):
        new_active_coords = []
        nearby_coords = []
        # rule 1
        for cube in active_coords:
            neighbours = coord_neighbours(active_coords, cube)
            if len([x for x in neighbours if x in active_coords]) in [2, 3]:
                new_active_coords.append(cube)
            nearby_coords += neighbours
        # rule 2
        inactive_nearby_coords = list(set(nearby_coords) - set(active_coords))
        new_active_coords += [x for x in inactive_nearby_coords if len([x for x in coord_neighbours(active_coords, x) if x in active_coords]) == 3]
        active_coords = new_active_coords

    print(len(active_coords))
