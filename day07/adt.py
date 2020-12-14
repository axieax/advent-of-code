
class Node:
    def __init__(self, colour):
        self.colour = colour

class Graph:
    def __init__(self):
        self.edges = {}
    
    def add_node(self, node):
        self.edges[node.colour] = []
    
    def add_edge(self, node, containing_colour, containing_num):
        if containing_num != 0:
            connection = (containing_colour, containing_num)
            self.edges[node.colour] = self.edges.get(node.colour, []) + [connection]
        else:
            self.edges[node.colour] = []

    def bfs(self, start, target):
        # Visited vertices
        visited = {colour: False for colour in self.edges.keys()}
        found = False
        if start == target:
            return False
        
        # Queue
        queue = [start]
        while queue:
            node = queue.pop(0)
            # target found
            if node == target:
                found = True
                break
            # add unvisited connections to queue
            connections = self.edges[node]
            for connection, weight in connections:
                if not visited[connection] and weight > 0:
                    visited[connection] = True
                    queue.append(connection)
        
        return found


    def weight_dfs(self, bag):
        connections = self.edges[bag]
        if not connections:
            return 0
        
        total_weight = 0
        for connection, weight in connections:
            # includes the bag itself
            total_weight += weight * (self.weight_dfs(connection) + 1)
        return total_weight
