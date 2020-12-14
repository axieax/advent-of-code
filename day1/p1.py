# extract numbers from input file
with open('input.txt', 'r') as f:
	nums = [int(n) for n in f.readlines()]
# first number
for i in range(len(nums)):
	# second number
	for j in range(len(nums)):
			# two numbers sum to 2020
			if nums[i] + nums[j] == 2020:
				print(nums[i]*nums[j])
				exit()
