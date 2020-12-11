from adt import Node, Graph

# represent data with graph
g = Graph()
with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        split_line = line.split(' ')
        # colour
        colour = ' '.join(split_line[:2])
        n = Node(colour)
        g.add_node(n)
        # contains
        if len(line) == 7:
            # contain no other bags
            g.add_edge(n, None, 0)
        else:
            # add containing bags to graph
            num_contains = (len(split_line) - 4) // 4
            for i in range(num_contains):
                c_num = int(split_line[4 + 4 * i])
                c_colour = ' '.join(split_line[4 + 4 * i + 1: 4 + 4 * i + 3])
                g.add_edge(n, c_colour, c_num)

# ceebs traversing backwards to count
with open("input.txt", "r") as f:
    lines = f.readlines()
    count = 0
    for line in lines:
        colour = ' '.join(line.split(' ')[:2])
        # count number of colours connected to shiny gold
        if g.bfs(colour, 'shiny gold'):
            count += 1
    print(count)
