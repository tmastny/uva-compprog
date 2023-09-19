import heapq
from math import inf


class Graph:
    def __init__(self, adj: dict, l: dict) -> None:
        self.adj = adj        
        
        self.l = {}
        for edge, weight in l.items():
            self.l[edge] = weight

            opposite = "".join(reversed(edge))
            self.l[opposite] = weight

        self.dist = {}


    def dijkstra(self, s):
        visited = set()

        dist = {}
        for node in adj:
            dist[node] = inf

        prev = {}
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
                    prev[v] = u
                    heapq.heappush(queue, (dist[v], v))

        self.prev = prev
        self.dist = dist


    def findbestroad(self, roads: dict):
        self.dijkstra("S")

        stack = ["T"]
        while stack[-1] != "S":
            stack.append(self.prev[stack[-1]])

        spt = {node: self.dist["T"] - self.dist[node] for node in stack}

        while stack:
            u = stack.pop()
            for v in self.adj[u]:
                if v in spt:
                    continue
                if self.dist[v] + self.l[v + u] == self.dist[u]:
                    spt[v] = spt[u] + self.l[v + u]
                    stack.append(v)

        bestroad = None
        shortestpath = self.dist["T"]
        for (start, end), length in roads.items():
            if end not in spt:
                continue

            newdist = self.dist[start] + length + spt[end]
            if newdist < shortestpath:
                shortestpath = newdist
                bestroad = {start + end: length}

        return bestroad




def ltoadj(l):
    nodes = set()
    for start, end in l:
        nodes.add(start)
        nodes.add(end)

    adj = {node: [] for node in sorted(nodes)}
    for start, end in l:
        adj[start].append(end)
        adj[end].append(start)

    return adj


data = [
    [
        {
            "SA": 2,
            "SE": 3,
            "SF": 1,
            "AB": 2,
            "BT": 2,
            "ET": 3,
        },
        {"FB": 2, "AC": 4, "BE": 1},
    ]
]

for l, roads in data:
    adj = ltoadj(l)
    G = Graph(adj, l)

    road = G.findbestroad(roads)
    print(road)
