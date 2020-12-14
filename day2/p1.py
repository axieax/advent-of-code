# extract input from file
with open('input.txt', 'r') as f:
	lines = [x.split(' ') for x in f.readlines()]
# count number of valid passwords
count = 0
for line in lines:
	# extract min and max values from 'min-max'
	min_max = [int(x) for x in line[0].split('-')]
	# extract letter
	letter = line[1][0]
	# extract word
	word = line[2]
	# number of occurrences of letter in word is in the inclusive range [min, max]
	if min_max[0] <= word.count(letter) <= min_max[1]:
		count += 1
print(count)
