from collections import defaultdict


class Graph:
    def __init__(self, adj) -> None:
        self.adj = adj

        self.clock = 0

        self.post = {}

        self.pre = {}
        self.visited = set()
        self.bipartite = True

    def previsit(self, node):
        self.clock += 1
        self.pre[node] = self.clock


    def postvisit(self, node):
        self.clock += 1
        self.post[node] = self.clock

    def isevencycle(self, node, neighbor):
        # distance from neighbor to node plus one more edge from
        # node to neighbor
        cycle = self.pre[node] - self.pre[neighbor] + 1
        return (cycle % 2) == 0

    def explore(self, node):
        self.visited.add(node)
        self.previsit(node)

        for neighbor in self.adj[node]:
            if neighbor in self.visited:
                self.bipartite &= self.isevencycle(node, neighbor)
            else:
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
        'C': ['A', 'B']
    }
]

for adj in adjs:
    G = Graph(adj)
    G.dfs()
    print(G.bipartite)
