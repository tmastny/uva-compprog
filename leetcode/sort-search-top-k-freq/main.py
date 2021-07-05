from typing import List
from collections import defaultdict

# Time: O(n log n), memory: O(n)
#   Count the frequency of elements with a dictionary.
#   Sort the values of the dictionary, and return the top
#   elements (keys).

# Time: O(n), memory: O(n)
#   Count the frequency of elements with a dictionary.
#   Track the element with the minimum frequency. If
#   len(dictionary) == k, the next element either
#   replaces the minimum or is not kept in the dictionary.


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        topk = set()
        min_freq = ()  # key, value

        for n in nums:
            freq[n] += 1

            # min_freq doesn't work. If I could another occurence
            # of the min_freq element, it might not be min_freq
            # anymore, and another from `topk` would be the new minimum.
            if len(topk) < k:
                topk.add(n)
                if not min_freq or freq[n] < min_freq[1]:
                    min_freq = (n, freq[n])

            elif freq[n] > min_freq[1]:
                topk.remove(min_freq[0])
                topk.add(n)
                min_freq = (n, freq[n])

        return list(topk)


if __name__ == "__main__":
    cases = [
        # [[1, 1, 1, 2, 2, 3], 2],
        # [[1], 1],
        [[3, 0, 1, 0], 1]
    ]

    s = Solution()
    for nums, k in cases:
        print(s.topKFrequent(nums, k))
