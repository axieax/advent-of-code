import re

def coordinate_move(original, offset):
    ''' returns a new coordinate tuple representing original + offset '''
    return original[0] + offset[0], original[1] + offset[1]

def flip_tile(black_tiles_set, tile):
    ''' flips a tile from a specified set of tiles '''
    if tile in black_tiles_set:
        black_tiles_set.remove(tile)
    else:
        black_tiles_set.add(tile)


if __name__ == '__main__':
    # extract input from file
    with open('input.txt', 'r') as f:
        lines = [re.findall(r'(e|se|sw|w|nw|ne)', line) for line in f.readlines()]

    '''
    Hexagonal grid coordinate system:
    [  ] [nw] [  ] [ne] [  ]
    [  ] [  ] [  ] [  ] [  ]
    [w ] [  ] [x ] [  ] [e ]
    [  ] [  ] [  ] [  ] [  ]
    [  ] [sw] [  ] [se] [  ]
    '''
    directions = {
        # x, y
        'e': (2, 0),
        'se': (1, -2),
        'sw': (-1, -2),
        'w': (-2, 0),
        'nw': (-1, 2),
        'ne': (1, 2),
    }

    # only save black tiles
    black_tiles = set()
    for line in lines:
        tile = (0, 0)
        for move in line:
            tile = coordinate_move(tile, directions[move])
        flip_tile(black_tiles, tile)

    print(len(black_tiles))
