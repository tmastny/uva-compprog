class Graph:
    def __init__(self, adj) -> None:
        self.adj = adj

        self.clock = 0
        self.post = {}
        self.pre = {}
        self.visited = set()

        self.found = False

    def previsit(self, node):
        self.clock += 1
        self.pre[node] = self.clock

    def postvisit(self, node):
        self.clock += 1
        self.post[node] = self.clock

    def find(self, u, v):
        def explore(node):
            if self.found:
                return
            
            self.visited.add(node)

            for neighbor in self.adj[node]:
                if neighbor == u:
                    self.found = True
                    return
                elif neighbor not in self.visited:
                    explore(neighbor)

        self.visited.add(v)
        for neighbor in self.adj[v]:
            if neighbor != u and neighbor not in self.visited:
                explore(neighbor)

        return self.found

    def prepost(self):
        output = {}
        for node in self.pre:
            output[node] = (self.pre[node], self.post[node])

        return output


adjs = [
    {
        'A': ['B', 'D'],
        'B': ['A', 'C', 'D'],
        'C': ['B', 'E'],
        'D': ['A', 'B', 'E'],
        'E': ['C', 'D']
    },
    {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'D'],
        'D': ['B', 'C', 'E'],
        'E': ['D']
    },
    {
        'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B'],
        'E': [],
        'D': []
    }
]

for adj in adjs:
    G = Graph(adj)
    print(G.find("E", "D"))
    
