with open("input.txt") as f:
    instructions = [x.split() for x in f.readlines()]

position = {
    "horizontal": 0,
    "vertical": 0,
    "aim": 0,
}

for movement, units in instructions:
    units = int(units)
    if movement == "forward":
        position["horizontal"] += int(units)
        position["vertical"] += position["aim"] * int(units)
    elif movement == "down":
        position["aim"] += int(units)
    elif movement == "up":
        position["aim"] -= int(units)

print(position["horizontal"] * position["vertical"])
