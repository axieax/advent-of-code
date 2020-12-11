with open('input.txt', 'r') as f:
    lines = [x.rstrip() for x in f.readlines()]
    # no lines visited
    visited = {x: False for x in range(len(lines))}

    accumulator = 0
    pc = 0
    while True:
        if visited[pc]:
            break
        visited[pc] = True
        line = lines[pc].split(' ')
        if line[0] == 'acc':
            accumulator += int(line[1])
            pc += 1
        elif line[0] == 'jmp':
            pc += int(line[1])
        else:
            pc += 1

    print(accumulator)
