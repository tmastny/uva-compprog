from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right = [-1]
        greatest = -1
        for i in range(len(arr) - 1, 0, -1):
            if arr[i] > greatest:
                greatest = arr[i]

            right.append(greatest)

        right.reverse()

        return right


cases = [([17, 18, 5, 4, 6, 1], [18, 6, 6, 6, 1, -1]), ([400], [-1])]

if __name__ == "__main__":
    for nums, ans in cases:
        orig = nums.copy()

        s = Solution()
        out = s.replaceElements(nums)

        if out != ans:
            print(f"{nums}, {out}: {ans}")
