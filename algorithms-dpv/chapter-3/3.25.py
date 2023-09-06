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

    def search(self, v):
        self.visited.add(v)
        mincost = self.price[v]

        for u in self.adj[v]:
            if u not in self.visited:
                mincost = min(mincost, self.search(u))
            else:
                mincost= min(mincost, self.cost[u])
        
        self.cost[v] = mincost
        return mincost

    def findmin(self, price, postorder):
        self.price = price
        self.cost = {}

        for v in postorder:
            if v not in self.visited:
                self.search(v)

        return self.cost


def findcost(adj, price):
    G = Graph(adj)
    G.dfs()
    postorder = list(reversed(G.post))

    G = Graph(adj)
    return(G.findmin(price, postorder))

    

data = [
    [
        {
            "A": ["C"],
            "B": ["D"],
            "C": ["E", "F"],
            "D": ["E", "F"],
            "E": [],
            "F": []
        },
        {"A": 2, "B": 3, "C": 6, "D": 1, "E": 4, "F": 5},
    ],
]

for adj, price in data:
    cost = findcost(adj, price)
    print(cost)
