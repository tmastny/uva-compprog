# long division
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        quotient = []
        if numerator < 0 and denominator > 0 or numerator > 0 and denominator < 0:
            quotient = ["-"]
        if numerator // denominator == 0:
            quotient.append("0")

        numerator, denominator = abs(numerator), abs(denominator)

        digits = []
        while numerator:
            digits.append(numerator % 10)
            numerator //= 10

        trailing_digits = set()
        remainders = set()
        past_decimal = False
        repeating = False
        remainder = 0
        while True:
            digit = digits.pop() if digits else 0

            numerator = remainder * 10 + digit
            output = numerator // denominator

            remainder = numerator - output * denominator

            if past_decimal and output in trailing_digits and remainder in remainders:
                repeating = True
                break
            elif past_decimal:
                trailing_digits.add(output)
                remainders.add(remainder)

            quotient.append(str(output))
            if not past_decimal and output == 0:
                quotient.pop()

            if not past_decimal and not digits:
                if remainder == 0:
                    break

                quotient.append(".")
                past_decimal = True
            elif past_decimal and remainder == 0:
                break

        if repeating:
            quotient.append(")")

            past_decimal = False
            for i, digit in enumerate(quotient):
                if past_decimal and digit == str(output):
                    break
                elif digit == ".":
                    past_decimal = True

            quotient.insert(i, "(")

        return "".join(quotient)


#      045            2.25           0.(4)
#    ------          ____           ____
#  5 | 225        4 | 9.0        9 | 4.0
#      0              8              0
#      22             1 0            4 0
#      20               8            3 6
#       25              20             40
#       25              20
#        0               0

cases = [
    (0, -123413, "0"),
    (-50, 8, "-6.25"),
    (-50, -8, "6.25"),
    (-50, 8, "-6.25"),
    (0, 3, "0"),
    (22, 7, "3.(142857)"),
    (31, 16, "1.9375"),
    (22, 15, "1.4(6)"),
    (4, 9, "0.(4)"),
    (9, 4, "2.25"),
    (1234, 32, "38.5625"),
    (225, 5, "45"),
    (1, 2, "0.5"),
    (2, 1, "2"),
    (4, 333, "0.(012)"),
]

if __name__ == "__main__":
    for num, den, ans in cases:
        s = Solution()
        output = s.fractionToDecimal(num, den)

        if output != ans:
            print(f"{num} / {den} = {output} | {ans}")
