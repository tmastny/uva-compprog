from operator import add, mul, sub
from typing import List

class Solution:
   operators = {"+": add, "-": sub, "*": mul, "/": lambda l, r: int(l / r)}

   def evalRPN(self, tokens: List[str]) -> int:
        tokens = tokens
        stack = []

        for t in tokens:
            if t not in self.operators:
                stack.append(int(t))
                continue


            func = self.operators[t]
            right = stack.pop()
            left = stack.pop()
            stack.append(func(left, right))

        return stack.pop()


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
