# Reference:
#   https://leetcode.com/problems/divide-two-integers/discuss/1516367/Complete-Thinking-Process-or-Intuitive-Explanation-or-All-rules-followed-or-C%2B%2B-code

# Idea:
#   Given: dividend = quotient * divisor + remainder
#   The quotient is the maximum number we can multiple
#   the divisor such that dividend >= quotient * divisor. 

#   We can also write the quotient as powers of two. So
#   we can think of `quotient * divisor` as 
#   divisor * certain powers of 2.
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        quotient = 0
        while dividend > divisor:
            pow2 = divisor
            while pow2 << 1 <= dividend:
                pow2 <<= 1

            quotient += pow2
            dividend -= pow2        
        
        quotient //= divisor
        if quotient > 2**31 - 1:
            return  2**31 - 1
        elif quotient < -2**31:
            return -2**31

        return quotient

cases = [
    (10, 3, 3),
#    (7, -3, -2),
    (58, 5, 11),
    (32, 8, 4),
    (17, 28, 0)
]

if __name__ == "__main__":
    for num, den, ans in cases:
        s = Solution()
        output = s.divide(num, den)

        if output != ans:
            print(f'{num} / {den} = {output} | {ans}')
