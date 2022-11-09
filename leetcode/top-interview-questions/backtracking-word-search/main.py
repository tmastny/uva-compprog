from typing import List
from collections import deque

# This problem is very similar to `tree-n-island`.
# Except that I don't think BFS works as well in this case.
# You have to visit each node in a certain order. If you mark
# a node as visited in BFS and the path turns out to be a dead
# end, you must go back and unmark it. But then you will have to
# visit it again. DFS avoids this problem by trying all paths
# until they work.


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Speed: 20, memory 41
        """
        rows = len(board)
        cols = len(board[0])

        def in_board(r, c):
            return 0 <= r < rows and 0 <= c < cols

        def is_word(prefix, r, c, found, used):
            if prefix == word:
                found[0] = True
                return True

            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                next_letter = word[len(prefix)]
                if (
                    in_board(nr, nc)
                    and board[nr][nc] == next_letter
                    and (nr, nc) not in used
                ):
                    is_word(prefix + next_letter, nr, nc, found, used | {(nr, nc)})

                if found[0]:
                    return True

            return False

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if is_word(word[0], r, c, [False], {(r, c)}):
                        return True

        return False


if __name__ == "__main__":
    cases = [
        [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"],
        [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"],
        [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"],
        [
            [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]],
            "ABCESEEEFS",
        ],
        [[["a", "a"]], "aaa"],
    ]

    s = Solution()
    for board, word in cases:
        print(s.exist(board, word))
