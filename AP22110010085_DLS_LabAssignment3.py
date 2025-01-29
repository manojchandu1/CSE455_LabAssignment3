class Graph:
    def __init__(self):
        self.graph = {
            'a': ['b', 'c'],
            'b': ['d'],
            'c': ['e'],
            'd': ['e', 'f'],
            'e': ['f'],
            'f': []
        }
    
    def dfs(self, node, depth, max_depth, path, visited_nodes):
        if depth > max_depth:
            return
        
        if node not in visited_nodes:
            visited_nodes.add(node)
            path.append(node)
        
        for neighbor in self.graph.get(node, []):
            if neighbor not in path:
                self.dfs(neighbor, depth + 1, max_depth, path, visited_nodes)
    
    def search(self, start, max_depth):
        path = []
        visited_nodes = set()
        self.dfs(start, 0, max_depth, path, visited_nodes)
        return path

graph = Graph()
start_node = 'a'
max_depth = 2
 
visited_order = graph.search(start_node, max_depth)
print("Nodes visited in order:")
print(" -> ".join(visited_order))

