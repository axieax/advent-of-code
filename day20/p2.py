from functools import reduce
def borders(tile):
    # TOP (N), RIGHT (E), BOTTOM (S), LEFT (W)
    return [tile[0], ''.join([t[-1] for t in tile]), tile[-1], ''.join([t[0] for t in tile]), ]

def all_borders(border):
    # include flipped borders
    return border + [''.join(reversed(x)) for x in border]


# extract input from file
with open('input.txt', 'r') as f:
    lines = [x.rstrip() for x in f.readlines()] + ['']
tiles = {}
for index, line in enumerate(lines):
    if line.startswith('Tile'):
        tiles[int(line.split('Tile ')[1][:-1])] = lines[index + 1: index + 11]

# corner tiles have two borders that are not in common with any other tiles
puzzle = {
    2: [], # corner
    3: [], # edge
    4: [], # middle
}
# examine each tile
for tile_key, tile_value in tiles.items():
    tile_borders = all_borders(borders(tile_value))
    # compare with other tile borders
    common_borders = []
    for compare_key, compare_value in tiles.items():
        compare_borders = all_borders(borders(compare_value))
        # ignore same key
        if tile_key == compare_key:
            continue
        # common borders exist
        for i in range(len(tile_borders)):
            if tile_borders[i] in compare_borders:
                common_borders.append(i)
                break
        # ??
        # for i in range(len(tile_borders)):
        #     for j in range(len(compare_borders)):
        #         if tile_borders[i] == compare_borders[j]:
        #             common_borders.append([(tile_key, i), (compare_key, j)])
    # corner tiles have two common borders
    puzzle[len(common_borders)].append({
        'tile key': tile_key,
        'common borders': common_borders,
    })

# product of corner tiles
# print(reduce(lambda x, y: x * y, corners))

# print(puzzle)

print(puzzle[2])
print(puzzle[3])
