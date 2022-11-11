from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return 0

cases = [
    ([1,1,4,2,1,3], 3),
    ([5,1,2,3,4], 5),
    ([1,2,3,4,5], 0)
]

if __name__ == "__main__":
    for nums, ans in cases:

        s = Solution()
        out = s.heightChecker(nums)

        if nums != ans:
            print(f"{nums}, {out}: {ans}")
