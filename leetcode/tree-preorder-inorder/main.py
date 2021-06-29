# Example:
#   preorder       inorder         output
#   [3,9,20,15,7]  [9,3,15,20,7]   [3,9,20,null,null,15,7]

# Preorder corresponds to a breadth-first search, and iorder
# is a depth-first search.

from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder or not preorder:
            return None

        node = TreeNode(preorder[0])

        node_index = inorder.index(preorder[0])

        node.left = self.buildTree(preorder[1:], inorder[0:node_index])
        node.right = self.buildTree(preorder[2:], inorder[node_index:])

        return node


def print_inorder(node):
    if node is None:
        return

    print_inorder(node.left)
    print(node.val, end="")
    print_inorder(node.right)


def print_bfs(node):
    queue = deque([node])
    while queue:
        size = len(queue)
        for _ in range(size):
            node = queue.pop()
            if node is None:
                continue

            print(node.val, end=",")
            queue.appendleft(node.left)
            queue.appendleft(node.right)


if __name__ == "__main__":
    cases = [
        [[1, 2], [1, 2]],
        [[1, 2], [2, 1]],
        [[3, 9, 20, 15, 7], [9, 3, 15, 20, 7]],
        [[-1], [-1]],
        [[1, 2, 3], [2, 1, 3]],
    ]

    s = Solution()
    for preorder, inorder in cases:
        node = s.buildTree(preorder, inorder)
        print_inorder(node)
        print()
        print_bfs(node)
