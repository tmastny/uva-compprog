from random import randint
from sys import argv

#   1011
# & 0110
# ------
#   0010

# Can I use a binary carry algorithm?
# Is that too slow? O(n) where n is number of bits.
# (or O(log N) where N is largest number)

# note: bit-wise not: ~x == -x-1
class SolutionBitwise:
    def getSum(self, a: int, b: int) -> int:
        mask = 2**32
        sum = mask
        bit_pos = 0 # (int(log2(bit_pos)) - 1)

        carry = 0
        while a or b or carry:
            abit = a & 1
            bbit = b & 1

            sum |= (carry ^ abit ^ bbit) << bit_pos
            bit_pos += 1

            carry = abit & bbit | (abit | bbit) & carry

            a >>= 1
            b >>= 1

        return sum ^ mask

# Carry-ahead addition overall all bits.
# Example:
#
#  11.                              1010
#  101      101    101       010     010
#  111  &<< 111  ^ 111  &<< 1010  ^  100
# 1100     1010    010       100    1100

# This solution doesn't work for additional bits. See reference
# Reference: https://timmastny.com/blog/adding-integers-logarithmic-time/
# This solution is only calculating the 2nd or 3rd lookahead bit.
# Significantly more comparisons have to happy for all lookahead bits,
# which is why the Reference says it requires so many gates.

# The fundamental algorithm must be sequential, because
# c[i + 1] = a[i]b[i] + (a[i] + b[i])c[i]
class SolutionWrongLookahead:
    def getSum(self, a: int, b: int) -> int:
        and_carry = (a & b) << 1

        xor = a ^ b
        carry_carry = (and_carry & xor) << 1

        return and_carry ^ carry_carry ^ xor

# Example:
#   1        a       b
#   11 |    11      11 |    10       10 |   100      100
# + 01 |  ^ 01  &<< 01 |  ^ 10  &<<  10 | ^  00  &<<  00
#  100 |    10      10 |    00      100 |   100      000

# -7 |   1001      1001 |     1101
#  4 | ^ 0100  &<< 0100 |  ^  1111    ~0010
# -3 |   1101      0000 |     0010     1101 = -3 ----> 0011 = 3
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # explanation of mask:
        # https://leetcode.com/problems/sum-of-two-integers/discuss/489210/Read-this-if-you-want-to-learn-about-masks

        mask = 2**32 - 1 #\ max positive integer in 32 bits
        a &= mask

        while b:
            # sum[i] = propagate   ^ carry
            # sum[i] = a[i] ^ b[i] ^ (a[i-1] & b[i-1])
            # ^sum^    ^--- a ---^   ^----- b -------^
            sum = (a ^ b) & mask
            carry = ((a & b) << 1) & mask

            a = sum
            b = carry

        # return two's complement if leading bit is 1
        # We should just return a, but we have to deal with overflow.
        # The plan is to take two's complement *twice* with the mask
        # to prevent overflow:
        # (a ^ mask) + 1 = two's complement
        # ~((a ^ mask) + 1) + 1 = a (32-bit)
        # Note the 1s cancel out.
        return ~(a ^ mask) if a >> 31 else a

# next step: 2's complement
# flip all the bits and add one:
#   example: 0000 -> 1111 -> (1)0000 = 0 (overflow ignored)
#   example:
#       7 = 0111 -> 1000 -> 1001 = -7
#           0110 <- 0110 <- 1001

# Another way to think about it beyond the procedure:
# The leading bit is negative, but all the other bits
# are their normal positive values. So for example:

# 100 = -4           |   110 = -4 + 2 = -2
# 101 = -3 = -4 + 1  |   111 = -4 + 3 = -1

# Two's complement also literally means that the sum of
# a and two's complement of a equals 2^n for n-bit a.
# This is way a + two's complement of a = 0, when you
# consider the maximum number of n-bits is 2^n - 1.

# Example 3-bit example:
# 3      =  011
# 5 (-3) =  101
# 8      = 1000 <- which is zero "modulo" 3-bit.
#                  Extra bit is discard in mask
# Indeed, it is modular arithmetic modulo 2^n

cases = [
    (301, 799),
    (61, 6),
    (44, 94),
    (193, 370),
    (1, -1),
    (-1, 1),
    (-10, 30),
    (5, 7),
    (20, 30),
    (193, 493),
    (403, 199),
    (403, -199),
    (-403, 199),
    (1, 2),
    (2, 3),
    (4, 0),
    (0, 100),
    (10, -30),
    (-134, -483),
    (134, 483)
]

if __name__ == "__main__":
    for a, b in cases:
        s = Solution()
        output = s.getSum(a, b)

        if output != a + b:
            print(f'{a} + {b} = {output}, {a + b}')

    num = 10
    if len(argv) > 2:
        num = int(argv[2])

    if len(argv) >= 2 and argv[1] == 'sim':
        print("=====> starting sim <======")
        for _ in range(num):
            a = randint(0, 1000)
            b = randint(0, 1000)

            s = Solution()
            output = s.getSum(a, b)
            if output != a + b:
                print(f'{a} + {b} = {output}, {a + b}')
