from functools import reduce
def borders(tile):
    # TOP, BOTTOM, LEFT, RIGHT
    return [tile[0], tile[-1], ''.join([t[0] for t in tile]), ''.join([t[-1] for t in tile])]

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
corners = []
# examine each tile
for tile_key, tile_value in tiles.items():
    tile_borders = all_borders(borders(tile_value))
    # compare with other tile borders
    common_borders = 0
    for compare_key, compare_value in tiles.items():
        compare_borders = all_borders(borders(compare_value))
        # ignore same key
        if tile_key == compare_key:
            continue
        # common borders exist
        if len(set(tile_borders).intersection(set(this_borders))) > 0:
            common += 1
    # corner tiles have two common borders
    if common == 2:
        corners.append(tile_key)

# product of corner tiles
print(reduce(lambda x, y: x * y, corners))
