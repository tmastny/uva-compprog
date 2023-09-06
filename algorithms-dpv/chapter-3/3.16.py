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


def parallelize(G: Graph):
    G.dfs()
    classes = {}
    postorder = list(reversed(G.post))

    semester = 1
    node = postorder[0]
    

    # check if next node in postorder is a child of
    # current node
    for next in postorder[1:]:
        classes[node] = semester

        # linear
        if next in G.adj[node]:
            semester += 1
        
        node = next

    classes[node] = semester
    return classes

adjs = [
    {"A": ["C"], "B": ["A", "D"], "C": ["E", "F"], "D": ["C"], "E": [], "F": []},
    {
        "A": ["C"],
        "B": ["A", "D"],
        "C": ["E", "F"],
        "D": ["C"],
        "E": [],
        "F": [],
        "G": ["C"],
    },
]

for adj in adjs:
    G = Graph(adj)
    p = parallelize(G)
    print(p)