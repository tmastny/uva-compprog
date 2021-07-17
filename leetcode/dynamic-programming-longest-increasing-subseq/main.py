from typing import List
from operator import itemgetter
from math import inf

# Stable sorting and then looking at the original
# instances is a different instance of the same problem.
# However, one difference is that the gaps are constrained.
# They are not abritrarily large.

# 0 1 2 3 4 5 6 7
# 0 7 6 1 5 2 4 3

#  0  1  2  3  4  5  6  7
# 10  9  2  5  3  7 101 18
#  2  4  3  5  1  0  7  6 <- still the same problem: find the longest increasing subseq
#                            but is constrained to indices
#  2
#  2   4
#  3   4
#      5
#


def print_nums(nums):
    for v, i in nums:
        print(f"{i:>3}", end="")
        # print(f'({v:>2}, {i:>2}) ', end='')
    print()


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        nums = [(v, i) for i, v in enumerate(nums)]
        nums.sort(key=itemgetter(0))

        largest_index = len(nums) - 1
        print_nums(nums)
        max_run = -inf
        increases = [0]
        for _, n in nums:
            if n > max_run:
                max_run = n
                increases[-1] += 1

            if max_run == largest_index:
                max_run = -inf
                increases.append(0)

        return max(increases)


# in index order:
#   First element is the smallest.
#   The element of value zero is the first in the original array.
#   Nothing special about those two values. Could have increasing
#   sequences that don't start with the first, nor the smallest.

if __name__ == "__main__":
    cases = [
        # [[10, 11, 12, 13, 14, 1, 2, 3], 5],
        # [[1, 2, 10, 3, 4], 4],
        # [[0, 10, 11, 12, 13, 1, 2, 3, 4, 5], 6],
        # [[10, 9, 2, 5, 3, 7, 101, 18], 4],
        # [[0, 1, 0, 3, 2, 3], 4],
        [[7, 7, 7, 7, 7, 7, 7], 1],
        # [[0, 7, 6, 1, 5, 2, 4, 3], 4],
        # [[7, 6, 5, 4, 3, 2, 1, 0], 1],
        # [[41, 20, 30, 21, 22, 23, 24, 10], 5],
        # [[7, 1, 5, 2, 3, 4, 6, 0], 5],
        # [[100, 99, 98, 97, 96, 21, 22, 23, 0, 1], 3],
        # [[100, 99, 98, 97, 96, 21, 110, 22, 109, 23, 101, 0, 1], 4],
    ]
    s = Solution()
    for nums, ans in cases:
        print(f"{s.lengthOfLIS(nums):>2} {ans:>2}")

#      array:  2  4  3  5  1  0  7  6
#   max heap:  2  4  4  5  5  5  7  7, max heap increases 4 times

# same as above with real numbers
#      array: 10  9  2  5  3  7  101 18
#   max heap: 10 10 10 10  10 10 101 101

#      array:  11 12  5  7  9  4  3  2  1  0 10  8  6
#   max heap:  11 12  5  7  9  9  9  9  9  9 10  10 10  increased 4 times
#                  ^
#                reset because reached max
