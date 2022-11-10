from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        non_dup_idx = 0
        for n in nums:
            if n != nums[non_dup_idx]:
                non_dup_idx += 1
                nums[non_dup_idx] = n

        return non_dup_idx + 1


cases = [
    ([1, 1, 2], 2, [1, 2, 0]),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4, 0, 0, 0, 0, 0]),
    ([0, 1, 1, 1, 1], 2, [0, 1, 0, 0, 0]),
    ([0, 1, 1, 1, 2], 3, [0, 1, 2, 0, 0]),
]

if __name__ == "__main__":
    for nums, ans1, ans2 in cases:
        orig = nums.copy()

        s = Solution()
        out = s.removeDuplicates(nums)

        if nums != ans2:
            print(f"{orig}: -> {nums}, {out}: {ans1}, {ans2}")
