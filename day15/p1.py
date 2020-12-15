def van_eck_seq(nums, limit):
    last_turn = {}
    for i in range(limit):
        # starting sequence
        if i < len(nums):
            last_turn[nums[i]] = i + 1
        # general case
        else:
            last_num = nums[-1]
            num = i - last_turn.get(last_num, i)
            nums.append(num)
            last_turn[last_num] = i
    return nums[-1]

if __name__ == '__main__':
    print(van_eck_seq([8,11,0,19,1,2], 2020))
