from adt import Node, Graph

def lines_to_graph(lines):
    # represent data with graph
    g = Graph()
    for line in lines:
        split_line = line.split(' ')
        # colour
        colour = ' '.join(split_line[:2])
        n = Node(colour)
        g.add_node(n)
        # check contains
        if len(split_line) == 7:
            # contain no other bags
            g.add_edge(n, None, 0)
        else:
            # add containing bags to graph
            num_contains = (len(split_line) - 4) // 4
            for i in range(num_contains):
                c_num = int(split_line[4 + 4 * i])
                c_colour = ' '.join(split_line[4 + 4 * i + 1: 4 + 4 * i + 3])
                g.add_edge(n, c_colour, c_num)
    return g

if __name__ == '__main__':
    # extract input from file
    with open('input.txt', 'r') as f:
        lines = [x.rstrip() for x in f.readlines()]
        g = lines_to_graph(lines)

    # count number of colours connected to shiny gold
    count = 0
    for line in lines:
        colour = ' '.join(line.split(' ')[:2])
        if g.bfs(colour, 'shiny gold'):
            count += 1
    print(count)
