from math import comb
from collections import deque
from collections import defaultdict

class Solution:
    def _choose(self, r, c):
        """
        You get to choose which vertical step to take
        on each path.

        Speed 96, memory 86
        """
        total_steps_to_end = (c - 1) + (r - 1)
        total_vertical_steps = r - 1

        return comb(total_steps_to_end, total_vertical_steps)

    def _dp(self, rows, cols):
        """
        Note that p[i, j] = p[i - 1, j] + p[i, j - 1]

        Speed 99, memory 37
        """

        paths = [[1] * cols] * rows
        for i in range(1, rows):
            for j in range(1, cols):
                paths[i][j] = paths[i - 1][j] + paths[i][j - 1]

        return paths[rows - 1][cols - 1]



    def uniquePaths(self, m: int, n: int) -> int:
        return self._dp(m, n)


if __name__ == "__main__":
    cases = [
        [2, 2, 2],
        [3, 7, 28],
        [3, 2, 3],
        [7, 3, 28],
        [3, 3, 6]
    ]

    s = Solution()
    for m, n, ans in cases:
        print(s.uniquePaths(m, n), ans)
