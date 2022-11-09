from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self._permute_without_set(nums)

    def _permute_without_set(self, nums):
        """
        The efficiency of set here is overrated. Because
        the number of permutations grows at O(n!), there will
        never be more than even 50 elements, so a linear search
        is sufficient.

        Speed: 88th percentile, memory 88th percentile
        """
        permutations = []

        def find_permutations(prefix: List[int]):
            if len(prefix) == len(nums):
                permutations.append(list(prefix))

            for n in nums:
                if n not in prefix:
                    prefix.append(n)
                    find_permutations(prefix)

                    prefix.pop()

        find_permutations([])

        return permutations

    def _ref_permute(self, nums):
        """
        More memory efficient version that relies on modifying
        data structures and passing by reference instead of copying
        them. Not sure how to do it with `nums`, because modifying
        the iterator returns unexpected results.

        Turns out to be much faster, but just as memory intensive.

        Speed: 88th percentile, memory 0th percentile
        """
        nums = set(nums)
        permutations = []

        def find_permutations(prefix: List[int], nums: set[int]):
            if not nums:
                permutations.append(list(prefix))

            for n in nums:
                prefix.append(n)
                find_permutations(prefix, nums - {n})

                prefix.pop()

        find_permutations([], nums)

        return permutations

    def _copy_permute(self, nums):
        """
        This solution is more difficult in terms of memory than other
        leetcode problems, because there is no immediately obvious way
        to use indicies rather than copying and creating new lists and
        sets on each recrusion.

        Is there a way to improve memory usage? The tricky part is that
        the recursion step needs to eliminate `n`, but remember the current
        state of prefix and nums for the next `n`.

        Speed: 69th percentile, memory 0th percentile
        """
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
