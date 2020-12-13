def first_multiple_above_earliest(n, earliest):
    ans = 0
    while ans < earliest:
        ans += n
    return ans

with open('input.txt', 'r') as f:
    lines = [x.rstrip() for x in f.readlines()]
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
    
    earliest_bus_service, earliest_bus_id = min(bus_ids)
    print((earliest_bus_service - earliest) * earliest_bus_id)
