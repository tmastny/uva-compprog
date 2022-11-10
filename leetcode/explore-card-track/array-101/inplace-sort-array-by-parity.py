from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evens = 0
        for i, n in enumerate(nums):
            if n % 2 == 0:
                nums[i], nums[evens] = nums[evens], nums[i]
                evens += 1

        return nums


cases = [
    ([3,1,2,4], [2,4,3,1]),
    ([0], [0])
]

if __name__ == "__main__":
    for nums, ans in cases:

        s = Solution()
        out = s.sortArrayByParity(nums)

        if out != ans:
            print(f"{nums}, {out}: {ans}")
