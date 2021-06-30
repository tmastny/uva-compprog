from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def near_land(grid, r, c):
            rows = len(grid)
            cols = len(grid[0])

            for hshift in [-1, 1]:
                if 0 <= r + hshift < rows and grid[r + hshift][c] == "1":
                    return True

            for vshift in [-1, 1]:
                if 0 <= c + vshift < cols and grid[r][c + vshift] == "1":
                    return True

            return False

        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if islands == 0 and grid[r][c] == "1":
                    islands = 1
                    continue

                if grid[r][c] == "1" and not near_land(grid, r, c):
                    islands += 1

        return islands


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
