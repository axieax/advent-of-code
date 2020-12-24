# extract input from file
with open('input.txt', 'r') as f:
	nums = [int(n) for n in f.readlines()]
# first number
for i in nums:
	# second number
	for j in nums:
			# two numbers sum to 2020
			if i + j == 2020:
				# print their product
				print(i * j)
				exit()
