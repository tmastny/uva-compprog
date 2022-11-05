from typing import List
from collections import defaultdict

# majority element appears more than floor(n / 2) times
# majority element always exists

# Best solution O(n) time, O(1) spaces
#   Naive solution is dictionary counter, but that
#   requires O(n) space

# 43% time, 86% memory
class SolutionDict:
    def majorityElement(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1

        return max(counter, key=counter.get)


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1

        return max(counter, key=counter.get)


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
