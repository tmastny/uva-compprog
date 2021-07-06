from typing import List
from collections import defaultdict
from random import randint

# Time: O(n log n), memory: O(n)
#   Count the frequency of elements with a dictionary.
#   Sort the values of the dictionary, and return the top
#   elements (keys).

# Time: O(n), memory: O(n)
#   Count the frequency of elements with a dictionary.
#   Track the element with the minimum frequency. If
#   len(dictionary) == k, the next element either
#   replaces the minimum or is not kept in the dictionary.
#   This doesn't work:
#       min_freq doesn't work. If I could another occurence
#       of the min_freq element, it might not be min_freq
#       anymore, and another from `topk` would be the new minimum.


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        counts = [(v, k) for k, v in freq.items()]
        quickselect(counts, len(nums) - k)

        return []


def partition(n, lo, hi, pivot):
    i = lo
    while i <= hi:
        # pivot index points to the first value of occurence of element
        if i < pivot and n[i] >= n[pivot]:
            n[i], n[pivot - 1] = n[pivot - 1], n[i]
            n[pivot], n[pivot - 1] = n[pivot - 1], n[pivot]
            pivot -= 1

        elif i > pivot and n[i] < n[pivot]:
            n[i], n[pivot + 1] = n[pivot + 1], n[i]
            n[pivot], n[pivot + 1] = n[pivot + 1], n[pivot]
            pivot += 1

        else:
            i += 1

    return pivot


def quickselect(n, k):
    def _quickselect_r(n, k, lo, hi):
        pivot = partition(n, lo, hi, randint(lo, hi))

        if k < pivot:
            _quickselect_r(n, k, lo, pivot)
        elif k > pivot:
            _quickselect_r(n, k, pivot, hi)

    return _quickselect_r(n, k, 0, len(n) - 1)


if __name__ == "__main__":
    partition_tests = [
        [[6, 5, 10, 3, 0, 4, 9], 2],
        [[6, 5, 10, 3, 11, 4, 9], 2],
        [[0, 1, 10, 3, 7, 5, 6], 3],
        [[0, 1, 10, 3, 7, 5, 6], 6],
    ]

    print("Partition Tests")
    for n, pivot in partition_tests:
        partition(n, 0, len(n) - 1, pivot)
        print(n)

    # cases = [
    #     # [[1, 1, 1, 2, 2, 3], 2],
    #     # [[1], 1],
    #     [[3, 0, 1, 0], 1]
    # ]

    # print("Leetcode Problem")
    # s = Solution()
    # for nums, k in cases:
    #     print(s.topKFrequent(nums, k))
