def count(right, down):
    # extract input from file
    with open('input.txt', 'r') as f:
        arr = [x.rstrip() for x in f.readlines()]
    # extend row length to be at least 3 * num_rows (has to go across 3 times and down 1 time)
    num_rows = len(arr)
    multiple = right * num_rows // len(arr[0]) + 1 if len(arr[0]) < num_rows else 1
    arr = [list(x * multiple) for x in arr]
    # count trees
    count = 0
    i = 0
    j = 0
    while True:
        i += down
        j += right
        try:
            # tree at specified position in the 2d array
            if arr[i][j] == '#':
                count += 1
        except:
            # out of 2d array bounds
            break
    return count

if __name__=='__main__':
    print(count(3, 1))
