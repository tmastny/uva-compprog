from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        n = 3
        ((())), ()()(), (())(), ()(()), (()())
                    (
                         (
                    )         (
                 )          )
                   (      )
                 )      )
        """
        parentheses = []

        def paren(prefix, open, closed):
            if not open and not closed:
                parentheses.append(prefix)

            if open:
                paren(prefix + "(", open[:-1], closed + [")"])

            if closed:
                paren(prefix + ")", open, closed[:-1])

        paren("", [ "(" for _ in range(n)], [])

        return parentheses


if __name__ == "__main__":
    cases = [1, 2, 3]

    s = Solution()
    for n in cases:
        print(s.generateParenthesis(n))
