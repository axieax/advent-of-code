with open("input.txt", "r") as f:
	nums = [int(n) for n in f.readlines()]
	for i in range(len(nums)):
		for j in range(len(nums)):
				if nums[i] + nums[j] == 2020:
					print(nums[i]*nums[j])

