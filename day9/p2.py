def two_sum(prev_nums, target):
    visited = []
    for num in prev_nums:
        visited.append(num)
        if target - num in visited:
            return True
    return False
    

with open('input.txt', 'r') as f:
    arr = [int(x) for x in f.readlines()]
    invalid_num = -1
    for i in range(25, len(arr)):
        prev_nums = arr[i - 25: i]
        # Check two numbers in this list sum to this number
        if not two_sum(prev_nums, arr[i]):
            invalid_num = arr[i]
            break
    
    found = False
    i = 0
    while not found and i < len(arr) - 2:
        contiguous_range = [arr[i], arr[i + 1]]
        
        j = i + 2
        while j < len(arr):
            # found
            if sum(contiguous_range) == invalid_num:
                print(min(contiguous_range) + max(contiguous_range))
                found = True
                break
            # exceeds
            elif sum(contiguous_range) > invalid_num:
                break
            contiguous_range.append(arr[j])
            j += 1
        i += 1
