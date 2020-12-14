# extract input from file
with open('input.txt', 'r') as f:
	lines = [x.split(' ') for x in f.readlines()]
# count number of valid passwords
count = 0
for line in lines:
	# extract positions from 'a-b'
	positions = [int(x) for x in line[0].split('-')]
	# extract letter
	letter = line[1][0]
	# extract word
	word = line[2]
	# only one of the positions (one-indexed) contains the letter
	if (word[positions[0] - 1] == letter) ^ (word[positions[1] - 1] == letter):
		count += 1
print(count)
