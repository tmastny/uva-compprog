from typing import List


# runtime: 35%
class SolutionMultiPass:
    def removeElement(self, nums: List[int], val: int) -> int:
        end = len(nums) - 1
        n_val = nums.count(val)
        k = len(nums) - n_val

        for i in range(len(nums)):
            if i >= k:
                break

            if nums[i] == val:
                while nums[end] == val:
                    end -= 1

                nums[i], nums[end] = nums[end], nums[i]

        return k


# single-pass, runtime: 50%
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n_nonval = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[n_nonval] = nums[i]
                n_nonval += 1

        return n_nonval


cases = [
    ([3, 2, 2, 3], 3, 2, [2, 2, 0, 0]),
    ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 1, 4, 0, 3, 0, 0, 0]),
]

if __name__ == "__main__":
    for nums, val, k, ans in cases:
        orig = nums.copy()

        s = Solution()
        s.removeElement(nums, val)

        if nums != ans:
            print(f"{orig}, {val} -> {nums}: {ans}")
