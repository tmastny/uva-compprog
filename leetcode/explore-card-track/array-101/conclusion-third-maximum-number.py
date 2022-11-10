from typing import List
from math import inf

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        threes = []

        for n in nums:
            if n in threes:
                continue

            if len(threes) < 3:
                threes.append(n)
                continue

            bot, top = inf, -inf
            for t in threes:
                if t > top:
                    top = t
                elif t < bot:
                    bot = t

            # [1,2,5] | 3
            if n > bot:
                threes.remove(bot)
                threes.append(n)
        
        if len(threes) < 3:
            return max(threes)

        return min(threes)



cases = [
    ([1,2,2,5,3,5], 2),
    ([3,2,1], 1),
    ([10, 20, 30, 25], 10),
    ([1,2], 2),
    ([2,2,3,1], 1)
]

if __name__ == "__main__":
    for nums, ans in cases:
    
        s = Solution()
        out = s.thirdMax(nums)

        if out != ans:
            print(f"{nums}, {out}: {ans}")
