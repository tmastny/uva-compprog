from typing import List
from collections import deque


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        pos = deque()
        neg = deque()
        for n in nums:
            if n < 0:
                neg.appendleft(n**2)
            else:
                pos.append(n**2)

        sqs = []
        while neg and pos:
            if neg[0] > pos[0]:
                sqs.append(pos.popleft())
            else:
                sqs.append(neg.popleft())

        remaining = neg if neg else pos

        return sqs + list(remaining)


cases = [
    ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
    ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
    ([0], [0]),
]

if __name__ == "__main__":
    for nums, ans in cases:
        s = Solution()
        output = s.sortedSquares(nums)

        if output != ans:
            print(f"{nums}, {output}: {ans}")
