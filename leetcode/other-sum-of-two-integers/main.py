from math import log2
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
        mask = 2**10
        sum = mask
        bit_pos = 0 # (int(log2(bit_pos)) - 1)

        carry = 0
        while a or b or carry:
            abit = a & 1
            bbit = b & 1

            sum |= (carry ^ abit ^ bbit) << bit_pos
            bit_pos += 1

            carry = abit & bbit

            a >>= 1
            b >>= 1

        return sum ^ mask

class Solution:
    def getSum(self, a: int, b: int) -> int:

        and_carry = (a & b) << 1

        xor = a ^ b
        carry_carry = (and_carry & xor) << 1

        return and_carry ^ carry_carry ^ xor
#  11
#  101      101    101       010
#  111  &<< 111  ^ 111  &<< 1010
# 1100     1010    010       100

# next step: 2's complement

cases = [
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
