from typing import List
from collections import defaultdict
from random import randint

# This is the selection algorithm. We can apply the same solution from the
# previous problem. I'll revisit this one to refresh my mind about
# quickselect.

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pass

if __name__ == "__main__":
    cases = [
        [[3,2,1,5,6,4], 2],
        [[3,2,3,1,2,4,5,5,6], 4]
    ]

    s = Solution()
    for nums, k in cases:
        print(s.topKFrequent(nums, k))
