from typing import List

# See also: binary subsets: https://www.keithschwarz.com/binary-subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self._subsets_i(nums)

    def _subsets_i(self, nums):
        """
        Cascading solution: for each new element, append it to the
        subsets of the previous elements.

        Speed 81, memory 77
        """
        power_set = [[]]
        for n in nums:
            power_set += [subset + [n] for subset in power_set]

        return power_set


    def _subsets_r(self, nums: List[int]) -> List[List[int]]:
        """
        The key different between subsets and permutations is that
        order does not matter.

        If we wanted all the permutations of all subsets, we could
        reuse the same permutation code, but append to the list
        at every node instead of every leaf.

        Speed: 81th percentile, memory 92th
        """
        power_set = []

        def find_subsets(prefix, start):
            power_set.append(list(prefix))

            for i in range(start, len(nums)):
                prefix.append(nums[i])
                find_subsets(prefix, i + 1)
                prefix.pop()

        find_subsets([], 0)

        return power_set

if __name__ == "__main__":
    cases = [[1, 2, 3], [0, 1], [1]]

    s = Solution()
    for n in cases:
        print(s.subsets(n))
