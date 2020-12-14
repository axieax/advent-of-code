from p1 import find_invalid_number

# extract input from file
with open('input.txt', 'r') as f:
    array = [int(x) for x in f.readlines()]
invalid_num = find_invalid_number(array)
    
# i is the index of the first number
i = 0
while i < len(array) - 2:
    # add first number and the following number to the continguous range (minimum 2 numbers)
    contiguous_range = [array[i], array[i + 1]]
    # the index j starts after these two numbers
    j = i + 2
    while j < len(array):
        # contiguous sum matches the invalid num (found)
        contiguous_sum = sum(contiguous_range)
        if contiguous_sum == invalid_num:
            print(min(contiguous_range) + max(contiguous_range))
            exit()
        # contiguous sum exceeds the invalid num
        elif contiguous_sum > invalid_num:
            break
        # keep trying to add more numbers
        contiguous_range.append(array[j])
        j += 1
    i += 1
