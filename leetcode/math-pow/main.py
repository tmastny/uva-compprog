# this solution is O(n)
class SolutionSlow:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            x = 1 / x
            n *= -1
        
        pow = x
        for i in range(n - 1):
            pow *= x
        
        return pow

# O(log n)
#   let n = 9. In binary, 9 = 1001_b = 2^3 + 2^0.
#   Then x^9 = x^(2^3 + 2^0) = x^(2^3) * x^(2^0).

# This means the solution is O(log n), because
# we only have to calculate powers of x for the number
# of bits of `n` (which is log2 n)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n *= -1

        pow = 1
        while n:
            if n & 1:
                pow *= x
            
            # this repeatedly squares x for each bit of n
            # x^2, x^2 * x^2 = x^4, x^4 * x^4 = x^8, etc.
            # Multiple x to pow when the bit is set
            x *= x
            n >>= 1

        return pow

cases = [
    (2, 2, 4),
    (2, 9, 512),
    (2, 10, 1024),
    (2.1, 3, 9.261),
    (2, -2, 0.25),
    (13142, 0, 1),
    (2, 3, 8)
]

if __name__ == "__main__":
    for x, n, ans in cases:
        s = Solution()
        output = s.myPow(x, n)

        if output != ans:
            print(f'{x}^{n} = {output} | {ans}')