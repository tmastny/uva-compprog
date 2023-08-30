from collections import OrderedDict

class Graph:
    adj = {}
    
    clock = 0
    post = {}
    pre = {}
    
    visited = {}

    def __init__(self, adj) -> None:
        self.adj = adj

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


adj = {
    'A': ['B', 'E'],
    'B': ['A', 'C', 'E'],
    'C': ['B', 'F'],
    'D': ['G', 'H'],
    'E': ['A', 'B', 'F'],
    'F': ['C', 'E', 'I'],
    'G': ['D', 'H'],
    'H': ['D', 'G'],
    'I': ['F']
}

G = Graph(adj)
G.dfs()

print(G.prepost())
