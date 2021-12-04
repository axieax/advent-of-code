import re

BOARD_SIZE = 5

# with open("input.txt") as f:
with open("sample.txt") as f:
    data = [x.strip() for x in f.readlines()]

# draws = [int(x) for x in data[0].split(",")]
# data = data[2:]
#
# boards = [
#     data[start : start + BOARD_SIZE] for start in range(0, len(data), BOARD_SIZE + 1)
# ]
# boards = list(
#     map(lambda board: [[int(x) for x in line.split()] for line in board], boards)
# )
#
# for draw in draws:
#     for board in boards:
#         pass
#
#
# print(boards)

# regex solution
