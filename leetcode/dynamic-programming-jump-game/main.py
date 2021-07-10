from typing import List

# The current value of `n` is the number of indices
# you are allowed to travel moving forward.

# The dynamic programming invariant is the number
# spaces you are allowed to move forward, which is
# based on the current value of the iteration
# and the maximum of the previous (minus the current
# iteration).

# Example:
#   n = [3, 1, 0, 0]
#   i   n[i]     steps
#   0   3        3
#   1   1        max(n[i], last_max - 1) = 2
#   2   0        1
#   3   -        -


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        steps = 0
        for i in range(len(nums) - 1):
            steps = max(nums[i], steps - 1)

            if steps <= 0:
                return False

        return True


if __name__ == "__main__":
    cases = [[[3, 1, 0, 0], True], [[2, 3, 1, 1, 4], True], [[3, 2, 1, 0, 4], False]]

    s = Solution()
    for nums, _ in cases:
        print(s.canJump(nums))
