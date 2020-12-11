with open('input.txt', 'r') as f:
    adapters = [0] + sorted([int(x) for x in f.readlines()])
    adapters += [adapters[-1] + 3]
    target = adapters[-1]

    # paths[n] represents the total number of paths from 0 to n
    paths = {}
    paths[0] = 1
    for adapter in adapters:
        for diff in range(1, 4):
            next_adapter = adapter + diff
            if next_adapter in adapters:
                # increase total number of paths to next adapter by number of paths to current adapter
                paths[next_adapter] = paths.get(next_adapter, 0) + paths[adapter]
    print(paths[target])
