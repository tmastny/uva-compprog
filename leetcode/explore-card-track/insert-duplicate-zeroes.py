from typing import List
from collections import deque

# runtime: 33%, O(n) memory
class SolutionQueue:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        queue = deque()
        for i, n in enumerate(arr):
            if queue:
                queue.appendleft(arr[i])
                arr[i] = queue.pop()

            if n == 0:
                queue.appendleft(0)


# runtime: 24%, O(1) memory
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeroes = arr.count(0)

        i = len(arr) - 1
        while i >= 0:
            if i + zeroes < len(arr):
                arr[i + zeroes] = arr[i]

            if arr[i] == 0:
                zeroes -= 1
                if i + zeroes < len(arr):
                    arr[i + zeroes] = arr[i]

            i -= 1


cases = [
    ([1, 0, 2, 3, 0, 4, 5, 0], [1, 0, 0, 2, 3, 0, 0, 4]),
    ([1, 2, 3], [1, 2, 3]),
    ([0], [0]),
]

if __name__ == "__main__":
    for nums, ans in cases:
        orig = nums.copy()

        s = Solution()
        s.duplicateZeros(nums)

        if nums != ans:
            print(f"{orig}, {nums}: {ans}")
