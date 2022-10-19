from typing import List
from collections import deque

cases = [
    [[11, 10], 1],
    [[10, 11], 2],
    [[10, 11, 12, 13, 14, 1, 2, 3], 5],
    [[1, 2, 10, 3, 4], 4],
#    [[0, 10, 11, 12, 13, 1, 2, 3, 4, 5], 6],
#    [[10, 9, 2, 5, 3, 7, 101, 18], 4],
#    [[0, 9, 4, 10, 3, 15, 5, 18, 1, 20], 6],
#    [[0, 1, 0, 3, 2, 3], 4],
#    [[7, 7, 7, 7, 7, 7, 7], 1],
#    [[7, 6, 7, 8], 3],  # have to be careful about how to handle duplicates
#    [[0, 7, 6, 1, 5, 2, 4, 3], 4],
#    [[7, 6, 5, 4, 3, 2, 1, 0], 1],
#    [[41, 20, 30, 21, 22, 23, 24, 10], 5],
#    [[7, 1, 5, 2, 3, 4, 6, 0], 5],
#    [[100, 99, 98, 97, 96, 21, 22, 23, 0, 1], 3],
#    [[100, 99, 98, 97, 96, 21, 110, 22, 109, 23, 101, 0, 1], 4],
#    [[10, 23, 41, 3, 61], 4],
]

def print_nums(nums):
    for i in nums:
        print(f"{i:>3}", end="")
    print()


class Solution:
    
    length_by_index = {}
    max_len = 1 

    def _lengthOfLIS(self, nums, start, length):

        for i in range(start + 1, len(nums)):
            if nums[i] > nums[start]:
                self.max_len = max(
                    self._lengthOfLIS(nums, i, length + 1), self.max_len
                )        
        return length 

    def lengthOfLIS(self, nums: List[int]) -> int:
        self._lengthOfLIS(nums, 0, 1)
        return self.max_len
    
# Find the length of the longest increasing subsequence

if __name__ == "__main__":
    s = Solution()
    for nums, ans in cases:
        print_nums(nums)
        print(f"Calc: {s.lengthOfLIS(nums):>2} Ans: {ans:>2}")
