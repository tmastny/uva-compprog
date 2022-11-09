from typing import List
from collections import deque

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        last = arr[0]
        shift = prev_zero = False
        for i, n in enumerate(arr):
            if shift:
                arr[i] = last
                last = n

            if prev_zero:
                last = n
                arr[i] = 0
                prev_zero = False
                shift = True

            if n == 0:
                prev_zero = True



cases = [
    ([1,0,2,3,0,4,5,0], [1,0,0,2,3,0,0,4]),
    ([1,2,3], [1,2,3]),
    ([0], [0]),
]

if __name__ == "__main__":
    for nums, ans in cases:
        orig = nums.copy()

        s = Solution()
        s.duplicateZeros(nums)

        if nums != ans:
            print(f"{orig}, {nums}: {ans}")
