# extract input from file
with open('input.txt', 'r') as f:
    lines = [x.rstrip() for x in f.readlines()]
# no lines visited initially
visited = {x: False for x in range(len(lines))}
accumulator = 0
pc = 0
while True:
    # pc already visited (loop detected)
    if visited[pc]:
        break
    # mark current pc as visited
    visited[pc] = True
    line = lines[pc].split(' ')
    # acc instruction
    if line[0] == 'acc':
        accumulator += int(line[1])
        pc += 1
    # jmp instruction
    elif line[0] == 'jmp':
        pc += int(line[1])
    # nop instruction
    else:
        pc += 1

print(accumulator)
