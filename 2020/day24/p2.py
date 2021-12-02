import re
from p1 import coordinate_move, flip_tile

def tile_neighbours(coordinate):
    return set([coordinate_move(coordinate, direction) for direction in directions.values()])


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
    curr = (0, 0)
    for move in line:
        curr = coordinate_move(curr, directions[move])
    flip_tile(black_tiles, curr)

# 100 days
for _ in range(100):
    new_black_tiles = black_tiles.copy()
    nearby_white_tiles = set()
    for black_tile in black_tiles:
        neighbours = tile_neighbours(black_tile)
        # rule 1
        black_neighbours = neighbours & black_tiles
        if len(black_neighbours) == 0 or len(black_neighbours) > 2:
            flip_tile(new_black_tiles, black_tile)
        nearby_white_tiles |= (neighbours - black_tiles)
    # rule 2
    for white_tile in nearby_white_tiles:
        black_neighbours = tile_neighbours(white_tile) & black_tiles
        if len(black_neighbours) == 2:
            flip_tile(new_black_tiles, white_tile)
    black_tiles = new_black_tiles

print(len(black_tiles))
