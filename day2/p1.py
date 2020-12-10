with open("input.txt", "r") as f:
	lines = [x.split(" ") for x in f.readlines()]
	count = 0
	for line in lines:
		min_max = line[0].split("-")
		letter = line[1][0]
		word = line[2]
		if int(min_max[0]) <= word.count(letter) <= int(min_max[1]):
			count += 1
	print(count)
		
