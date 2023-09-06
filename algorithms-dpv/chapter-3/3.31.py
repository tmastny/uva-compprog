class Graph:
    def __init__(self, adj) -> None:
        self.adj = adj

        self.clock = 0
        self.post = {}
        self.pre = {}
        self.visited = set()

    def previsit(self, node):
        self.clock += 1
        self.pre[node] = self.clock

    def postvisit(self, node):
        self.clock += 1
        self.post[node] = self.clock

    def explore(self, node):
        self.visited.add(node)
        self.previsit(node)

        for neighbor in self.adj[node]:
            if neighbor not in self.visited:
                self.explore(neighbor)

        self.postvisit(node)

    def dfs(self):
        for node in self.adj:
            if node not in self.visited:
                self.explore(node)

    def prepost(self):
        output = {}
        for node in self.pre:
            output[node] = (self.pre[node], self.post[node])

        return output

    def findlow(self, v, parent):
        self.visited.add(v)
        self.previsit(v)

        self.low[v] = self.pre[v]

        for u in self.adj[v]:
            if u in self.visited and u != parent:
                self.low[v] = min(self.low[v], self.pre[u])
            elif u not in self.visited:
                self.low[v] = min(self.low[v], self.findlow(u, v))
        
        self.postvisit(v)
        return self.low[v]


def findlow(G: Graph):
    G.low = {}

    for v in G.adj:
        if v not in G.visited:
            G.findlow(v, None)

    return G.low

def findedges(G: Graph):
    edges = set()

    for v in G.adj:
        for u in G.adj[v]:
            edge = "".join(sorted(v + u))
            edges.add(edge)
    
    return edges

def bc(G: Graph, low: dict):
    edges = findedges(G)

    bc = {}
    bridges = set()
    for u, v in edges:
        if low[u] == low[v]:
            bc[u + v] = low[u]
        else:
            bridges.add(u + v)

    return (bc, bridges)

data = [
    {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "D"],
        "D": ["C", "B"],
        "E": ["B", "F", "G"],
        "F": ["E", "G"],
        "G": ["E", "F"]
    },
    {
        "A": ["B", "C"],
        "B": ["A", "C", "D"],
        "C": ["A", "B"],
        "D": ["B", "E"],
        "E": ["D", "F"],
        "F": ["E"]
    },
]

for adj in data:
    G = Graph(adj)
    low = findlow(G)
    print(low)
    print(bc(G, low))
