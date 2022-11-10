from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        return 0


cases = [
    ([1, 1, 2], 2, [1, 2, 0]),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4, 0, 0, 0, 0, 0]),
]

if __name__ == "__main__":
    for nums, ans1, ans2 in cases:
        orig = nums.copy()

        s = Solution()
        s.removeDuplicates(nums)

        if nums != ans2:
            print(f"{orig}: -> {nums}: {ans1}, {ans2}")
