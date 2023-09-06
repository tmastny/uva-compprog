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

    def searchz(self, v):
        self.visited.add(v)

        zmax = 0

        for u in self.adj[v]:
            if u not in self.visited:
                zmax = max(zmax, self.searchz(u))
        
        self.z[v] = zmax
        return max(zmax, self.x[v])


    def z(self, x):
        self.x = x
        self.z = {}

        self.searchz('A')
        return self.z

data = [
    [
        {
            "A": ["B", "E"],
            "B": ["C", "D"],
            "C": [],
            "D": [],
            "E": ["F", "G"],
            "F": [],
            "G": [],
        },
        {"A": 2, "B": 6, "C": 3, "D": 1, "E": 7, "F": 9, "G": 4},
    ],
]

for adj, x in data:
    G = Graph(adj)
    z = G.z(x)
    print(z)
