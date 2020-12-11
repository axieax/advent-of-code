def two_sum(prev_nums, target):
    visited = []
    for num in prev_nums:
        visited.append(num)
        if target - num in visited:
            return True
    return False
    

with open('input.txt', 'r') as f:
    arr = [int(x) for x in f.readlines()]
    for i in range(25, len(arr)):
        prev_nums = arr[i - 25: i]
        # Check two numbers in this list sum to this number
        if not two_sum(prev_nums, arr[i]):
            print(arr[i])
            break
