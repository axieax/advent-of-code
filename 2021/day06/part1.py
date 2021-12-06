with open("input.txt") as f:
    fish = [int(x) for x in f.read().split(",")]

for _ in range(80):
    # simulate growth
    new = fish.count(0)
    fish = [f - 1 for f in fish if f > 0]
    fish += [6, 8] * new

print(len(fish))
