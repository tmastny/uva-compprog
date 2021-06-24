import math
from typing import List
import random


class Solution:
    def _fastest(self, nums):
        lo = math.inf
        mid = math.inf

        for n in nums:
            if n <= lo:
                lo = n
            elif n <= mid:
                mid = n
            else:
                return True

        return False

    def _fast_no_cache(self, nums):
        """
        O(n) time and O(1) memory, from the internet.
        Find a pair lo, mid. Then see if next number is hi,
        completing the triplet.

        During iteration, keep track of min. Then for any
        element after the new min such that `min < nums[i]`
        update lo = min and mid = nums[i]
        """
        next_lo = None
        lo = nums[0]
        mid = None
        # [1, 5, 0, 4, 1, 3]
        for i in range(1, len(nums)):
            if mid is None:
                if nums[i] > lo:
                    mid = nums[i]
                else:
                    lo = nums[i]
                continue

            if nums[i] > mid:
                return True

            if lo < nums[i] < mid:
                mid = nums[i]

            if next_lo is None and nums[i] < lo:
                next_lo = nums[i]

            if next_lo is not None:
                if nums[i] < next_lo:
                    next_lo = nums[i]

                elif nums[i] > next_lo:
                    mid = nums[i]
                    lo = next_lo
                    next_lo = None

        return False

    def _max_array_cache(self, nums):
        """
        Build cache of upcoming subarray maximums in O(n).
        """
        imax = [nums[-1]]
        for n in reversed(nums):
            if n > imax[-1]:
                imax.append(n)
            else:
                imax.append(imax[-1])
        imax.reverse()
        imax.pop()

        return imax

    def _faster_cache(self, nums):
        """
        O(n) solution. Same strategy as O(n^2), but saves a loop by using O(n) memory.
        The challenge of a solution with O(n) memory is that the algorithm subtracts
        elements from the upcoming subarray (compared to adding elements to the previous
        subarray). This means if we removed the max, we we would need to search the
        upcoming subarray to find it.
        """
        if len(nums) < 3:
            return False

        imin = nums[0]
        imax = self._max_array_cache(nums)

        for i in range(1, len(nums) - 1):
            imin = min(imin, nums[i - 1])

            if imin < nums[i] < imax[i + 1]:
                return True

        return False

    def _faster_brute(self, nums):
        """
        O(n^2) brute force. Can I cache this approach?
        I have an almost fixed look-back.
        """
        for i in range(1, len(nums) - 1):
            mmin = min(nums[0:i])
            mmax = max(nums[i + 1 : len(nums)])
            if mmin < nums[i] < mmax:
                return True

        return False

    def _brute_force(self, nums):
        """
        Brute force, O(n^3) solution.
        """
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] < nums[j] < nums[k]:
                        return True

        return False

    def increasingTriplet(self, nums: List[int]) -> bool:
        return self._fastest(nums)


if __name__ == "__main__":
    s = Solution()

    test_cases = [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [2, 1, 5, 0, 4, 6],
        [1, 1, 5, 0, 3, 4],
        [0, 5, 0, 0, 0],
        [20, 100, 10, 12, 5, 13],
        [1, 5, 0, 4, 1, 3],
    ]

    print("\nFunction   Truth")
    print("----------------------")
    for case in test_cases:
        print(
            f"{str(s.increasingTriplet(case)):<5}      {str(s._brute_force(case)):<5}"
        )

    errors = 0
    for i in range(10):
        length = random.randint(10, 1000)
        seq = [random.randint(-1000, 1000) for i in range(length)]
        if s._brute_force(seq) != s.increasingTriplet(seq):
            errors += 1

    if errors:
        print(f"Errors: {errors}")
