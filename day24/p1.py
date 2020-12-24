import re
class Tile:
    def __init__(self):
        self.black = False
        self.neighbours = {}
    def flip(self):
        self.black = not self.black


def opposite_direction(d):
    directions = ['n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw']
    return directions[(directions.index(d) + 4) % 8]


# extract input from file
with open('input.txt', 'r') as f:
    lines = [x.rstrip() for x in f.readlines()]

# split directions
for n, line in enumerate(lines):
    tokenised = []
    for i, char in enumerate(line):
        if char == 'e' or char == 'w':
            tokenised.append(char)
        elif char == 's' or char == 'n':
            tokenised.append(char + line[i + 1])
    lines[n] = tokenised

print(lines)

all_tiles = [Tile(), ]
for line in lines:
    # reference tile
    curr = all_tiles[0]
    curr.flip()
    for move in line:
        if move in curr.neighbours:
            new = curr.neighbours[move]
        else:
            new = Tile()
            new.neighbours[opposite_direction(move)] = curr
            curr.neighbours[move] = new
            all_tiles.append(new)
        curr.flip()
        curr = new

print(all_tiles)
print(len([x for x in all_tiles if x.black]))

# issue: E then W should point to the same tile, but program doesn't know - doubly linked
