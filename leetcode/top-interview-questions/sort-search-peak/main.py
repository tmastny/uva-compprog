from typing import List
from math import inf

# A peak element is any element that is strictly greater
# than it's neighbors. An array may have more than one
# peak element.

# Proof of O(log n) solution.
#   Pick the middle element of the array. There are three
#   possibilites. Either the element is a peak and return that
#   index, or one of the neighbors is larger (because n[i] != n[i + 1]).
#   Without loss of generality, assume the next element is larger.
#
#   Then there are also two cases. Suppose the sequence increases from i + 1
#   to the end. Then the end is the peak, which the recursive algo will
#   find by stepping there by half.

#   Otherwise there is some element
#   that is less than the previous element. Therefore, that previous element
#   is the peak, because the sequence was increasing.

#   ***
#   Another way to think about this proof is thinking about
#   the sequence as a set of increasing subsequences.
#   The algorithm then climbs the current subsequence to the top.


class Solution:
    def _is_peak(self, nums, i):
        return nums[i - 1] < nums[i] and nums[i] > nums[i + 1]

    def _linear(self, nums):
        """
        Speed 49, memory 70 (no call stack)
        """
        for i in range(len(nums)):
            if self._is_peak(nums, i):
                return i

    def _log(self, nums, lo, hi):
        """
        Speed 77, memory 42
        """
        if lo == hi:
            return lo

        i = (lo + hi) // 2

        if self._is_peak(nums, i):
            return i
        elif nums[i - 1] > nums[i]:
            return self._log(nums, lo, i)
        else:
            return self._log(nums, i + 1, hi)

    def findPeakElement(self, nums: List[int]) -> int:
        """
        Note that nums[i] != nums[i + 1] for all i
        """
        nums.append(-inf)
        return self._log(nums, 0, len(nums))


if __name__ == "__main__":
    cases = [[[1, 2, 3, 1], 2], [[1, 2, 1, 3, 5, 6, 4], 5]]

    s = Solution()
    for nums, _ in cases:
        print(s.findPeakElement(nums))
