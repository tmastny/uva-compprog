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
    def _sort(self, nums, k):
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        counts = [(v, k) for k, v in freq.items()]
        counts.sort()

        return [k for _, k in reversed(counts[-k:])]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        counts = [(v, k) for k, v in freq.items()]
        quickselect(counts, len(counts) - k)

        return [k for _, k in reversed(counts[-k:])]



def partition(n, lo, hi, pivot):
    pivot = n[pivot]
    pleft = pright = lo

    while pright <= hi:
        if n[pright] < pivot:
            n[pleft], n[pright] = n[pright], n[pleft]
            pleft += 1
            pright += 1

        elif n[pright] > pivot:
            n[pright], n[hi] = n[hi], n[pright]
            hi -= 1

        else:
            pright += 1

    return pleft, pright


def quickselect(n, k):
    def _quickselect_r(n, k, lo, hi):
        if lo >= hi:
            return

        left, right = partition(n, lo, hi, randint(lo, hi))

        if k < pivot:
            _quickselect_r(n, k, lo, left - 1)
        elif k > pivot:
            _quickselect_r(n, k, right + 1, hi)

    return _quickselect_r(n, k, 0, len(n) - 1)


if __name__ == "__main__":
    partition_tests = [
        [[6, 5, 10, 3, 0, 4, 9], 2],
        [[6, 5, 10, 3, 11, 4, 9], 2],
        [[0, 1, 10, 3, 7, 5, 6], 3],
        [[0, 1, 10, 3, 7, 5, 6], 6],
        [[5,1,6,2,4,1,1,1,7,6,9], 0],
        [[5,1,6,2,4,1,1,1,7,6,9], 1]
    ]

    print("Partition Tests")
    for n, pivot in partition_tests:
        partition(n, 0, len(n) - 1, pivot)
        print(n)

    qtests = [
        [[6, 5, 10, 3, 0, 4, 9], 2],
        [[6, 5, 10, 3, 11, 4, 9], 2],
        [[0, 1, 10, 3, 7, 5, 6], 3],
        [[0, 1, 10, 3, 7, 5, 6], 6],
    ]

    print()
    print("Quick Select")
    print([0,1,2,3,4,5,6,7])
    for n, _ in qtests:
        quickselect(n, 3)
        print(n)

    print()
    print("Top K")
    cases = [
        [[1, 1, 1, 2, 2, 3], 2],
        [[1], 1],
        [[3, 0, 1, 0], 1]
    ]

    s = Solution()
    for nums, k in cases:
        print(s.topKFrequent(nums, k))
