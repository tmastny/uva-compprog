from typing import List
from collections import deque

# This problem is very similar to `tree-n-island`.


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def is_word(r, c):
            letters = deque(word[1:])
            queue = deque([(r, c)])

            while queue:
                r, c = queue.pop()

                for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if 0 <= nr < rows and 0 <= nc < cols and board[r][c] == letters[0]:
                        queue.appendleft((r, c))

                letters.pop()

            if letters:
                return False

            return True



        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    return is_word(r, c)

        return False




if __name__ == "__main__":
    cases = [
        [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"],
        [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"],
    ]

    s = Solution()
    for board, word in cases:
        print(s.exist(board, word))
