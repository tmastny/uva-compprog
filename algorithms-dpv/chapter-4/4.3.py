from collections import deque


class Graph:
    def __init__(self, adj: dict) -> None:
        self.adj = adj
        self.dist = {}
        self.prev = {}

    def bfs(self, node):
        queue = deque([node])
        dist = {node: 0}
        prev = {node: None}

        while queue:
            u = queue.pop()

            for v in self.adj[u]:
                if v not in dist:
                    dist[v] = dist[u] + 1
                    prev[v] = u
                    queue.appendleft(v)

        self.dist = dist
        self.prev = prev

    def shortestpaths(self, start, end):
        self.bfs(start)

        path = set()
        node = end
        while node:
            path.add(node)
            node = self.prev[node]

        paths = 1
        for u in self.adj:
            if u not in path:
                for v in self.adj[u]:
                    if v in path and self.dist[v] == self.dist[u] + 1:
                        paths += 1

        return paths


data  = [
    [
        {
            "A": ["A", "B", "E"],
            "B": ["A", "D"],
            "C": ["D", "E"],
            "D": ["B", "C", "E"],
            "E": ["A", "C", "D"],
        },
        "D",
    ],
    [
        {
            "A": ["B", "C"],
            "B": ["A", "D"],
            "C": ["A", "D"],
            "D": ["B", "C", "E"],
            "E": ["D"],
        },
        "E",
    ],
]

for adj, end in data:
    G = Graph(adj)
    paths = G.shortestpaths("A", end)
    print(paths)
