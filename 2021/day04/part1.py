import re

BOARD_SIZE = 5

# with open("sample.txt") as f:
with open("input.txt") as f:
    data = f.read()

boards = data.split("\n\n")
draws: list[str] = boards.pop(0).split(",")
boards = "\n\n".join(boards)

GAPS = (0, 3, 6, 9, 12)
BINGO_PATTERNS = [
    # vertical matches
    re.compile(("\n.{%s}-1.*?" % gap) * BOARD_SIZE)
    for gap in GAPS
] + [
    # horizontal matches
    re.compile(" ".join(("-1",) * BOARD_SIZE))
]
# diagonal matches
# re.compile("\n".join(f".{gap}-1.*?" for gap in GAPS)),
# re.compile("\n".join(f".*?-1.{gap}" for gap in GAPS)),
bingo_win = lambda b: any(bingo_checker.search(b) for bingo_checker in BINGO_PATTERNS)

for draw in draws:
    # indicate matches on boards
    # pad with space if necessary
    sub_pattern = draw if len(draw) > 1 else " " + draw
    # followed by a space or end of line
    sub_pattern += "(?= |\n)"
    boards = re.sub(sub_pattern, "-1", boards)

    # check for bingo
    if bingo_win("\n" + boards):
        print(f"BINGO! {draw}")
        # find winning board
        boards = boards.split("\n\n")
        winning_board = [b for b in boards if bingo_win("\n" + b)][0]
        print(winning_board)
        # calculate score
        unmarked_numbers = re.findall(r"[^(-1)]\d+", winning_board)
        score = int(draw) * sum(int(x) for x in unmarked_numbers)
        print(f"{score=}")
        break
