from collections import defaultdict

def twodegree(adj: dict):
    degree = {}
    for v, neighbors in adj.items():
        degree[v] = len(neighbors)
    
    twodegree = defaultdict(int)
    for v, neighbors in adj.items():
        for u in neighbors:
            twodegree[v] += degree[u]
    
    return twodegree

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
    print(twodegree(adj))
