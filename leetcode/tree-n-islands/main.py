# Solution is based on Union-Find data structure,
# see notes in Algorithms I notebook, page 14
# and https://algs4.cs.princeton.edu/15uf/
# https://en.wikipedia.org/wiki/Disjoint-set_data_structure

from typing import List
from collections import deque


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
            x, y = y, x

        self.parent[y] = x

        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1

        self.count -= 1


class UnionFindRC(UnionFind):
    def __init__(self, n) -> None:
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
        self.count = n


class Solution:
    def _coord_index_type_unionfind(self, grid):
        """
        This is very similar to `_coord_to_index_unionfind`, but uses
        a direct mapping of the coordinates to indices of the UnionFind
        array.

        It also adds additional logic to keep track of the land connected
        components.

        Speed: 0th percentile
        """
        rows = len(grid)
        cols = len(grid[0])

        def rci(r, c):
            return cols * r + c

        coords = {}
        index = 0
        uf = UnionFindRC(rows * cols)
        for r in range(rows):
            for c in range(cols):
                point = grid[r][c]
                for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == point:
                        uf.union(rci(r, c), rci(nr, nc))

        def irc(n):
            c = n % cols
            r = (n - c) // cols
            return (r, c)

        islands = set()
        for i in range(rows * cols):
            r, c = irc(uf.find(i))
            if grid[r][c] == "1" and (r, c) not in islands:
                islands.add((r, c))

        return len(islands)

    def _coord_to_index_unionfind(self, grid):
        """
        Maps tuple of coordinates (r, c) to a unique index for UnionFind.
        Each time a coordinate is visited for the first time, it's assigned
        a unique index and added to UnionFind. It's then `union`ed to the
        surroudning points.

        Only `land` is considered. If water is also considered, the water
        will also contribute to the connected component count. Example:
        1 1 0
        0 0 1  Two islands, but four connected components.
        0 0 1

        Speed: 10th percentile.
            My guess is the slow performance has to do with the coord-to-index
            hashing.
        """
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

    def _dfs(self, grid):
        """
        Treat neighboring islands as land. Once you visit land,
        visit all connecting points (and mark them connected (dict or "*")).

        Then search for unvisited landed. All the other connected components
        will already be visited, any new one is a different island.

        I think of it as trying all paths in the maze.

        So the input isn't permenantly modified, could go back and replace
        "*" with "1".

        Speed: 48th percentile
        Memory: 26th
        """
        rows = len(grid)
        cols = len(grid[0])

        def visit(r, c):
            if not (0 <= r < rows and 0 <= c < cols):
                return

            if grid[r][c] != "1":
                return

            grid[r][c] = "*"
            neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
            for nr, nc in neighbors:
                visit(nr, nc)

        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    visit(r, c)
                    islands += 1

        return islands

    def _bfs(self, grid):
        """
        Same idea as `_dfs`, but doing a bfs. Maybe mildly
        faster, since it doesn't have to use the call stack.

        Speed: 48th percentile
        Memory: 85th
        """
        rows = len(grid)
        cols = len(grid[0])

        def visit(r, c):
            queue = deque([(r, c)])

            while queue:
                r, c = queue.pop()
                if not (0 <= r < rows and 0 <= c < cols):
                    continue
                if grid[r][c] != "1":
                    continue

                grid[r][c] = "*"

                neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
                for nr, nc in neighbors:
                    queue.appendleft((nr, nc))

        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    visit(r, c)
                    islands += 1

        return islands

    def numIslands(self, grid: List[List[str]]) -> int:
        return self._bfs(grid)


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
