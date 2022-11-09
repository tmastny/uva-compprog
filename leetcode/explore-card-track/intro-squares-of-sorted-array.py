from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:


        return []

cases = [
    ([-4,-1,0,3,10], [0,1,9,16,100]),
    ([-7,-3,2,3,11], [4,9,9,49,121]),
    ([0], [0]),
]

if __name__ == "__main__":
    for nums, ans in cases:
        s = Solution()
        output = s.findNumbers(nums)

        if output != ans:
            print(f"{nums}, {output}: {ans}")
