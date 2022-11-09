from typing import List
from collections import defaultdict
from statistics import median

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


# O(n log(n)) speed, O(1) memory. Sort and calculate longest run
# 58% speed, 0% memory
class SolutionSort:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        nums.sort()

        max_run = 0
        max_el = None
        run = 1
        for i in range(0, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                run += 1
            else:
                if run > max_run:
                    max_el = nums[i]
                    max_run = run
                run = 1

        if run > max_run:
            max_el = nums[i]

        return max_el


# Solution: quickselect / median
# 69% time, 86% memory

# note: why quickselect is O(n): https://stackoverflow.com/questions/8783408/why-is-the-runtime-of-the-selection-algorithm-on
#   You recursive into each half:
#       n + n/2 + n/4 + n/8 + n/16 +...
#       Then by geometric sum, the total is 2n
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return int(median(nums))


# Even faster O(n) time, one-pass algorithm:
# Reference: https://leetcode.com/problems/majority-element/discuss/51613/O(n)-time-O(1)-space-fastest-solution
# Paper: Linear Time Majority Voting Algorithm: https://www.cs.utexas.edu/~moore/best-ideas/mjrty/
# 87% time
# Note: this doesn't actually find the *count* of the majority element, only that
#       it *is* the majority, if the majority exists
# Also note:
#   if majority *may* not exist, you must take an additional pass through
#   the array to confirm it is a majority
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element = None
        counter = 0
        for n in nums:
            if counter == 0:
                element = n
                counter = 1
            else:
                if element == n:
                    counter += 1
                else:
                    counter -= 1

        return element


cases = [
    ([1], 1),
    ([6, 6, 6, 7, 7], 6),
    ([3, 2, 3], 3),
    ([2, 2, 1, 1, 1, 2, 2], 2),
]

if __name__ == "__main__":
    for nums, ans in cases:
        s = Solution()
        output = s.majorityElement(nums)

        if output != ans:
            print(f"{nums}, {output}, {ans}")
