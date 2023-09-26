class UnionFind:
    def __init__(self, numbers):
        self.parent = [0 for _ in range(len(numbers) + 1)]
        self.rank = [0 for _ in range(len(numbers) + 1)]

        for n in numbers:
            self.makeset(n)
    
    def makeset(self, n):
        self.parent[n] = n

    def find(self, n):
        root = self._find_recursive_path_compression(n)
        print(f"find({n}): {self.parent}")
        
        return root

    def _find_recursive_path_compression(self, n):
        # path-compression
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])

        return self.parent[n]

    def union(self, a, b):
        roota = self.find(a)
        rootb = self.find(b)

        if roota == rootb:
            return

        if self.rank[roota] > self.rank[rootb]:
            self.parent[rootb] = rootb
        else:
            self.parent[roota] = self.parent[rootb]
            if self.rank[rootb] == self.rank[rootb]:
                self.rank[rootb] += 1
        
        print(f"union({a}, {b}): {self.parent}")

data = [
    [n for n in range(1, 8 + 1)]
]

for numbers in data:
    uf = UnionFind(numbers)
    
    uf.union(1, 2)
    uf.union(3, 4)
    uf.union(5, 6)
    uf.union(7, 8)
    uf.union(1, 4)
    uf.union(6, 7)
    uf.union(4, 5)
    uf.find(1)
