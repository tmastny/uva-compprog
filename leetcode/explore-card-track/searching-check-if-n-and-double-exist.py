from typing import List


class Solution1:
    def checkIfExist(self, arr: List[int]) -> bool:
        elems = {n: i for i, n in enumerate(arr)}

        for i, n in enumerate(arr):
            if n * 2 in elems and elems[n * 2] != i:
                return True

        return False

# it's easier if you do it in one step. That why
# you don't have the check the indices (and you can)
# check half value
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        map = set()

        for n in arr:
            if n * 2 in map or (n % 2 == 0 and n // 2 in map):
                return True
            map.add(n)

        return False

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
