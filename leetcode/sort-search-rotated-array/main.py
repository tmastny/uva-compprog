from typing import List

# Requirements: solution must be O(log n) time.
#   All values are unique. The array is sorted, but
#   rotated an unkown number of times.


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Speed 75, memory 53
        """
        if len(nums) == 1:
            return -1 if target not in nums else 0

        def in_range(n, r):
            if r[0] <= r[1]:
                return r[0] <= n <= r[1]
            return r[0] <= n or n <= r[1]

        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2

            lomid = max(lo, mid - 1)
            himid = min(hi, mid + 1)
            if nums[mid] == target:
                return mid
            elif in_range(target, (nums[lo], nums[lomid])):
                hi = mid - 1
            elif in_range(target, (nums[himid], nums[hi])):
                lo = mid + 1
            else:
                return -1

        return lo


if __name__ == "__main__":
    cases = [
        # 0  1  2  3  4  5  6  7  8
        [[4, 5, 6, 7, 0, 1, 2], 0],
        [[4, 5, 6, 7, 0, 1, 2], 3],
        [[1], 0],
        [[0], 0],
        [[5, 4, 3, 2, 1], 5],
        [[5, 6, 0, 1, 2, 3, 4, 5], 0],
        [[2, 3, 4, 5, 6, 0, 1], 6],
        [[1, 2, 3, 4, 5, 6, 7, 8, 0], 0],
        [[1, 0], 0],
        [[1, 3, 5], 3],
    ]

    s = Solution()
    for nums, target in cases:
        print(s.search(nums, target))
