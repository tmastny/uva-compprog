class UnionFind:
    def __init__(self, numbers):
        self.parent = [0 for _ in range(len(numbers) + 1)]
        self.rank = [0 for _ in range(len(numbers) + 1)]

        for n in numbers:
            self.makeset(n)
    
    def makeset(self, n):
        self.parent[n] = n

    def find(self, n):
        root = self._find_no_path_compression(n)
        print(f"find({n}): {self.parent}")
        
        return root

    def _find_no_path_compression(self, n):
        while self.parent[n] != n:
            n = self.parent[n]
        
        return self.parent[n]

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
    [n for n in range(1, 16 + 1)]
]

for numbers in data:
    uf = UnionFind(numbers)
    
    for k in range(4):
        for n in numbers:
            if n + 2**k > len(numbers):
                break
            uf.union(n, n + 2**k)
