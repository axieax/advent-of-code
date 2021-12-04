import re

BOARD_SIZE = 5

# with open("input.txt") as f:
with open("sample.txt") as f:
    data = f.read()

boards = data.split("\n\n")
draws: list[str] = boards.pop(0).split(",")

# TODO: compile search regex

for draw in draws:
    pattern = draw if len(draw) > 1 else " " + draw
    checker = re.compile(pattern)
    # TODO: boards together
    for board in boards:
        checker.sub("-1", board)
        # check for bingo
        # horizontal bingo
        bingo = False
        if re.search(r"-1 -1 -1 -1 -1", board):
            bingo = True
        # vertical bingo
        if re.search(r"\n-1", "\n" + board):
            bingo = True
        # diagonal bingo 1
        gaps = [0, 3, 6, 9, 12]
        gap_pattern = "\n".join(f".{gap}-1.*?" for gap in gaps)
        if re.search(gap_pattern, board):
            bingo = True
