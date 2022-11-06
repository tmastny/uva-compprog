# long division
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        output = []

        while len(output) < 10:
            output.append(numerator // denominator)
            numerator -= output[-1] * denominator

        return ""

#      045            2.25           0.(44)
#    ------          ____           ____
#  5 | 225        4 | 9.0        9 | 4.0
#      0              8              0
#      22             1 0            4 0
#      20               8            3 6
#       25              20             40
#       25              20
#        0               0

cases = [
    (225, 5, "45"),
    (1, 2, "0.5"),
    (2, 1, "2"),
    (4, 333, "0.(012)")
]

if __name__ == "__main__":
    for num, den, ans in cases:
        s = Solution()
        output = s.fractionToDecimal(num, den)

        if output != ans:
            print(f"{num} / {den} = {output} | {ans}")
