# long division
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        digits = []
        while numerator:
            digits.append(numerator % 10)
            numerator //= 10

        trailing_digits = set()
        past_decimal = False
        repeating = False
        quotient = []
        remainder = 0
        while True:
            digit = digits.pop() if digits else 0

            numerator = remainder * 10 + digit
            output = numerator // denominator

            remainder = numerator - output * denominator

            if past_decimal and output in trailing_digits:
                repeating = True
                break
            elif past_decimal:
                trailing_digits.add(output)

            quotient.append(str(output))

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

        # remove leading zeroes if necessary
        i = 0
        while quotient[i] == "0":
            i += 1

        if quotient[i] == ".":
            i -= 1

        return "".join(quotient[i:])


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
    (4, 9, "0.(4)"),
    (9, 4, "2.25"),
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
