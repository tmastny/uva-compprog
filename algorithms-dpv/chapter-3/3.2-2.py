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


adjs = [
    {
        "A": ["B", "F"],
        "B": ["C", "E"],
        "C": ["D"],
        "D": ["B", "H"],
        "E": ["D", "G"],
        "F": ["E", "G"],
        "G": ["F"],
        "H": ["G"],
    },
    {
        "A": ["B", "H"],
        "B": ["F"],
        "C": ["B"],
        "D": ["C", "E"],
        "E": [],
        "F": ["C", "D", "E"],
        "G": ["A", "B", "F"],
        "H": ["G"],
    },
]

for adj in adjs:
    G = Graph(adj)
    G.dfs()
    print(G.prepost())
