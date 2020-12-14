from p1 import lines_to_graph

# extract input from file
with open('input.txt', 'r') as f:
    lines = [x.rstrip() for x in f.readlines()]
    g = lines_to_graph(lines)

total_weight = g.weight_dfs('shiny gold')
print(total_weight)
