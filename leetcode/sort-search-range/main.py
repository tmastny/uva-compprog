from typing import List

# Given a set of intervals, return a set of non-overlapping
# intervals that cover all intervals in the input.
# Input intervals are inclusive, so [1, 4], [4, 5] are overlappig
# and should output [1, 5]

# Time O(n log n), memory O(n):
#   1. sort the array.
#   2. Compare the start of the interval to the end of the last one.
#      If they overlap, combine them.


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Speed 54, memory 53
        """
        intervals.sort()

        merged = []
        for interval in intervals:
            if len(merged) and interval[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], interval[1])
            else:
                merged.append(interval)

        return merged


if __name__ == "__main__":
    cases = [
        [[5, 6], [1, 4]],
        [[1, 3], [2, 6], [8, 10], [15, 18]],
        [[1, 4], [4, 5]],
        [[1, 5], [2, 6], [2, 10]],
        [[20, 30]],
        [[20, 20]],
        [[1, 4], [2, 3]],
        [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]],
    ]

    s = Solution()
    for intervals in cases:
        print(s.merge(intervals))
