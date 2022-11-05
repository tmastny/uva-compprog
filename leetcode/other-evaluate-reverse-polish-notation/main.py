from random import randint
from sys import argv


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        return 0


cases = [
    (["2", "1", "+", "3", "*"], 9),
    (["4", "13", "5", "/", "+"], 6),
    (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
]

if __name__ == "__main__":
    for tokens, ans in cases:
        s = Solution()
        output = s.evalRPN(tokens)

        if output != ans:
            print(f"{tokens}, {output}, {ans}")
