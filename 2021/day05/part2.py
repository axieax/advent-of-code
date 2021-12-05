from collections import defaultdict

with open("input.txt") as f:
    # with open("sample.txt") as f:
    data = f.readlines()

points = defaultdict(int)

# parse input
# data = ["1,1 -> 3,3"]
# data = ["9,7 -> 7,9"]
for line in data:
    u, v = line.split("->")
    u1, u2 = [int(x) for x in u.split(",")]
    v1, v2 = [int(x) for x in v.split(",")]
    # horizontal lines
    if u1 == v1:
        start = min(u2, v2)
        end = max(u2, v2)
        for y in range(start, end + 1):
            points[(u1, y)] += 1

    # vertical lines
    elif u2 == v2:
        start = min(u1, v1)
        end = max(u1, v1)
        for x in range(start, end + 1):
            points[(x, u2)] += 1

    # diagonal lines
    else:
        # make u the leftmost point
        if u1 > v1:
            u1, u2, v1, v2 = v1, v2, u1, u2

        # positive gradient from u to v
        if v2 > u2:
            for x in range(u1, v1 + 1):
                passed = x - u1
                for y in range(u2, v2 + 1):
                    if y - u2 == passed:
                        points[(x, y)] += 1

        # negative gradient from u to v
        else:
            for x in range(u1, v1 + 1):
                passed = x - u1
                for y in range(u2, v2 - 1, -1):
                    if u2 - y == passed:
                        points[(x, y)] += 1

# count
count = len(list(filter(lambda x: x >= 2, points.values())))
print(count)
