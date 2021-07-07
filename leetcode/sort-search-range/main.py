from typing import List

# The first idea is to use binary search to find `target`.
# Once target is found, then use a while loop to find
# the first and last occurence. However, the worst case
# time-complexity of this is O(n), in the case where
# every value of `nums` is equal to target.

# Therefore, the solution calls for exponential search
# from the start and end of the array to find the first
# instance of target from beginning and end.


class Solution:
    def _bleft(self, n, target, lo, hi):
        while lo < hi:
            mid = (lo + hi) // 2
            if n[mid] < target:
                lo = mid + 1
            else:
                hi = mid

        return lo

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        `nums` is sorted in ascending order. `target` is value to find in array.
        Goal is to return the starting and ending indices (inclusive) that contain
        the target. If target not found return [-1, -1].

        Speed 45, memory 50
        """
        if len(nums) == 0:
            return [-1, -1]


        left = self._bleft(nums, target, 0, len(nums))
        if left >= len(nums) or nums[left] != target:
            return [-1, -1]

        right = self._bleft(nums, target + 1, 0, len(nums)) - 1

        return [left, right]

if __name__ == "__main__":
    cases = [
        # 0, 1, 2, 3, 4, 5
        [[5, 7, 7, 8, 8, 10], 8],
        [[5, 7, 7, 8, 8, 10], 6],
        [[], 0],
        [[5, 7, 7, 8, 8, 10], 5],
        [[5, 7, 7, 8, 8, 10], 10],
        [[5, 7], 5],
        [[5, 7], 7],
        [[5], 5],
        [[2, 2], 3],
        [[2, 2], 1],
        [[2, 2], 2],
        [[1], 0]
    ]

    s = Solution()
    for nums, target in cases:
        print(f'{target:<2} {s.searchRange(nums, target)}')
