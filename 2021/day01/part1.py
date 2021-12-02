with open("input.txt") as f:
    depths = [int(x) for x in f.readlines()]

count = 0
prev = depths[0]
for x in depths[1:]:
    count += x > prev
    prev = x
print(count)
