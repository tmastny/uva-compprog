from typing import List


class Solution:
    num_to_letter = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wzyz",
    }

    def letterCombinations(self, digits: str) -> List[str]:
        pass


if __name__ == "__main__":
    cases = ["23", "", "2"]

    s = Solution()
    for digits in cases:
        print(s.letterCombinations(digits))
