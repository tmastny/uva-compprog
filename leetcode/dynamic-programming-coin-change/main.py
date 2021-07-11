from typing import List

# Must return the minimum number of coins necessary to make the amount.

# Option 1: Greedy
#   Use the largest denomination of coin until the next coin
#   would be greater then the amount. Repeat for the largest.
#   Challenges:
#       Prove that some combination of coins could represent
#       the amount, the greedy strategy would achieve it.
#       (Recall the flashlight-bridge crossing problem, where
#       the greedy approach does not return the minimum.)
#
#       Is this the most efficient approach?


# Option 2: Use the solution to amount - 1
#   This is a typical dynamic programming strategy, where the
#   answer to the current problem can be derived from previous
#   instance.

#   Not immediately obvious how. For example:
#   coins = [1, 5], amount = 5. The solution to 4 would require
#   4 coins, while 5 would require 1.

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        pass


if __name__ == "__main__":
    cases = [[[1, 2, 5], 11, 3], [[2], 3, -1], [[1], 0, 0], [[1], 1, 1], [[1], 2, 2]]

    s = Solution()
    for coins, amount, ans in cases:
        print(s.coinChange(coins, amount), ans)
