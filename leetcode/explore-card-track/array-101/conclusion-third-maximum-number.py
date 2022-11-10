from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        threes = []

        for n in nums:
            if len(threes) < 3 and n not in threes:
                threes.append(n)
                continue

            next_loop = False
            top = threes[0]
            for t in threes:
                if n == t:
                    next_loop = True
                    break
                
                if n > top:
                    top = n

            if next_loop:
                continue
            
            if n > top:
                threes.remove(min)
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
