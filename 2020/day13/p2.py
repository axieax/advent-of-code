from functools import reduce

with open('input.txt', 'r') as f:
    lines = [x.rstrip() for x in f.readlines()]
    all_bus_services = lines[1].split(',')
    # list of tuples: bus_id (ignoring 'x'), bus_index (add to t)
    restricted_bus_services = [(int(bus_id), index) for (index, bus_id) in enumerate(all_bus_services) if bus_id != 'x']
    
# We want to find t such that (t + bus_index) % bus_id = 0 for each bus
# this is the same as (t + bus_index) = 0 (mod bus_id)
# so t = -bus_index (mod bus_id) = (bus_id - bus_index) (mod bus_id)
# The Chinese Remainder Theorem can be applied since all bus_indices are coprime
# t = \sum_i{b_i * N_i * x_i}

# let N (LCM) be the product of the n_i's, and 
N = reduce(lambda x, y: x * y, [bus[0] for bus in restricted_bus_services])
ans = 0
for bus_id, bus_index in restricted_bus_services:
    # let b_i be the remainder: (bus_id - bus_index)
    b_i = bus_id - bus_index
    # let n_i be the divisor: (bus_id)
    n_i = bus_id
    # let N_i be N / n_i (what to multiply by n_i to get the LCM: N)
    N_i = N // n_i
    # let x_i be the inverse of N_i in modulo n_i: (N_i * x_i) = 1 (mod n_i)
    x_i = pow(N_i, -1, bus_id)
    ans += b_i * N_i * x_i
print(ans % N)
