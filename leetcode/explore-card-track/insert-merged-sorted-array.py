from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1, i2 = m - 1, n - 1
        j = m + n - 1

        while i1 >= 0 and i2 >= 0:
            if nums1[i1] > nums2[i2]:
                nums1[j] = nums1[i1]
                i1 -= 1
            else:
                nums1[j] = nums2[i2]
                i2 -= 1

            j -= 1

        if i2 < 0:
            return

        while i2 >= 0:
            nums1[j] = nums2[i2]
            j -= 1
            i2 -= 1


cases = [
    ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
    ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6]),
    ([1], 1, [], 0, [1]),
    ([0], 0, [1], 1, [1]),
]

if __name__ == "__main__":
    for nums1, m, nums2, n, ans in cases:
        orig = nums1.copy()

        s = Solution()
        s.merge(nums1, m, nums2, n)

        if nums1 != ans:
            print(f"{orig}, {nums1}: {ans}")
