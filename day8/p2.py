def try_run(lines):
    ''' tries to run program in lines, returning True if successful '''
    # no lines visited initially
    visited = {x: False for x in range(len(lines))}
    accumulator = 0
    pc = 0
    while True:
        # end reached
        if pc == num_lines:
            print(accumulator)
            return True
        # pc already visited (loop detected)
        elif visited[pc]:
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
    return False

# extract input from file
with open('input.txt', 'r') as f:
    lines = [x.rstrip() for x in f.readlines()]

''' Determine repeated pc's '''
# no lines visited initially
visited = {x: False for x in range(len(lines))}
repeated = []

pc = 0
while True:
    # pc already visited (loop detected)
    if visited[pc]:
        # break out of the loop when all repeated pc's have been appended to repeated once
        if pc in repeated:
            break
        # add all already visited pc's to repeated
        repeated.append(pc)
    # mark current pc as visited
    visited[pc] = True
    line = lines[pc].split(' ')
    # acc instruction
    if line[0] == 'acc':
        pc += 1
    # jmp instruction
    elif line[0] == 'jmp':
        pc += int(line[1])
    # nop instruction
    else:
        pc += 1

''' try changing each pc instruction one at a time '''
for pc in repeated:
    line = lines[pc].split(' ')
    if line[0] == 'jmp':
        # try changing jmp instruction to nop
        new_line = 'nop ' + line[1]
        # update instruction
        lines[pc] = new_line
        # run the program
        if try_run(lines):
            # exit if successful
            break
        # change back
        lines[pc] = ' '.join(line)
    elif line[0] == 'nop':
        # try changing nop instruction to jmp
        new_line = 'jmp ' + line[1]
        # update instruction
        lines[pc] = new_line
        # run the program
        if try_run(lines):
            # exit if successful
            break
        # change back
        lines[pc] = ' '.join(line)
