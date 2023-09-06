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

    def paths(self, v):
        self.visited.add(v)
        paths = 0

        for u in self.adj[v]:
            if u == self.end:
                paths += 1
            elif u not in self.visited:
                paths += self.paths(u)
            else:
                paths += self.pathsat[u]

        self.pathsat[v] = paths
        return paths


def findpaths(G: Graph, start, end):
    G.visited.add(end)
    G.end = end
    G.pathsat = {}

    return G.paths(start)


data = [
    {"A": ["C"], "B": ["A", "D"], "C": ["E", "F"], "D": ["C"], "E": [], "F": []},
    {
        "A": ["C", "F"],
        "B": ["A", "D", "E"],
        "C": [],
        "D": ["C"],
        "E": ["A", "D"],
        "F": ["C"],
    },
]

for adj in data:
    paths = findpaths(Graph(adj), "B", "C")
    print(paths)
