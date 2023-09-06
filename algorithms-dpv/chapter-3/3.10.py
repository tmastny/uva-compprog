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
        stack = [node]

        while stack:
            node = stack[-1]
            if node in self.visited:
                if node not in self.post:
                    self.postvisit(node)
                stack.pop()
                continue

            self.visited.add(node)
            self.previsit(node)

            # reversed so process in alphabetical order.
            # not needed, but done to match recursive dfs
            for neighbor in reversed(self.adj[node]):
                if neighbor not in self.visited:
                    stack.append(neighbor)

    def dfs(self):
        for node in self.adj:
            if node not  in self.visited:
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

# {'A': (1, 16), 'B': (2, 15), 'C': (3, 14), 'D': (4, 13), 'H': (5, 12), 'G': (6, 11), 'F': (7, 10), 'E': (8, 9)}
# {'A': (1, 16), 'B': (2, 11), 'F': (3, 10), 'C': (4, 5), 'D': (6, 9), 'E': (7, 8), 'H': (12, 15), 'G': (13, 14)}
for adj in adjs:
    G = Graph(adj)
    G.dfs()
    print(G.prepost())
