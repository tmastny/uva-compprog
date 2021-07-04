from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums = set(nums)
        permutations = []

        def find_permutations(prefix, nums):
            if not nums:
                permutations.append(prefix)

            for n in nums:
                find_permutations(prefix + [n], nums - {n})

        find_permutations([], nums)

        return permutations


if __name__ == "__main__":
    cases = [[1, 2, 3], [0, 1], [1]]

    s = Solution()
    for n in cases:
        print(s.permute(n))
