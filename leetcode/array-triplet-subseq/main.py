from typing import List

class Solution:
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

    def _sequential_difference(self, nums):
        n_increases = 0
        max = nums[0]

        for i in range(len(nums)):
            if nums[i] > max:
                n_increases += 1
                max = nums[i]

        return n_increases >= 2

    def increasingTriplet(self, nums: List[int]) -> bool:
        return self._sequential_difference(nums)


if __name__ == "__main__":
    s = Solution()

    test_cases = [
        [1,2,3,4,5],
        [5,4,3,2,1],
        [2,1,5,0,4,6]
    ]

    for case in test_cases:
        print(s.increasingTriplet(case))
