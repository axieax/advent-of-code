with open("input.txt") as f:
    instructions = [x.split() for x in f.readlines()]

position = {
    "horizontal": 0,
    "vertical": 0,
}

for movement, units in instructions:
    units = int(units)
    if movement == "forward":
        position["horizontal"] += units
    elif movement == "down":
        position["vertical"] += units
    elif movement == "up":
        position["vertical"] -= units

print(position["horizontal"] * position["vertical"])
