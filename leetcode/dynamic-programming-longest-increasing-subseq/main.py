from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        pass


if __name__ == "__main__":
    cases = [
        [[10, 9, 2, 5, 3, 7, 101, 18], 4],
        [[0, 1, 0, 3, 2, 3], 4],
        [[7, 7, 7, 7, 7, 7, 7], 1],
    ]
    s = Solution()
    for nums, ans in cases:
        print(f"{s.lengthOfLIS(nums):>2} {ans:>2}")
