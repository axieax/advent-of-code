"""rank 678"""
from collections import defaultdict

with open("input.txt") as f:
    data = f.readlines()

points = defaultdict(int)

# parse input
for line in data:
    u, v = line.split("->")
    u1, u2 = [int(x) for x in u.split(",")]
    v1, v2 = [int(x) for x in v.split(",")]

    # horizontal lines
    if u1 == v1:
        start = min(u2, v2)
        end = max(u2, v2)
        for i in range(start, end + 1):
            points[(u1, i)] += 1

    # vertical lines
    if u2 == v2:
        start = min(u1, v1)
        end = max(u1, v1)
        for i in range(start, end + 1):
            points[(i, u2)] += 1

# count
count = len(list(filter(lambda x: x >= 2, points.values())))
print(count)
