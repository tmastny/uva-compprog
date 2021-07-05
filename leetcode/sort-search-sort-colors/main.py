from typing import List

# The unique set of colors is [0, 1, 2]. So this is
# simpler than the general sort case, where the set of
# values is large.

# Constraints:
#   1. in-place
#   2. one-pass
#   3. constant memory

# Two-pass, O(n) memory:
#   count the frequency of each element. Return a
#   a new array built placing elements to the
#   number of elements.

class Solution:
    def sortColors(self, nums: List[int]) -> None:
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
