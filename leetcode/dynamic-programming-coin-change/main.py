from collections import defaultdict
from typing import List
from math import inf

# Must return the minimum number of coins necessary to make the amount.
# See: Algorithms 1 notebok, page 18.

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
#   "advanced" greedy approach. Thinking working backwards: take the
#   minimum solution, and show that the greedy algorithm would have
#   reached it.


class Solution:
    def _greedy(self, coins: List[int], amount, coin_index, total_coins):
        """
        Call:
            coins.sort()
            return self._greedy(coins, amount, len(coins) - 1, 0)

        Greedy solution doesn't not work in general. If any solution
        exists in the greedy path before the minimum, that solution will
        be reported. For example: [[13, 9, 3, 1], 21, 3]
        """
        if amount == 0:
            return total_coins

        for i in range(coin_index, -1, -1):
            n_coins = amount // coins[i]
            while n_coins > 0:
                new_total_coins = self._greedy(
                    coins,
                    amount - coins[i] * n_coins,
                    coin_index - 1,
                    total_coins + n_coins,
                )
                if new_total_coins != -1:
                    return new_total_coins
                n_coins -= 1

        return -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        n_coins = self._dp_topdown(coins, amount, {0: 0})
        return n_coins if n_coins != inf else -1

    def _dp_topdown(self, coins: List[int], amount, dp: List):
        """
        Speed 42th, memory 14th
        """
        if amount < 0:
            return inf

        if amount in dp:
            return dp[amount]

        n_coins = []
        for coin in coins:
            n_coins.append(self._dp_topdown(coins, amount - coin, dp) + 1)

        min_coins = min(n_coins)
        dp[amount] = min_coins
        return min_coins



    def _dp_bottomup_optimized(self, coins: List[int], amount):
        """
        This version uses a simplified dynamic programming structure.
        The other adopted the two-dimensional array from the subset sum
        problem, but restricts the memory to a single array, and updates
        the amount in place as it iterates through the coins.

        This also highlights the importance of the base-case.
        This is sort of the inverse of the "grid" solution. Instead of
        a dynamic programming solution on the `ith` coin, it's a solution
        on the `ith` amount.

        Speed 55th, memory 97
        """
        dp = [inf] * (amount + 1)
        dp[0] = 0

        for j in range(1, amount + 1):
            for coin in coins:
                remaining_amount = j - coin
                if remaining_amount >= 0:
                    dp[j] = min(dp[j], dp[remaining_amount] + 1)

        return dp[amount] if dp[amount] != inf else -1

    def _dp_bottomup(self, coins: List[int], amount):
        """
        Time complexity:
            O(nk) where n == len(coins), k == amount.

        Speed 13th, memory 25th
        """
        if amount == 0:
            return 0

        # sort may not be necessary, but simplifies the implementation
        # see https://stackoverflow.com/a/45427013/6637133
        coins.sort()
        d = [[0] * (amount + 1) for _ in range(len(coins))]

        for i in range(len(coins)):
            for j in range(amount + 1):
                remaining_amount = j - coins[i]

                if j % coins[i] == 0:
                    d[i][j] = j // coins[i]

                elif i > 0 and remaining_amount >= 0 and d[i][remaining_amount] > 0:
                    last_coinage = d[i - 1][j] if d[i - 1][j] > 0 else inf
                    d[i][j] = min(d[i][remaining_amount] + 1, last_coinage)

                elif i > 0:
                    d[i][j] = d[i - 1][j]

        return d[-1][amount] if d[-1][amount] > 0 else -1

    def _dp_dividing(self, coins: List[int], amount):
        """
        Time Limit exceeded
        Time complexity:
            O(nkd) where n == len(coins), k == amount and
            d is the maximum number of times an coin divides the amount.
            Each coin `n` has to traverse each value from 0 to k + 1. Then
            on it k, it has to walk the number of times it divides `k`.

        I think depending on the divisors is making it too slow
        """
        if amount == 0:
            return 0

        coins.sort()
        d = [[0] * (amount + 1) for _ in range(len(coins))]

        for i in range(len(coins)):
            for j in range(amount + 1):
                if j % coins[i] == 0:
                    d[i][j] = j // coins[i]
                elif i > 0:
                    n_coins_i = j // coins[i]
                    n_coins_total = []
                    while n_coins_i:
                        remainder = j - coins[i] * n_coins_i
                        if remainder >= 0 and d[i - 1][remainder] > 0:
                            n_coins_total.append(n_coins_i + d[i - 1][remainder])

                        n_coins_i -= 1

                    min_coins = min(n_coins_total) if n_coins_total else d[i - 1][j]
                    d[i][j] = (
                        min(min_coins, d[i - 1][j]) if d[i - 1][j] > 0 else min_coins
                    )

        return d[-1][amount] if d[-1][amount] > 0 else -1

    def _brute_force(self, coins, amount, coin_index, total_coins, min_total_coins):
        """
        Time limit exceeded
        Call:
            if amount == 0:
                return 0

            coins.sort()
            n_coins = [inf]
            self._brute_force(coins, amount, len(coins) - 1, 0, n_coins)

            return n_coins[0] if n_coins[0] is not inf else -1
        """
        if amount == 0:
            return total_coins

        for i in range(coin_index, -1, -1):
            n_coins = amount // coins[i]
            while n_coins > 0:
                new_total_coins = self._brute_force(
                    coins,
                    amount - coins[i] * n_coins,
                    coin_index - 1,
                    total_coins + n_coins,
                    min_total_coins,
                )
                if new_total_coins != -1 and new_total_coins < min_total_coins[0]:
                    min_total_coins[0] = new_total_coins
                    return new_total_coins
                n_coins -= 1

        return -1


if __name__ == "__main__":
    cases = [
        [[1, 2, 5], 11, 3],
        [[1, 2, 3, 5], 8, 2],
        [[1, 2, 3, 5], 6, 2],
        [[2], 3, -1],
        [[1], 0, 0],
        [[1], 1, 1],
        [[1], 2, 2],
        [[2, 3, 9], 10, 4],
        [[2, 3, 9], 14, 3],
        [[2, 5, 10, 1], 27, 4],
        [[186, 419, 83, 408], 6249, 20],
        [[13, 9, 3, 1], 21, 3],
        [[388, 232, 419, 338, 49, 434, 4, 143], 4993, 13],
    ]

    s = Solution()
    for coins, amount, ans in cases:
        # print method when s.coinChange returns `d` from s._dp
        # for row in s.coinChange(coins, amount):
        #     for v in row:
        #         print(f'{v:>3}', end="")
        #     print()
        print(f"{s.coinChange(coins, amount):>2} {ans:>2}")
