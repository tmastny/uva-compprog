from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pass


if __name__ == "__main__":
    cases = [[[1, 1, 1, 2, 2, 3], 2], [[1], 1]]

    s = Solution()
    for nums, k in cases:
        print(s.topKFrequent(nums, k))
