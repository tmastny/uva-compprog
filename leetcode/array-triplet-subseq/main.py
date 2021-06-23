from typing import List
import random


class Solution:
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
        O(n) solution. O(n^2) solution with O(n) memory.
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
        return self._faster_cache(nums)


if __name__ == "__main__":
    s = Solution()

    test_cases = [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [2, 1, 5, 0, 4, 6],
        [1, 1, 5, 0, 3, 4],
        [0, 5, 0, 0, 0],
    ]

    print("\nFunction   Truth")
    print("----------------------")
    for case in test_cases:
        print(
            f"{str(s.increasingTriplet(case)):<5}      {str(s._brute_force(case)):<5}"
        )

    for i in range(100):
        length = random.randint(10, 1000)
        seq = [random.randint(-1000, 1000) for i in range(length)]
        if s._brute_force(seq) != s.increasingTriplet(seq):
            print("Error")
            break
