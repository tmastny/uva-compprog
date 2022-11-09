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
        "9": "wxyz",
    }

    def _combo_r(self, prefix, digits, combos):
        """
        Recursive until there are no more digits, and then
        add the chain to the combination list.

        Need to add only at the bottom of the list, because
        I want the full sequence (or path through the tree),
        not just the subsequence.

        For better memory usage, I could use the index of of the
        current digit, instead of the slice.

        Speed: 84th percentile
        """
        if not digits:
            return combos.append(prefix)

        for letter in self.num_to_letters[digits[0]]:
            self._combo_r(prefix + letter, digits[1:], combos)

    def letterCombinations(self, digits: str) -> List[str]:
        """
        Example: "23"
        "2": "abc"
          a       b       c
        d e f   d e f   d e f

        I feel like there must be a cleaner solution.
        """

        combos = []
        if not digits:
            return combos

        self._combo_r("", digits, combos)

        return combos


if __name__ == "__main__":
    cases = [
        ["23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]],
        ["", []],
        ["2", ["a", "b", "c"]],
        # ["529", []],
    ]

    s = Solution()
    for digits, _ in cases:
        print(s.letterCombinations(digits))
