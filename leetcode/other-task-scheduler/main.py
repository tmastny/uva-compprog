from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        return 0


cases = [
    (["A", "A", "A", "B", "B", "B"], 2, 8),
    (["A", "A", "A", "B", "B", "B"], 0, 6),
    (["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2, 16),
]

if __name__ == "__main__":
    for tasks, n, ans in cases:
        s = Solution()
        output = s.leastInterval(tasks, n)

        if output != ans:
            print(f"{tasks}, {n}, {output}: {ans}")
