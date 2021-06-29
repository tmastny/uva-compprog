# Example:
#   preorder       inorder         output
#   [3,9,20,15,7]  [9,3,15,20,7]   [3,9,20,null,null,15,7]

# See the pre and in order print methods for the definition.
# Preorder does NOT correspond to a breadth-first search.

from typing import List
from collections import deque


def val_is_left_of(val, root, array):
    return True


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _build(self, preorder, pi, inorder):
        if not inorder:
            return None

        root = TreeNode(preorder[pi[0]])
        ri = inorder.index(root.val)

        pi[0] += 1
        root.left = self._build(preorder, pi, inorder[:ri])
        root.right = self._build(preorder, pi, inorder[ri + 1 :])

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self._build(preorder, [0], inorder)


def print_inorder(node):
    if node is None:
        return

    print_inorder(node.left)
    print(node.val, end=",")
    print_inorder(node.right)


def print_preorder(node):
    if node is None:
        return

    print(node.val, end=",")
    print_preorder(node.left)
    print_preorder(node.right)


if __name__ == "__main__":
    cases = [
        [[3, 1, 2, 4], [1, 2, 3, 4]],
        [[1, 2], [1, 2]],
        [[1, 2], [2, 1]],
        [[3, 9, 20, 15, 7], [9, 3, 15, 20, 7]],
        [[-1], [-1]],
        [[1, 2, 3], [2, 1, 3]],
    ]

    s = Solution()
    for preorder, inorder in cases:
        node = s.buildTree(preorder, inorder)
        print_preorder(node)
        print()
        print_inorder(node)
        print("\n")
