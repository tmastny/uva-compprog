from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pass


if __name__ == "__main__":
    cases = [[[2, 3, 1, 1, 4], True], [[3, 2, 1, 0, 4], False]]

    s = Solution()
    for nums, _ in cases:
        print(s.canJump(nums))
