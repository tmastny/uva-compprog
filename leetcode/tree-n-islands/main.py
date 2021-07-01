# Solution is based on Union-Find data structure,
# see notes in Algorithms I notebook, page 14

from typing import List, Union


class UnionFind:
    def __init__(self) -> None:
        self.parent = []
        self.rank = []
        self.count = 0

    def add(self, x):
        self.parent.append(x)
        self.rank.append(0)
        self.count += 1

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        elif self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[y] = x
            self.rank[x] += 1

        self.count -= 1


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        coords = {}
        index = 0
        uf = UnionFind()
        for r in range(rows):
            for c in range(cols):
                point = grid[r][c]
                if point == "1":
                    if (r, c) not in coords:
                        coords[(r, c)] = index
                        index += 1
                        uf.add(coords[(r, c)])

                    for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == point:
                            if (nr, nc) not in coords:
                                coords[(nr, nc)] = index
                                index += 1
                                uf.add(coords[(nr, nc)])

                            uf.union(coords[(r, c)], coords[(nr, nc)])

        return uf.count


if __name__ == "__main__":
    cases = [
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ],
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ],
    ]

    s = Solution()
    for case in cases:
        print(s.numIslands(case))
