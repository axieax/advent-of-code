import math
from p1 import highest_seat_id

with open('input.txt', 'r') as f:
    lines = [x.rstrip() for x in f.readlines()]
# binary search
seats = []
for line in lines:
    # row FB
    fb_lo = 0
    fb_hi = 127
    for char in line[:7]:
        mid = (fb_lo + fb_hi) / 2
        if char == 'F':
            fb_hi = math.floor(mid)
        elif char == 'B':
            fb_lo = math.ceil(mid)
    row = min((fb_lo, fb_hi))
    # col LR
    lr_lo = 0
    lr_hi = 7
    for char in line[7:]:
        mid = (lr_lo + lr_hi) / 2
        if char == 'L':
            lr_hi = math.floor(mid)
        elif char == 'R':
            lr_lo = math.ceil(mid)
    col = max((lr_lo, lr_hi))
    # seat
    seat = row * 8 + col
    seats.append(seat)
# id missing from the range of numbers from the lowest_seat_id to the highest_seat_id
missing_id = (set(range(min(seats), highest_seat_id())) - set(seats))
print(list(missing_id)[0])
