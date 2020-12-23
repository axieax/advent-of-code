import re
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

def tile_combinations(tile):
    patterns = []
    for flip in [0, 1, 2]:
        for rotation in [0, 90, 180, 270]:
            patterns.append(tile_flip(tile_rotate(tile, rotation), flip))
    return patterns

def tile_neighbours(tile):
    tiles = []
    if tile in two_borders:
        common_borders = two_borders[tile]
        for border_tuple in common_borders:
            tiles.append(border_tuple[2])
    elif tile in three_borders:
        common_borders = three_borders[tile]
        for border_tuple in common_borders:
            tiles.append(border_tuple[2])
    elif tile in four_borders:
        common_borders = four_borders[tile]
        for border_tuple in common_borders:
            tiles.append(border_tuple[2])
    return tiles

def common_border_positions(tile, neighbours):
    positions = []
    tile_borders = borders(tile)
    for neighbour in neighbours:
        for position in [0, 1, 2, 3]:
            if tile_borders[position] in all_borders(tiles[neighbour]):
                positions.append(position)
    return positions


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
            left_tile_key = puzzle[i][j - 1]
            left_common_border = borders(puzzle_visual[i][j - 1])[1]
            left_neighbours = tile_neighbours(left_tile_key)
            # try to find the tile which shares a common border with left_common_border
            placed = False
            for possible in left_neighbours:
                if placed:
                    break
                possible_neighbours = tile_neighbours(possible)
                combinations = tile_combinations(tiles[possible])
                for combination in combinations:
                    # left border of possible is the left_common_border, and other common borders aren't facing an edge (being unused)
                    open_positions = [2, 3] if j == 11 else [1, 2, 3]
                    if borders(combination)[3] == left_common_border and sorted(common_border_positions(combination, possible_neighbours)) == open_positions:
                        # place
                        puzzle[i][j] = possible
                        puzzle_visual[i][j] = combination
                        placed = True
                        break
        # left column
        elif j == 0:
            up_tile_key = puzzle[i - 1][j]
            up_common_border = borders(puzzle_visual[i - 1][j])[2]
            up_neighbours = tile_neighbours(up_tile_key)
            # try to find the tile which shares a common border with up_commmon_border
            placed = False
            for possible in up_neighbours:
                if placed:
                    break
                possible_neighbours = tile_neighbours(possible)
                combinations = tile_combinations(tiles[possible])
                for combination in combinations:
                    # up border of possible is up_common_border, and the other common borders aren't facing an edge (being unused)
                    open_positions = [0, 1] if i == 11 else [0, 1, 2]
                    if borders(combination)[0] == up_common_border and sorted(common_border_positions(combination, possible_neighbours)) == open_positions:
                        # place
                        puzzle[i][j] = possible
                        puzzle_visual[i][j] = combination
                        placed = True
                        break
        # general placement - check left and above
        else:
            left_tile_key = puzzle[i][j - 1]
            left_common_border = borders(puzzle_visual[i][j - 1])[1]
            left_neighbours = tile_neighbours(left_tile_key)
            up_tile_key = puzzle[i - 1][j]
            up_common_border = borders(puzzle_visual[i - 1][j])[2]
            up_neighbours = tile_neighbours(up_tile_key)
            options = list(set(left_neighbours) & set(up_neighbours))
            placed = False
            for possible in options:
                if placed:
                    break
                possible_neighbours = tile_neighbours(possible)
                combinations = tile_combinations(tiles[possible])
                for combination in combinations:
                    # up border of possible is up_common_border, and the other common borders aren't facing an edge (being unused)
                    if i == 11:
                        open_positions = [0, 3] if j == 11 else [0, 1, 3]
                    else:
                        open_positions = [0, 2, 3] if j == 11 else [0, 1, 2, 3]
                    if borders(combination)[0] == up_common_border and borders(combination)[3] == left_common_border and sorted(common_border_positions(combination, possible_neighbours)) == open_positions:
                        # place
                        puzzle[i][j] = possible
                        puzzle_visual[i][j] = combination
                        placed = True
                        break

# convert puzzle_visual into an artwork
artwork = ['' for _ in range(144)]
for i, row in enumerate(puzzle_visual):
    for j, tile in enumerate(row):
        for k, line in enumerate(tile):
            artwork[i * 12 + j] += line
artwork = [list(x) for x in artwork]
print(artwork)

sea_monster = '''
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
'''
sea_monster_pattern = [
    '..................#.',
    '#....##....##....###',
    '.#..#..#..#..#..#...',
]


def check_sea_monster(image, row, column):
    # 20 wide
    try:
        window = [x[column: column + 20] for x in image[row: row + 3]]
        if window == sea_monster_pattern:
            return True
        return False
    except:
        return False

print(puzzle_visual[0][0]) # BUG: some are 10 instead of 12

# find sea monsters
for comb in tile_combinations(artwork):
    # print('\n'.join([''.join(x) for x in comb]))
    num_sea_monsters = 0
    for i, row in enumerate(comb):
        for j, char in enumerate(line):
            if char == '#':
                num_sea_monsters += check_sea_monster(comb, i, j)
    # print(num_sea_monsters)
