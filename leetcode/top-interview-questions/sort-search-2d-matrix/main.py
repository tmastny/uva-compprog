from typing import List

# Integers in each row and column are sorted in acsending order.
# Must be faster than O(n * m).


# This is great resouce, showing an adversial approach
# to complexity analysis: https://stackoverflow.com/a/18160169/6637133
# Also known as the Saddleback search: https://stackoverflow.com/a/2458113/6637133
# Reference includes my solution: http://twistedoakstudios.com/blog/Post5365_searching-a-sorted-matrix-faster


# _in_matrix:
#   Speed 24, memory 10
#
# Partitions matrix into two submatrices (+, &),
# and recursively searches each.
# `_` entries are less than or greater than v.
# if t > v:          if t < v:
#     ______&&&&&|       &&&&&++++++|
#     ______&&&&&|       &&&&&++++++|
#     _____v&&&&&|       &&&&&v_____|
#     ++++++&&&&&|       &&&&&______|
#     -----------|       -----------|
#   Time complexity: O(n^0.7). There are two
#   subproblems at each step, and each subproblem
#   size of size 3/8 * n (or a total of 3/4).
# See here: https://leetcode.com/problems/search-a-2d-matrix-ii/discuss/66154/Is-there's-a-O(log(m)+log(n))-solution-I-know-O(n+m)-and-O(m*log(n))/182918

# _stepthrough:
#   Speed 68, memory 69
# Steps through the entries in order searching
# for target.``
#
# Time complexity O(n + m), which is roughly
# equivalent to O(n^0.5), faster than the recursive
# solution.
#
# Reverts to a linear search when the number of
# rows or columns is one.


class Solution:
    def _stepthrough(self, m, target):
        r = len(m) - 1
        c = 0
        cols = len(m[0])

        while r >= 0 and c < cols:
            if m[r][c] == target:
                return True
            elif target < m[r][c]:
                r -= 1
            else:
                c += 1

        return False

    def _mid(self, range):
        return (range[0] + range[1]) // 2

    def _in_matrix(self, m, target, rrange, crange):
        if (rrange[1] - rrange[0]) == 0 or (crange[1] - crange[0]) == 0:
            return False

        rmid = self._mid(rrange)
        cmid = self._mid(crange)

        entry = m[rmid][cmid]
        if target == entry:
            return True
        elif target < entry:
            if self._in_matrix(m, target, (rrange[0], rmid), (cmid, crange[1])):
                return True

            if self._in_matrix(m, target, rrange, (crange[0], cmid)):
                return True

        else:
            if self._in_matrix(m, target, (rmid + 1, rrange[1]), (crange[0], cmid + 1)):
                return True

            if self._in_matrix(m, target, rrange, (cmid + 1, crange[1])):
                return True

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # return self._in_matrix(matrix, target, (0, len(matrix)), (0, len(matrix[0])))
        return self._stepthrough(matrix, target)


if __name__ == "__main__":
    cases = [
        [[[1, 4, 7, 11, 15]], 15, True],
        [[[1, 4, 7, 11, 15]], 2, False],
        [[[1, 2, 3, 4, 6], [4, 6, 8, 9, 10], [5, 7, 13, 14, 15]], 5, True],
        [
            [
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30],
            ],
            5,
            True,
        ],
        [
            [
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30],
            ],
            20,
            False,
        ],
        [
            [
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30],
            ],
            24,
            True,
        ],
        [[[3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20, False],
        [[[3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 10, True],
        [[[1]], 1, True],
        [[[1]], 5, False],
        [
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            5,
            True,
        ],
        [[[5, 6, 10, 14], [6, 10, 13, 18], [10, 13, 18, 19]], 14, True],
        [
            [
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30],
            ],
            21,
            True,
        ],
    ]

    s = Solution()
    print("Func  solution")
    for matrix, target, solution in cases:
        print(s.searchMatrix(matrix, target), solution)
