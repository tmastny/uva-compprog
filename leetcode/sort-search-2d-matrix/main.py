from typing import List

# Integers in each row and column are sorted in acsending order.
# Must be O(log n) where `n` is the number of entries in the matrix.


# Partitions matrix into two submatrices (*, &).
# if t > v:         if t < v:
#    v +++++++|       &&&&&++++++|
#    &&&&&&&&&|       &&&&&++++++|
#    ---------|       &&&&&v_____|
#                     &&&&&______|
#                     -----------|

class ColView:
    def __init__(self, matrix, col) -> None:
        self.matrix = matrix
        self.col = col

    def __getitem__(self, key):
        return self.matrix[key][self.col]

    def __len__(self):
        return len(self.matrix)


class Solution:
    def _bleft(self, n, target):
        lo, hi = 0, len(n)

        while lo < hi:
            mid = (lo + hi) // 2

            if n[mid] < target:
                lo = mid + 1
            else:
                hi = mid

        return lo

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
            if self._in_matrix(m, target, (rmid, rmid + 1), (cmid + 1, crange[1])):
                return True

            if self._in_matrix(m, target, (rmid + 1, rrange[1]), (cmid, crange[1])):
                return True


        return False


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self._in_matrix(matrix, target, (0, len(matrix)), (0, len(matrix[0])))

    def _leftmatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        closest_row = min(self._bleft(ColView(matrix, cols // 2), target), rows - 1)
        closest_col = min(self._bleft(matrix[rows // 2], target), cols - 1)

        row_on_col = min(self._bleft(ColView(matrix, closest_col), target), rows - 1)
        if matrix[row_on_col][closest_col] == target:
            return True

        col_on_row = min(self._bleft(matrix[closest_row], target), cols - 1)
        return matrix[closest_row][col_on_row] == target


if __name__ == "__main__":
    cases = [
        [
            [[1, 4, 7, 11, 15]], 15
        ],
        [
            [[1, 4, 7, 11, 15]], 2
        ],
        # [
        #     [
        #         [1, 4, 7, 11, 15],
        #         [2, 5, 8, 12, 19],
        #         [3, 6, 9, 16, 22],
        #         [10, 13, 14, 17, 24],
        #         [18, 21, 23, 26, 30],
        #     ],
        #     5,
        # ],
        # [
        #     [
        #         [1, 4, 7, 11, 15],
        #         [2, 5, 8, 12, 19],
        #         [3, 6, 9, 16, 22],
        #         [10, 13, 14, 17, 24],
        #         [18, 21, 23, 26, 30],
        #     ],
        #     20,
        # ],
        # [
        #     [
        #         [1, 4, 7, 11, 15],
        #         [2, 5, 8, 12, 19],
        #         [3, 6, 9, 16, 22],
        #         [10, 13, 14, 17, 24],
        #         [18, 21, 23, 26, 30],
        #     ],
        #     24,
        # ],
        # [[[3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20],
        # [[[3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 10],
        # [[[1]], 1],
        # [[[1]], 5],
        # [
        #     [
        #         [1, 2, 3, 4, 5],
        #         [6, 7, 8, 9, 10],
        #         [11, 12, 13, 14, 15],
        #         [16, 17, 18, 19, 20],
        #         [21, 22, 23, 24, 25],
        #     ],
        #     5,
        # ],
    ]

    s = Solution()
    for matrix, target in cases:
        print(s.searchMatrix(matrix, target))
