def two_sum(array, target):
    '''
    Returns whether there exists two numbers in the given array which sum to reach target
    '''
    # store visited numbers
    visited = []
    for num in array:
        # complement already visited
        if target - num in visited:
            return True
        # mark num as visited
        visited.append(num)
    return False
    

def find_invalid_number(array):
    '''
    Finds the 'invalid' number in the array which cannot be
    expressed as the sum of two of its previous 25 numbers
    '''
    # check previous 25 numbers    
    for i in range(25, len(array)):
        prev_nums = array[i - 25: i]
        # check whether two numbers in this list sum to this number
        if not two_sum(prev_nums, array[i]):
            # invalid property
            return array[i]


if __name__ == '__main__':
    # extract input from file
    with open('input.txt', 'r') as f:
        array = [int(x) for x in f.readlines()]
    print(find_invalid_number(array))
