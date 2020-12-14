def first_multiple_above_earliest(n, earliest):
    ''' returns first multiple of n that is >= earliest '''
    ans = 0
    while ans < earliest:
        ans += n
    return ans

if __name__ == '__main__':
    # extract input from file
    with open('input.txt', 'r') as f:
        lines = [x.rstrip() for x in f.readlines()]
    # earliest timestamp
    earliest = int(lines[0])
    bus_services = lines[1].split(',')
    bus_ids = []
    for bus in bus_services:
        try:
            bus_id = int(bus)
            # tuple: (first timestamp above earliest timestamp, bus_id)
            bus_ids.append((first_multiple_above_earliest(bus_id, earliest), bus_id))
        except ValueError:
            # ignore 'x'
            pass
    
    # get the earliest bus service and its corresponding bus id
    earliest_bus_service, earliest_bus_id = min(bus_ids)
    print((earliest_bus_service - earliest) * earliest_bus_id)
