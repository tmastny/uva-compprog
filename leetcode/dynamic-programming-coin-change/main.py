from typing import List

# Must return the minimum number of coins necessary to make the amount.

# Option 1: Greedy
#   Use the largest denomination of coin until the next coin
#   would be greater then the amount. Repeat for the next largest.
#
#   If no combination of coins with the largest coin equal the amount,
#   try again with the next largest.
#
#   Counter-example that the greedy solution produces the minimum:
#       coins = [2, 3, 9], amount = 10. 1 9, neither 3 nor 2 make 10.
#       3 3s, 2 does not make 10. Then the greedy approach would return 5 2s.
#       But this isn't the minimum: 2 3s, 2 2s for a minimum of 4.
#
#       (Recall the flashlight-bridge crossing problem, where
#       the greedy approach does not return the minimum.)
#   Could use a more advanced greedy approach that lowers the number
#   of the largest coinage by one if there is no solution. That
#   resolves the counter-example.


# Option 2: Use the solution to amount - 1
#   This is a typical dynamic programming strategy, where the
#   answer to the current problem can be derived from previous
#   instance.

#   Not immediately obvious how. For example:
#   coins = [1, 5], amount = 5. The solution to 4 would require
#   4 coins, while 5 would require 1.

# Option 3: Remainder
#   Find the Remainder for each coin into the amount. This is more
#   efficient than repeatly adding numbers until the next coin
#   would be larger than the total. May only be an optimization
#   to option 1.

# Option 4: recursive
#   Consider this example: [[2, 3, 9], 14]. With 1 9, we need
#   coinage to cover 5. In other words, the problem is now
#   [[2, 3], 5]. Therefore, there is a recursive way to design
#   the algorithm. The think this also leads to the proof of the
#   "advanced" greedy approach.

class Solution:
    def _greedy(self, coins: List[int], amount):
        for i in range(len(coins) - 1, -1, -1):
            n_coins = amount // coins[i]


    def coinChange(self, coins: List[int], amount: int) -> int:
        pass


if __name__ == "__main__":
    cases = [
        [[1, 2, 5], 11, 3],
        [[2], 3, -1],
        [[1], 0, 0],
        [[1], 1, 1],
        [[1], 2, 2],
        [[2, 3, 9], 10, 4],
        [[2, 3, 9], 14, 3]
    ]

    s = Solution()
    for coins, amount, ans in cases:
        print(s.coinChange(coins, amount), ans)
