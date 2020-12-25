import re
from functools import reduce
import numpy as np
from p1 import borders, all_borders

# border position (0 - North/Up, 1 - East/Right, 2 - South/Down, 3 - West/Left)
# rotation (0, 90, 180, 270)
# flipped (0 - no flip, 1 - about X axis, 2 - about Y axis)
# NOTE: flip of 1 + flip of 2 is the same as a 180 degree rotation

def tile_rotate(tile, degree):
    ''' Rotates a 2D array clockwise by the degree specified '''
    a = np.array([list(x) for x in tile])
    a = np.rot90(a, k=degree//90, axes=(1,0))
    return [''.join(x) for x in a.tolist()]

def tile_flip(tile, flip):
    ''' Flips a 2D array in the flip direction specified '''
    if flip == 0:
        return tile
    elif flip == 1:
        return [x[::-1] for x in tile]
    else:
        return tile[::-1]

def tile_combinations(tile):
    ''' Return all flipped and rotated combinations of a 2D array '''
    patterns = []
    for flip in [0, 1, 2]:
        for rotation in [0, 90, 180, 270]:
            patterns.append(tile_flip(tile_rotate(tile, rotation), flip))
    return patterns

def tile_neighbours(tile_key):
    ''' Returns the tiles that share a common border with the given tile '''
    tiles = []
    if tile_key in two_borders:
        common_borders = two_borders[tile_key]
        for border_tuple in common_borders:
            tiles.append(border_tuple[2])
    elif tile_key in three_borders:
        common_borders = three_borders[tile_key]
        for border_tuple in common_borders:
            tiles.append(border_tuple[2])
    elif tile_key in four_borders:
        common_borders = four_borders[tile_key]
        for border_tuple in common_borders:
            tiles.append(border_tuple[2])
    return tiles

def common_border_positions(tile, neighbours):
    ''' Returns a list of borders for a tile that are common with a neighbour '''
    positions = []
    tile_borders = borders(tile)
    for neighbour in neighbours:
        for position in [0, 1, 2, 3]:
            if tile_borders[position] in all_borders(tiles[neighbour]):
                positions.append(position)
    return positions

def find_tile(possible_tiles, tile_common_border_positions, border_requirements):
    '''
    Returns a tile from possible_tiles which has common borders for the specified tile_common_border_positions,
    and satisfies the border_requirements (list of tuples (border_direction, border_pattern)) where its
    border_direction border matches the specified border_pattern
    '''
    for tile in possible_tiles:
        neighbours = tile_neighbours(tile)
        combinations = tile_combinations(tiles[tile])
        # examine all possible arrangements for the tile
        for combination in combinations:
            # tile has to satisfy requirements - has 'border' in its specified border direction
            if not all([borders(combination)[direction] == border for direction, border in border_requirements]):
                continue
            # tile has common borders in its specified tile_common_border_positions
            if sorted(common_border_positions(combination, neighbours)) == tile_common_border_positions:
                return tile, combination
    return None, None

def check_sea_monster(image, i, j):
    ''' Checks if a sea monster can be seen from coordinates i, j '''
    try:
        for row, sm_line in enumerate(sea_monster):
            for col, sm_char in enumerate(sm_line):
                # where a sea monster has a '#', the relative position in the image should also have a '#'
                if sm_char == '#' and image[i + row][j + col] != '#':
                    return False
        return True
    except:
        return False


# extract input from file
with open('input.txt', 'r') as f:
    lines = [x.rstrip() for x in f.readlines()] + ['']
# tiles (key -> pattern)
tiles = {}
tile_length = 10
for index, line in enumerate(lines):
    if line.startswith('Tile'):
        tiles[int(line.split('Tile ')[1][:-1])] = lines[index + 1: index + 1 + tile_length]
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
num_tiles = len(tiles)
puzzle_length = int(num_tiles ** 0.5)
puzzle = [[-1 for _ in range(puzzle_length)] for _ in range(puzzle_length)] # tile key representation
puzzle_visual = [['' for _ in range(puzzle_length)] for _ in range(puzzle_length)] # tile pattern representation
# find leftmost tile
leftmost_tile = [tile_key for tile_key, common_borders in two_borders.items() if all([tup[1] in [1, 2] for tup in common_borders])][0]
puzzle[0][0] = leftmost_tile
puzzle_visual[0][0] = tiles[leftmost_tile]


# fill in puzzle
for i in range(puzzle_length):
    for j in range(puzzle_length):
        # ignore leftmost piece (already placed)
        if i == j == 0:
            continue
        # top row tile placement
        elif i == 0:
            # extract information about tile to the left
            left_tile_key = puzzle[i][j - 1]
            left_common_border = borders(puzzle_visual[i][j - 1])[1]
            left_tile_neighbours = tile_neighbours(left_tile_key)

            # top row tiles (excluding the upper left and upper right corner tiles) have open common borders on their right, down and left edges (1, 2, 3)
            # the upper left corner tile has already been placed so we ignore it, and the upper right corner tile has open borders on its down and left edges (2, 3)
            tile_common_border_positions = [2, 3] if j == puzzle_length - 1 else [1, 2, 3]
            # try to find the tile which shares a common border with the tile to the left (has left_common_border as its west border)
            border_requirements = [(3, left_common_border)]
            
            # find tile with these requirements
            tile_key, tile_pattern = find_tile(left_tile_neighbours, tile_common_border_positions, border_requirements)
            puzzle[i][j] = tile_key
            puzzle_visual[i][j] = tile_pattern

        # left column
        elif j == 0:
            # extract information about tile above
            up_tile_key = puzzle[i - 1][j]
            up_common_border = borders(puzzle_visual[i - 1][j])[2]
            up_neighbours = tile_neighbours(up_tile_key)

            # left column tiles (excluding the upper left and bottom left corner tiles) have open common borders on their up, right, down edges (0, 1, 2)
            # the upper left corner tile has already been placed so we ignore it, and the bottom left corner tile has open borders on its up and right edges (0, 1)
            tile_common_border_positions = [0, 1] if i == puzzle_length - 1 else [0, 1, 2]
            # try to find the tile which shares a common border with the tile above (has up_common_border as its top border)
            border_requirements = [(0, up_common_border)]
            
            # find tile with these requirements
            tile_key, tile_pattern = find_tile(up_neighbours, tile_common_border_positions, border_requirements)
            puzzle[i][j] = tile_key
            puzzle_visual[i][j] = tile_pattern

        # general placement - check left and above
        else:
            # extract information about tile to the left
            left_tile_key = puzzle[i][j - 1]
            left_common_border = borders(puzzle_visual[i][j - 1])[1]
            left_neighbours = tile_neighbours(left_tile_key)
            # extract information about tile above
            up_tile_key = puzzle[i - 1][j]
            up_common_border = borders(puzzle_visual[i - 1][j])[2]
            up_neighbours = tile_neighbours(up_tile_key)
            # possible options for this tile are neighbours of both the tile to the left and the tile above
            tile_options = list(set(left_neighbours) & set(up_neighbours))
            
            # bottom row
            if i == puzzle_length - 1:
                # excluding the bottom left and bottom right corners, bottom row tiles have open common borders on their
                # left, up and right edges (0, 1, 3), the bottom left corner has already been addressed under left column
                # so we ignore it, and the bottom right corner has open borders on its left and up edges (0, 3)
                tile_common_border_positions = [0, 3] if j == puzzle_length - 1 else [0, 1, 3]
            # general rows
            else:
                # in general, excluding tiles in the rightmost column, these tiles have all their borders open (0, 1, 2, 3)
                tile_common_border_positions = [0, 2, 3] if j == puzzle_length - 1 else [0, 1, 2, 3]
            # try to find the tile which shares a common border with the tile to the left (has left_common_border as its west border)
            # and shares a common border with the tile above (has up_common_border as its top border)
            border_requirements = [(0, up_common_border), (3, left_common_border)]

            # find tile with these requirements
            tile_key, tile_pattern = find_tile(tile_options, tile_common_border_positions, border_requirements)
            puzzle[i][j] = tile_key
            puzzle_visual[i][j] = tile_pattern


# remove borders from completed puzzle
for i, row in enumerate(puzzle_visual): # puzzle_length
    for j, tile in enumerate(row): # puzzle_length
        puzzle_visual[i][j] = [r[1:-1] for r in tile[1:-1]]
tile_length -= 2

# create artwork (2D list of characters) from the puzzle (3D list of characters)
artwork = [[] for _ in range(puzzle_length * tile_length)]
for i, row in enumerate(puzzle_visual): # puzzle_length
    for j, tile in enumerate(row): # puzzle_length
        for k, line in enumerate(tile): # tile_length
            artwork[i * tile_length + k] += list(line)

# check for sea monsters
sea_monster = [
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   ',
]
sea_monster = [list(row) for row in sea_monster]

# find sea monsters for each rotation/flip combination of artwork
for comb in tile_combinations(artwork):
    num_hashes = 0
    num_sea_monsters = 0
    for i, row in enumerate(comb):
        for j, char in enumerate(row):
            if char == '#':
                num_hashes += 1
            num_sea_monsters += check_sea_monster(comb, i, j)
    if num_sea_monsters > 0:
        # roughness: number of hashes that are not part of a sea monster (which has 15 hashes)
        print(num_hashes - 15 * num_sea_monsters)
        break
