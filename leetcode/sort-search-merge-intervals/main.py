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


class VK:
    def __init__(self, v, k) -> None:
        self.v = v
        self.k = k

    def __lt__(self, other):
        return self.v < other.v

    def __repr__(self) -> str:
        return f'({self.v}, {self.k})'


class Solution:
    def _sort(self, nums, k):
        """
        Time: O(n log n), memory O(n)

        Despite worse time complexity, this algorithm is substantially faster.
        Possibly because the built-in sort method is optimized.

        Time: 51, memory 31
        """
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        counts = [(v, k) for k, v in freq.items()]
        counts.sort()

        return [k for _, k in reversed(counts[-k:])]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Time: O(n), memory: O(n)

        Frequency of each unique element is stored in a dictionary at O(n) time
        and O(n) memory. The frequency of each element is converted to a list.

        Then Quickselect is ran on the frequencies to find the top k at O(n) time.
        Lastly, the elements associated with those frequencies are returned.

        Time: 26, memory 15
        """
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        counts = [VK(v, k) for k, v in freq.items()]
        quickselect(counts, len(counts) - k)

        return [vk.k for vk in reversed(counts[-k:])]


def partition(n, lo, hi, pivot_index):
    """
    See: https://en.wikipedia.org/wiki/Dutch_national_flag_problem
    if current value (pright) is smaller than pivot, slide the
    pivot window to the right. For example: pivot = 6
        0 3 2 6 6 3 8 1 0 2
            ^ ^ ^
            ^ ^
        0 3 2 3 6 6 8 1 0 2
                ^   ^
                ^   ^

    if current value is larger than pivot, put at the end of array
    """
    pivot = n[pivot_index]
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

        if k < left:
            _quickselect_r(n, k, lo, left - 1)
        elif k > right:
            _quickselect_r(n, k, right, hi)

    return _quickselect_r(n, k, 0, len(n) - 1)


if __name__ == "__main__":
    partition_tests = [
        [[6, 5, 10, 3, 0, 4, 9], 2],
        [[6, 5, 10, 3, 11, 4, 9], 2],
        [[0, 1, 10, 3, 7, 5, 6], 3],
        [[0, 1, 10, 3, 7, 5, 6], 6],
        [[5, 1, 6, 2, 4, 1, 1, 1, 7, 6, 9], 0],
        [[5, 1, 6, 2, 4, 1, 1, 1, 7, 6, 9], 1],
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
    print([0, 1, 2, 3, 4, 5, 6, 7])
    for n, _ in qtests:
        quickselect(n, 3)
        print(n)

    print()
    print("Top K")
    cases = [
        [[1, 1, 1, 2, 2, 3], 2],
        [[1], 1],
        [[3, 0, 1, 0], 1],
        [[5, 2, 5, 3, 5, 3, 1, 1, 3], 2],
    ]

    s = Solution()
    for nums, k in cases:
        print(s.topKFrequent(nums, k))
