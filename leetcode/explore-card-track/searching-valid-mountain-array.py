from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        return True


cases = [
    ([-2, 0, 10, -19, 4, 6, -8], False),
    ([0, 0], True),
    ([10, 2, 5, 3], True),
    ([3, 1, 7, 11], False),
]

if __name__ == "__main__":
    for nums, ans in cases:
        orig = nums.copy()

        s = Solution()
        out = s.checkIfExist(nums)

        if out != ans:
            print(f"{nums}, {out}: {ans}")
