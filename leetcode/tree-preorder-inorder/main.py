# Example:
#   Input                    Output
#   [3,9,20,null,null,15,7]  [[3],[20,9],[15,7]]

# Looks like a kinda of breadth first search
import queue
from typing import List
from collections import deque


class TreeNode:
    @classmethod
    def _add_to_list(cls, ls, i):
        if i >= len(ls) or ls[i] is None:
            return None

        node = cls(ls[i])
        node.left = cls._add_to_list(ls, i * 2 + 1)
        node.right = cls._add_to_list(ls, i * 2 + 2)

        return node

    @classmethod
    def from_list(cls, ls):
        """
        [0, 1, 2, 3, 4, 5, 6, 7]
            0          1
          1   2      2   3
         3 4 5 6    4 5 6 7
        l(0) = 1    l(1) = 3   l(2) = 5   l(i) = i * 2 + 1
        r(0) = 2    r(1) = 4   r(2) = 6   r(i) = i * 2 + 2
        """

        return cls._add_to_list(ls, 0)

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return TreeNode()


if __name__ == "__main__":
    cases = [[[3, 9, 20, 15, 7], [9, 3, 15, 20, 7]], [[-1], [-1]]]

    s = Solution()
    for preorder, inorder in cases:
        print(s.buildTree(preorder, inorder))
