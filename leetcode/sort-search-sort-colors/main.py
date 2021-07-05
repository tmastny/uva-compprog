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
        index = {0: None, 1: None, 2: None}
        print('i nums')
        for i in range(len(nums)):
            if index[nums[i]] is None:
                index[nums[i]] = i

            if nums[i] == 1 and index[2] is not None:
                nums[i], nums[index[2]] = nums[index[2]], nums[i]
                index[1] = index[2]
                index[2] += 1

            elif nums[i] == 0 and index[1] is not None:
                nums[i], nums[index[1]] = nums[index[1]], nums[i]
                index[1] += 1

            elif nums[i] == 0 and index[2] is not None:
                nums[i], nums[index[2]] = nums[index[2]], nums[i]
                index[2] += 1
            print(f'{i} {nums}')


if __name__ == "__main__":
    cases = [
        [[2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]],
        # [[2, 0, 1], [0, 1, 2]],
        # [[0], [0]],
    ]

    s = Solution()
    for nums, _ in cases:
        s.sortColors(nums)
        print(nums)
