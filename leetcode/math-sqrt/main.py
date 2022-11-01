import random
from math import log

# Newton's method is one option, with the
# quadratic function f(a) = a^2 - x.
# This would also converge to an exact answer.
# Also accurate in only a few iterations, faster
# than O(log n) time.

# Considered quadratically converage, where
# the number of correct digits doubles each iteration.
# https://en.wikipedia.org/wiki/Newton%27s_method#Square_root

# Note: if the initial guess is 1, then the algorithm will
# still be O(log n): 0.5 log2(n).
# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Babylonian_method

# Leetcode: 84th run-time, 95th memory
class Solution1:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        # linear regression initial guess
        sqrt0 = (x / 10 + 1.2) * log(x, 10) / 2

        while True:
            sqrt1 = 0.5 * (sqrt0 + x / sqrt0)

            # end if int answer is the same (since algo
            # converges quadratically)
            if int(sqrt0) == int(sqrt1):
                break

            sqrt0 = sqrt1

        return int(sqrt0)


# But the input space is constrained to integers, 
# so I think we can do a binary search and
# find the answer in O(log n) time.

# 32th percentile
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        lo, hi = 0, x // 2
        while lo < hi:
            mid = (lo + hi) // 2

            mid2 = mid**2
            if x < mid2:
                hi = mid
            elif mid2 < x:
                lo = mid + 1
            else:
                return mid

        return lo if lo**2 <= x else lo - 1

cases = [
    (4, 2),
    (16, 4),
    (8, 2),
    (2, 1)
]

if __name__ == "__main__":
    for x, ans in cases:
        s = Solution()
        output = s.mySqrt(x)

        if output != ans:
            print(f'{x}^.5 = {output} | {ans}')

    for x in [random.randint(1, 2**31 - 1) for _ in range(10)]:
        s = Solution()
        s1 = Solution1()

        ans = s.mySqrt(x)
        ans1 = s1.mySqrt(x)

        if ans != ans1:
            print(f'{x}^.5 = {ans} | {ans1}')