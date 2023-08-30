class Graph:
    def __init__(self, adj) -> None:
        self.adj = adj
        
        self.clock = 0
        self.post = {}
        self.linear = []

        self.pre = {}
        self.visited = {}

    def previsit(self, node):
        self.clock += 1
        self.pre[node] = self.clock

    def postvisit(self, node):
        self.clock += 1
        self.post[node] = self.clock
        
        self.linear.append(node)

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
    
    def linearization(self):
        self.linear.reverse()
        return self.linear


adj = {
    'A': ['C'],
    'B': ['C'],
    'C': ['D', 'E'],
    'D': ['F'],
    'E': ['F'],
    'F': ['G', 'H'],
    'G': [],
    'H': []
}

G = Graph(adj)
G.dfs()

print(G.prepost())
print(G.linearization())
