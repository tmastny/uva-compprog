from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        evens = 0
        for n in nums:
            digits = 1
            n //= 10
            while n:
                digits += 1
                n //= 10

            if digits % 2 == 0:
                evens += 1

        return evens


cases = [
    ([12, 345, 2, 6, 7896], 2),
    ([555, 901, 482, 1771], 1),
    ([0], 0),
]

if __name__ == "__main__":
    for nums, ans in cases:
        s = Solution()
        output = s.findNumbers(nums)

        if output != ans:
            print(f"{nums}, {output}: {ans}")
