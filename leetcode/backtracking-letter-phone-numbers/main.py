from typing import List


class Solution:
    num_to_letters = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wzyz",
    }

    def _combo_r(self, digits, combos):
        if not digits:
            return ""

        for i in range(len(digits)):
            for letter in self.num_to_letters[digits[i]]:
                for j in range(i + 1, len(digits)):
                    for letterj in self.num_to_letters[digits[j]]:
                        combos.append(letter + letterj)


    def letterCombinations(self, digits: str) -> List[str]:
        """
        Example: "23"
        "2": "abc"
          a       b       c
        d e f   d e f   d e f
        """
        # if len(digits) == 1:
        #     return list(self.letterCombinations[digits])

        combos = []
        self._combo_r(digits, combos)

        return combos

if __name__ == "__main__":
    cases = [
        ["23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]],
        ["", []],
        ["2", ["a", "b", "c"]],
    ]

    s = Solution()
    for digits, _ in cases:
        print(s.letterCombinations(digits))
