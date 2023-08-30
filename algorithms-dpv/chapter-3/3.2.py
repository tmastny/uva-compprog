class Graph:
    def __init__(self, adj) -> None:
        self.adj = adj
        
        self.clock = 0
        self.post = {}
        self.pre = {}
        self.visited = {}

    def previsit(self, node):
        self.clock += 1
        self.pre[node] = self.clock

    def postvisit(self, node):
        self.clock += 1
        self.post[node] = self.clock

    def explore(self, node):
        self.visited[node] = True
        self.previsit(node)

        for neighbor in self.adj[node]:
            if not self.visited.get(neighbor, False):
                self.explore(neighbor)
        
        self.postvisit(node)
        

    def dfs(self):
        for node in self.adj:
            if not self.visited.get(node, False):
                self.explore(node)


    def prepost(self):
        output = {}
        for node in self.pre:
            output[node] = (self.pre[node], self.post[node])

        return output


adj_a = {
    'A': ['B', 'F'],
    'B': ['C', 'E'],
    'C': ['D'],
    'D': ['B', 'H'],
    'E': ['D', 'G'],
    'F': ['E', 'G'],
    'G': ['F'],
    'H': ['G']
}

G = Graph(adj_a)
G.dfs()

print(G.prepost())


adj_b = {
    'A': ['B', 'H'],
    'B': ['F'],
    'C': ['B'],
    'D': ['C', 'E'],
    'E': [],
    'F': ['C', 'D', 'E'],
    'G': ['A', 'B', 'F'],
    'H': ['G']
}

G = Graph(adj_b)
G.dfs()

print(G.prepost())
