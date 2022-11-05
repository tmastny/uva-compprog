from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return 0


cases = [
    ([3, 2, 3], 3),
    ([2, 2, 1, 1, 1, 2, 2], 2),
]

if __name__ == "__main__":
    for nums, ans in cases:
        s = Solution()
        output = s.majorityElement(nums)

        if output != ans:
            print(f"{nums}, {output}, {ans}")
