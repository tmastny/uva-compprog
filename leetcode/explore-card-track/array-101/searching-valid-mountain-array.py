from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 or arr[0] > arr[1]:
            return False

        descending = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                descending = True

            if arr[i] == arr[i + 1]:
                return False
            elif descending and arr[i] < arr[i + 1]:
                return False

        return True if descending else False


cases = [
    ([1, 2, 3, 4], False),
    ([0, 1, 2, 3, 2, 3, 0], False),
    ([0, 2, 3, 3, 5, 2, 1, 0], False),
    ([2, 1], False),
    ([3, 5, 5], False),
    ([0, 3, 2, 1], True),
]

if __name__ == "__main__":
    for nums, ans in cases:
        orig = nums.copy()

        s = Solution()
        out = s.validMountainArray(nums)

        if out != ans:
            print(f"{nums}, {out}: {ans}")
