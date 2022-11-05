from typing import List
from collections import defaultdict
from random import randint

# This is the selection algorithm. We can apply the same solution from the
# previous problem. I'll revisit this one to refresh my mind about
# quickselect.


# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# You must solve it in O(n) time complexity.
# https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/800/


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pass


if __name__ == "__main__":
    cases = [[[3, 2, 1, 5, 6, 4], 2, 5], [[3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 5]]

    s = Solution()
    for nums, k, ans in cases:
        print(s.topKFrequent(nums, k))
