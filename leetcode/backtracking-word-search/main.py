from typing import List
from collections import deque

# This problem is very similar to `tree-n-island`.


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def within(r, c):
            return 0 <= r < rows and 0 <= c < cols

        def is_word(r, c):
            letters = deque(word[1:])
            queue = deque([(r, c, 1)])
            used = set((r, c))

            while queue and letters:
                r, c = queue.pop()
                letter = letters[0]

                found_letter = False
                for nr, nc, i in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if (nr, nc) not in used and within(nr, nc) and board[nr][nc] == letter:
                        queue.appendleft((nr, nc))
                        found_letter = True

                if found_letter:
                    letters.popleft()

                last_rc = (r, c)

            if letters:
                return False

            return True

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if is_word(r, c):
                        return True

        return False


if __name__ == "__main__":
    cases = [
        # [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"],
        # [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"],
        # [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"],
        [[["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"]
    ]

    s = Solution()
    for board, word in cases:
        print(s.exist(board, word))
