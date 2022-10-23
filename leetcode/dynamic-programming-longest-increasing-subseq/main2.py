# Problem: https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/810/

from typing import List
from collections import deque

cases = [
    # [[11, 10], 1],
    # [[10, 11], 2],
    # [[10, 11, 12, 13, 14, 1, 2, 3], 5],
    # [[1, 2, 10, 3, 4], 4],
    [[0, 10, 11, 12, 13, 1, 2, 3, 4, 5], 6],
    # [[10, 9, 2, 5, 3, 7, 101, 18], 4],
    # [[0, 9, 4, 10, 3, 15, 5, 18, 1, 20], 6],
    # [[0, 1, 0, 3, 2, 3], 4],
    # [[7, 7, 7, 7, 7, 7, 7], 1],
    # [[7, 6, 7, 8], 3],  # duplicates
    # [[0, 7, 6, 1, 5, 2, 4, 3], 4],
    # [[7, 6, 5, 4, 3, 2, 1, 0], 1],
    # [[41, 20, 30, 21, 22, 23, 24, 10], 5],
    # [[7, 1, 5, 2, 3, 4, 6, 0], 5],
    # [[100, 99, 98, 97, 96, 21, 22, 23, 0, 1], 3],
    # [[100, 99, 98, 97, 96, 21, 110, 22, 109, 23, 101, 0, 1], 4],
    # [[10, 23, 41, 3, 61], 4],
]


def print_nums(nums):
    for i in nums:
        print(f"{i:>3}", end="")
    print()


# cached dynamic solution. Extremely slow: either
# too slow to pass or in the 99th percentile 
class SolutionSlow:

    lenLISAtIndex = []

    def _findLenLISAtIndex(self, nums, start):
        if self.lenLISAtIndex[start] > 0:
            return self.lenLISAtIndex[start]

        length = 1
        for i in range(start + 1, len(nums)):
            if nums[i] > nums[start]:
                length = max(self._findLenLISAtIndex(nums, i) + 1, length)

        self.lenLISAtIndex[start] = length
        return length

    def lengthOfLIS(self, nums: List[int]) -> int:

        self.lenLISAtIndex = [0 for i in range(len(nums))]

        for i in range(len(nums)):
            self._findLenLISAtIndex(nums, i)

        return max(self.lenLISAtIndex)

# O(n log n):
#   in a strictly increasing sequence, each iteration through
#   nums we add the next element at the end of tails.
#   Up to that point, the length of tails is the length
#   of the longest increasing subsequence. 

#   Once we encounter a non-increasing value, 
#   the length of LIS doesn't increase. But this new
#   value could be the start of a subsequence that is
#   longer than the one we are currently tracking. So
#   we do a binary search to find where the element
#   would go in tails and replace the current value. 
#   That way if there is another value larger than the current
#   max, the length increases. Otherwise, if there are values 
#   greater than the new one, but less than the max,
#   we can keep building that sequence until we expand the array.

# References:
# - Explanation: https://algodaily.com/challenges/longest-increasing-subsequence
# - Solution: https://www.interviewbit.com/blog/longest-increasing-subsequence/
class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # tails[j] is the smallest element of `nums`
        # in a subsequence of length `j`. 
        tails = [0] * len(nums)
        
        # length is the number of non-zero elements in `tails`
        length = 0
    
        # we iterate over each element of `nums` and binary search
        # for the placement in `tails`    
        for n in nums:
            lo, hi = 0, length
            while lo != hi:
                mid = (lo + hi) // 2
                if tails[mid] < n:
                    lo = mid + 1
                else:
                    hi = mid
            tails[lo] = n
            length = max(lo + 1, length)
            
            print(f'n={n:>2}, lo={lo:>2}, hi={hi:>2}, l={length:>2}, tails={tails}')
            
        return length

        

# Find the length of the longest increasing subsequence

if __name__ == "__main__":
    s = Solution()
    for nums, ans in cases:
        print_nums(nums)

        solution = s.lengthOfLIS(nums)
        outcome = "Right!" if solution == ans else "Wrong!"

        print(f"{outcome}: {solution:>2} vs. {ans:>2}")
        print()
