with open('input.txt', 'r') as f:
    adapters = sorted([int(x) for x in f.readlines()])
    diff_one = 0
    diff_three = 0
    for i in range(len(adapters)):
        curr = adapters[i]
        prev = adapters[i - 1] if i > 0 else 0
        diff = curr - prev
        if diff == 1:
            diff_one += 1
        elif diff == 3:
            diff_three += 1
    print(diff_one * (diff_three + 1))
