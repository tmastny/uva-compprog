from typing import List


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        pass


if __name__ == "__main__":
    cases = [[[3, 1, 0, 0], True], [[2, 3, 1, 1, 4], True], [[3, 2, 1, 0, 4], False]]

    s = Solution()
    for nums, _ in cases:
        print(s._backfront(nums))
