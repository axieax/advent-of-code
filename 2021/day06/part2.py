# with open("sample.txt") as f:
with open("input.txt") as f:
    fish = [int(x) for x in f.read().split(",")]

lives = {i: fish.count(i) for i in range(-1, 9)}

for _ in range(256):
    # simulate growth
    new = lives[0]
    old = lives[-1]
    # tick down
    lives = {k: lives[k + 1] for k in range(-1, 8)}
    # add to old
    lives[-1] += old
    lives[6] += new
    lives[8] = new

# NOTE: doesn't include old (would have died) for some reason (same as part 1)
print(sum(lives.values()) - lives[-1])
