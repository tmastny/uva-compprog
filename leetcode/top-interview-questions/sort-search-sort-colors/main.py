from typing import List

# The unique set of colors is [0, 1, 2]. So this is
# simpler than the general sort case, where the set of
# values is large.

# Constraints:
#   1. in-place
#   2. one-pass
#   3. constant memory

# Two-pass, O(1) memory:
#   count the frequency of each element. Overwrite
#   the array using the count of each element


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        self._zero_two(nums)

    def _zero_two(self, nums):
        """
        In this approach we ignore the one, and swap
        zeroes and twos to the beginning and end of the
        array.

        See https://en.wikipedia.org/wiki/Dutch_national_flag_problem

        Speed: 48th percentile
        """
        zero = 0
        two = len(nums) - 1
        i = 0

        while i <= two:
            if nums[i] == 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[two] = nums[two], nums[i]
                two -= 1
            else:
                i += 1

    def _zero_one(self, nums: List[int]) -> None:
        """
        One pass with swapping. Keep track of the index
        to swap zero or one.

        Speed: 91th percentile, memory 0
        """
        zero = one = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i], nums[zero] = nums[zero], nums[i]

                zero += 1
                if zero - 1 == one:
                    one += 1

            if nums[i] == 1:
                nums[i], nums[one] = nums[one], nums[i]
                one += 1


if __name__ == "__main__":
    cases = [
        [[2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]],
        [[2, 0, 1], [0, 1, 2]],
        [[0], [0]],
    ]

    s = Solution()
    for nums, _ in cases:
        s.sortColors(nums)
        print(nums)
