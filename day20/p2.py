from functools import reduce
import numpy as np
from p1 import borders, all_borders

# border position (0 - North/Up, 1 - East/Right, 2 - South/Down, 3 - West/Left)
# rotation (0, 90, 180, 270)
# flipped (0 - no flip, 1 - about X axis, 2 - about Y axis)

def tile_rotate(tile, degree):
    a = np.array([list(x) for x in tile])
    a = np.rot90(a, k=degree//90, axes=(1,0))
    return [''.join(x) for x in a.tolist()]

def tile_flip(tile, flip):
    # flip of 1 and flip of 2 => rotate 180
    if flip == 0:
        return tile
    elif flip == 1:
        return [x[::-1] for x in tile]
    else:
        return tile[::-1]


# extract input from file
with open('input.txt', 'r') as f:
    lines = [x.rstrip() for x in f.readlines()] + ['']
# map: key -> pattern
tiles = {}
for index, line in enumerate(lines):
    if line.startswith('Tile'):
        tiles[int(line.split('Tile ')[1][:-1])] = lines[index + 1: index + 11]
# find pieces with x borders
two_borders = {}
three_borders = {}
four_borders = {}

# examine each tile
for tile_key, tile_pattern in tiles.items():
    tile_borders = borders(tile_pattern)
    # compare with other tile borders
    common_borders = []
    for compare_key, compare_pattern in tiles.items():
        # ignore same key
        if tile_key == compare_key:
            continue
        compare_borders = all_borders(compare_pattern)
        # check for common borders
        for t_border_position, t_border_pattern in enumerate(tile_borders):
            for c_border_position, c_border_pattern in enumerate(compare_borders):
                if t_border_pattern == c_border_pattern:
                    common_borders.append((tile_key, t_border_position, compare_key, c_border_position))
    if len(common_borders) == 2:
        two_borders[tile_key] = common_borders
    elif len(common_borders) == 3:
        three_borders[tile_key] = common_borders
    elif len(common_borders) == 4:
        four_borders[tile_key] = common_borders

# start filling in puzzle
puzzle = [[-1 for _ in range(12)] for _ in range(12)] # tile key representation
puzzle_visual = [['' for _ in range(12)] for _ in range(12)] # tile pattern representation
# find leftmost tile
leftmost_tile = [tile_key for tile_key, common_borders in two_borders.items() if all([tup[1] in [1, 2] for tup in common_borders])][0]
puzzle[0][0] = leftmost_tile
puzzle_visual[0][0] = tiles[leftmost_tile]

# fill in puzzle
for i in range(12):
    for j in range(12):
        # ignore leftmost piece (already placed)
        if i == j == 0:
            continue
        # top row
        elif i == 0:
            left_tile_key = puzzle[0][j]
        # left column
        elif j == 0:
            pass
        # right column
        elif j == 11:
            pass
        # bottom row
        elif i == 11:
            pass
        # general placement
        else:
            pass

# issue: already placed left piece might need to be flipped


'''
Old code:
from functools import reduce
import numpy as np
from p1 import borders, all_borders

def print_tile(tile):
    for t in tile:
        print(t)


# extract input from file
with open('input.txt', 'r') as f:
    lines = [x.rstrip() for x in f.readlines()] + ['']
tiles = {}
for index, line in enumerate(lines):
    if line.startswith('Tile'):
        tiles[int(line.split('Tile ')[1][:-1])] = lines[index + 1: index + 11]

# corner tiles have two borders that are not in common with any other tiles
# dictionary of dictionary of tile1, corner1, tile2, corner2
pieces = {
    2: {}, # corner
    3: {}, # edge
    4: {}, # middle
}
# examine each tile
for tile_key, tile_value in tiles.items():
    tile_borders = borders(tile_value)
    # compare with other tile borders
    common_borders = []
    for compare_key, compare_value in tiles.items():
        compare_borders = all_borders(compare_value)
        # ignore same key
        if tile_key == compare_key:
            continue
        # common borders exist
        for i in range(len(tile_borders)):
            for j in range(len(compare_borders)):
                if tile_borders[i] == compare_borders[j]:
                    # tile1, corner1, tile2, corner2
                    common_borders.append((tile_key, i, compare_key, j))
    # corner tiles have two common borders
    pieces[len(common_borders)][tile_key] = common_borders

print(pieces[2])

# TWO FLIPS
def flip(tile, flip):
    return list(reversed(tile)) if flip else tile

def rotate(tile, degree):
    a = np.array([list(x) for x in tile])
    a = np.rot90(a, k=degree//90, axes=(1,0))
    return [''.join(x) for x in a.tolist()]


# 2D list of (tile, rotation, flipped)
puzzle = [[-1 for _ in range(12)] for _ in range(12)]

# choose leftmost piece as the one with east and south common borders
leftmost_piece = [tile_key for tile_key, common_borders in pieces[2].items() if all([tup[1] in [1, 2] for tup in common_borders])][0]
print(leftmost_piece)
puzzle[0][0] = (leftmost_piece, 0, False)

def tile_pattern(tile, rotation, flipped):
    return '\n'.join(flip(rotate(tile, rotation), flipped))

def border_position(relative_border, rotation, flipped):
    return (relative_border + (rotation // 90)) % 4 + 4 * flipped

for i in range(12):
    for j in range(12):
        # ignore leftmost piece (already placed)
        if i == j == 0:
            continue
        # top row
        if i == 0:
            # look for piece to the left (with common border being its right)
            print(puzzle[i][j - 1])
            left_tile, left_rotation, left_flipped = puzzle[i][j - 1]
            left_pattern = tile_pattern(tiles[left_tile], left_rotation, left_flipped)
            common_border = borders(left_pattern)[1]
            print(pieces[2][left_tile])
            lefts_border_position = border_position()
            lefts_common_border = border_position
            # look for a three piece
            for piece in pieces[3]:
                pass
            
            # [tile['common borders'] for tile in pieces[2] if tile['tile key'] == left_tile][0]
        # left
        elif j == 0:
            pass
        # right
        elif j == 11:
            pass
        # bottom row
        elif i == 11:
            pass
        # normal
        else:
            pass

'''
