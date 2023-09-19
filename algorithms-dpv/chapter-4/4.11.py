import heapq
from math import inf


class Graph:
    def __init__(self, adj: dict, l: dict) -> None:
        self.adj = adj
        self.l = l
        self.dist = {}

    def minl(self, s):
        visited = set()

        minl = {}
        for node in adj:
            minl[node] = inf

        minl[s] = 0
        queue = [(min, node) for node, min in minl.items()]
        heapq.heapify(queue)
        while queue: 
            minu, u = heapq.heappop(queue)
            if u in visited:
                continue

            visited.add(u)
            for v in self.adj[u]:
                comparemin = max(self.l[u + v], minu)
                if minl[v] > comparemin:
                    minl[v] = comparemin
                    heapq.heappush(queue, (minl[v], v))

        return minl


def ltoadj(l): 
    nodes = set()
    for start, end in l:
        nodes.add(start)
        nodes.add(end)

    adj = {node: [] for node in sorted(nodes)}
    for start, end in l:
        adj[start].append(end)
  
    return adj


data = [
    [
        {
            "AB": 2,
            "AD": 4,
            "BC": 3,
            "BD": 5,
            # "CE": 3,
            "DE": 1,
        },
        "A",
    ],
    [
        {"AB": 2, "AD": 5, "BC": 2, "CD": 2},
        "A",
    ],
]

for l, start in data:
    adj = ltoadj(l)
    G = Graph(adj, l)

    ml = G.minl(start)
    print(ml)
