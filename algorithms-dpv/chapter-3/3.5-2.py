from collections import defaultdict


class Graph:
    def __init__(self, adj) -> None:
        self.adj = adj

        self.clock = 0

        self.cc = {}
        self.ccnum = 0

        self.post = {}
        self.postnodes = []

        self.pre = {}
        self.visited = {}

    def previsit(self, node):
        self.clock += 1
        self.pre[node] = self.clock

        self.cc[node] = self.ccnum

    def postvisit(self, node):
        self.clock += 1
        self.post[node] = self.clock

        self.postnodes.append(node)

    def explore(self, node):
        self.visited[node] = True
        self.previsit(node)

        for neighbor in self.adj[node]:
            if not self.visited.get(neighbor, False):
                self.explore(neighbor)

        self.postvisit(node)

    def dfs(self, order=None):
        nodes = order if order else self.adj

        for node in nodes:
            if not self.visited.get(node, False):
                self.ccnum += 1
                self.explore(node)

    def reverse(self):
        """Cleaner approach without recursion"""
        adj = defaultdict(list)

        for node, neighbors in self.adj.items():
            if node not in adj:
                adj[node] = []
                 
            for neighbor in neighbors:
                adj[neighbor].append(node)

        self.adj = adj

    def prepost(self):
        output = {}
        for node in self.pre:
            output[node] = (self.pre[node], self.post[node])

        return output


def ssc(adj):
    Gr = Graph(adj)
    Gr.reverse()
    Gr.dfs()

    order = list(reversed(Gr.postnodes))

    G = Graph(adj)
    G.dfs(order)

    return G.cc


adjs = [
    {
        "A": ["C", "H"],
        "B": ["A"],
        "C": ["D"],
        "D": ["F"],
        "E": ["A", "I"],
        "F": ["J"],
        "G": ["I"],
        "H": ["F", "G"],
        "I": ["H"],
        "J": ["C"],
    },
    {
        "A": ["B", "D"],
        "B": ["C", "E"],
        "C": ["F"],
        "D": ["H"],
        "E": ["A", "H"],
        "F": ["I"],
        "G": ["D"],
        "H": ["F", "G", "I"],
        "I": ["H"],
    },
]

for adj in adjs:
    print(ssc(adj))
