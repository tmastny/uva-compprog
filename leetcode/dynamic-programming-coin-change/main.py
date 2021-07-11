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


class Solution:
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
    ]

    s = Solution()
    for coins, amount, ans in cases:
        print(s.coinChange(coins, amount), ans)
