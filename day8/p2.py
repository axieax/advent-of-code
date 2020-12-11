def try_run(lines):
    visited = {x: False for x in range(len(lines))}
    accumulator = 0
    pc = 0
    while True:
        if pc == num_lines:
            print(accumulator)
            return True
        elif visited[pc]:
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
    return False

with open('input.txt', 'r') as f:
    lines = [x.rstrip() for x in f.readlines()]
    num_lines = len(lines)
    # no lines visited
    visited = {x: False for x in range(len(lines))}
    repeated = []

    pc = 0
    while True:
        if visited[pc]:
            if pc in repeated:
                break
            repeated.append(pc)
        visited[pc] = True
        line = lines[pc].split(' ')
        if line[0] == 'acc':
            pc += 1
        elif line[0] == 'jmp':
            pc += int(line[1])
        else:
            pc += 1

    for pc in repeated:
        line = lines[pc].split(' ')
        if line[0] == 'jmp':
            # try changing
            new_line = 'nop ' + line[1]
            lines[pc] = new_line
            if try_run(lines):
                break
            # change back
            lines[pc] = ' '.join(line)
        elif line[0] == 'nop':
            new_line = 'jmp ' + line[1]
            lines[pc] = new_line
            if try_run(lines):
                break
            lines[pc] = ' '.join(line)

