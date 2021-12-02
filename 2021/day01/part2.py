SLIDING_WINDOW_SIZE = 3

with open("input.txt") as f:
    depths = [int(x) for x in f.readlines()]

# find each window
count = 0
prev_window_sum = sum(depths[:SLIDING_WINDOW_SIZE])
for window_start in range(1, len(depths) - SLIDING_WINDOW_SIZE + 1):
    window = depths[window_start : window_start + SLIDING_WINDOW_SIZE]
    window_sum = sum(window)
    count += window_sum > prev_window_sum
    prev_window_sum = window_sum
print(count)
