import math
with open("input.txt", "r") as f:
    lines = [x.rstrip() for x in f.readlines()]
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
    missing_id = (set(range(99, 975)) - set(seats))
    print(missing_id)
