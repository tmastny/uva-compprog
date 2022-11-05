from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Each time an open parenthese is added to the string,
        an additional closed parenthese must be added in the future.

        Speed: 67th percentile. Memory: 0th (used slices instead of indices)

        Example:
        n = 3
        ((())), ()()(), (())(), ()(()), (()())

        i    prefix     open    closed
        0               (((
        1    (          ((      )
        2    ((         (       ))
        3    (()        (       )
        """
        parentheses = []

        def paren(prefix, open, closed):
            if not open and not closed:
                parentheses.append(prefix)

            if open:
                paren(prefix + "(", open[:-1], closed + [")"])

            if closed:
                paren(prefix + ")", open, closed[:-1])

        paren("", ["(" for _ in range(n)], [])

        return parentheses


if __name__ == "__main__":
    cases = [1, 2, 3]

    s = Solution()
    for n in cases:
        print(s.generateParenthesis(n))
