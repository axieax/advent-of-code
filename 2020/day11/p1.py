def occupied_adjacent_seats(model, row, col):
    ''' returns the number of occupied adjacent seats for a given seat '''
    # constraints
    max_row = len(model)
    max_col = len(model[0])
    
    seats = 0
    # check NW
    if row - 1 >= 0 and col - 1 >= 0 and model[row - 1][col - 1] == '#':
        seats += 1
    # check N
    if row - 1 >= 0 and model[row - 1][col] == '#':
        seats += 1
    # check NE
    if row - 1 >= 0 and col + 1 < max_col and model[row - 1][col + 1] == '#':
        seats += 1
    # check E
    if col + 1 < max_col and model[row][col + 1] == '#':
        seats += 1
    # check SE
    if row + 1 < max_row and col + 1 < max_col and model[row + 1][col + 1] == '#':
        seats += 1
    # check S
    if row + 1 < max_row and model[row + 1][col] == '#':
        seats += 1
    # check SW
    if row + 1 < max_row and col - 1 >= 0 and model[row + 1][col - 1] == '#':
        seats += 1
    # check W
    if col - 1 >= 0 and model[row][col - 1] == '#':
        seats += 1

    return seats


def total_occupied_seats(model):
    ''' returns the number of occupied seats in a model '''
    occupied = 0
    for row in model:
        for space in row:
            if space == '#':
                occupied += 1
    return occupied


if __name__ == '__main__':
    # extract input from file
    with open('input.txt', 'r') as f:
        model = [list(x.rstrip()) for x in f.readlines()]
    
    max_row = len(model)
    max_col = len(model[0])
    while True:
        # copy model - normal model.copy() still contains references to original model rows
        new_model = list(map(list, model))
        num_changes = 0
        for row in range(max_row):
            for col in range(max_col):
                seat = model[row][col]
                if seat == 'L' and occupied_adjacent_seats(model, row, col) == 0:
                    # update seat in new model
                    new_model[row][col] = '#'
                    num_changes += 1
                elif seat == '#' and occupied_adjacent_seats(model, row, col) >= 4:
                    # update seat in new model
                    new_model[row][col] = 'L'
                    num_changes += 1
        # update model
        model = new_model
        # no changes made during iteration
        if num_changes == 0:
            print(total_occupied_seats(model))
            break
