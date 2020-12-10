with open("input.txt", "r") as f:
	lines = [x.split(" ") for x in f.readlines()]
	count = 0
	for line in lines:
		positions = [int(x) for x in line[0].split("-")]
		letter = line[1][0]
		word = line[2]
		if (word[positions[0] - 1] == letter) ^ (word[positions[1] - 1] == letter):
			count += 1
	print(count)
		
