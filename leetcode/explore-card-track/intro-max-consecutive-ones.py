from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones = max_ones = 0
        for n in nums:
            if n == 1:
                ones += 1
                if ones > max_ones:
                    max_ones = ones
            else:
                if ones > max_ones:
                    max_ones = ones
                ones = 0

        return max_ones


cases = [([1, 1, 0, 1, 1, 1], 3), ([1, 0, 1, 1, 0, 1], 2)]

if __name__ == "__main__":
    for nums, ans in cases:
        s = Solution()
        output = s.findMaxConsecutiveOnes(nums)

        if output != ans:
            print(f"{nums}, {output}: {ans}")
