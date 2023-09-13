import heapq
from math import inf
from collections import defaultdict

# why decreasekey isn't supported by heapq: https://stackoverflow.com/questions/46996064/how-to-update-elements-within-a-heap-priority-queue?noredirect=1&lq=1S
# to efficiently support decreasekey, you need what Dasguta calls h^{-1}: a dictionary matching every element it's index in h, the heap.
# That means we'd have to rewrite all the heap operations to update h^{-1} as items are inserted or deleted. This would have to be implemented
# in the underlying `bubbleup` routine.


# the alternative implementation of Dijkstra's algorithm is implemented below for simplicity.
class Graph:
    def __init__(self, adj: dict, l: dict) -> None:
        self.adj = adj
        self.l = l
        self.dist = {}

    def dijkstra(self, s):
        visited = set()

        dist = {}
        for node in adj:
            dist[node] = inf

        dist[s] = 0
        queue = [(dist, node) for node, dist in dist.items()]
        heapq.heapify(queue)
        while queue:
            distu, u = heapq.heappop(queue)
            if u in visited:
                continue

            visited.add(u)
            for v in self.adj[u]:
                if dist[v] > distu + self.l[u + v]:
                    dist[v] = distu + self.l[u + v]
                    heapq.heappush(queue, (dist[v], v))

            print(dist)

        self.dist = dist

    def bellmanford(self, s):
        dist = {}
        for node in adj:
            dist[node] = inf
        
        dist[s] = 0

        # with hasupdated, complexity is O(l * |E|),
        # where is l is length of shortest path. 
        for _ in range(len(self.adj) - 1):
            print(dist)
            hasupdated = False
            for (u, v), weight in self.l.items():
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    hasupdated = True

            if not hasupdated:
                break  
        
        for (u, v), weight in self.l.items():
            if dist[v] > dist[u] + weight:
                return "Graph has negative cycle, shortest path does not exist."
        
        self.dist = dist


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
            "AB": 1,
            "AE": 4,
            "AF": 8,
            "BC": 2,
            "BF": 6,
            "BG": 6,
            "CD": 1,
            "CG": 2,
            "DG": 1,
            "DH": 4,
            "EF": 5,
            "GF": 1,
            "GH": 1,
        },
        "A",
    ],
    [
        {
            "SA": 7,
            "SC": 6,
            "SF": 5,
            "SE": 6,
            "AC": -2,
            "AB": 4,
            "BG": -2,
            "BH": -4,
            "CD": 2,
            "CF": 1,
            "EF": -2,
            "EH": 3,
            "FD": 3,
            "GI": -1,
            "HG": 1,
            "IH": 1,
        },
        "S",
    ],
    [
        {"SE": 2, "EB": -4, "BS": 1},
        "S"
    ]
]

for l, start in data:
    adj = ltoadj(l)
    G = Graph(adj, l)

    if start == "A":
        continue
        G.dijkstra(start)
    else:
        result = G.bellmanford(start)
        if result:
            print(result)


    print(G.dist)
