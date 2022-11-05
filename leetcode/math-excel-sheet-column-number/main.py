class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ordinal = lambda x: ord(x) - ord("A") + 1

        num = 0
        for pos, letter in enumerate(reversed(columnTitle)):
            num += ordinal(letter) * pow(26, pos)

        return num


cases = [
    ("A", 1),
    ("B", 2),
    ("C", 3),
    ("Z", 26),
    ("AA", 27),
    ("AB", 28),
    ("ZY", 701),
    ("ZZ", 702),
    ("AAA", 703),
]

if __name__ == "__main__":
    for input, ans in cases:
        s = Solution()
        output = s.titleToNumber(input)

        if output != ans:
            print(f"input={input}, output={output}, ans={ans}")
