# Example:
#   preorder       inorder         output
#   [3,9,20,15,7]  [9,3,15,20,7]   [3,9,20,null,null,15,7]

# See the pre and in order print methods for the definition.
# Preorder does NOT correspond to a breadth-first search.
# In fact, they are all a special case of a depth-first search.

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _build(self, preorder, pi, inorder):
        """
        Improvements:
          1. build a hash map of the root to the index of the array
             so the left/right split can be found in constant time,
             instead of a linear search (which makes the algo O(n^2)
             instead of O(n)).

          2. use indices instead of slices
        """
        if not inorder:
            return None

        root = TreeNode(preorder[pi[0]])
        ri = inorder.index(root.val)

        pi[0] += 1
        root.left = self._build(preorder, pi, inorder[:ri])
        root.right = self._build(preorder, pi, inorder[ri + 1 :])

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        val_to_inorder_index = {val: i for i, val in enumerate(inorder)}

        def build(pi, loi, roi):
            if pi[0] >= len(preorder) or roi - loi <= 0:
                return None

            node = TreeNode(preorder[pi[0]])
            ni = val_to_inorder_index[node.val]

            pi[0] += 1
            node.left = build(pi, loi, ni)
            node.right = build(pi, ni + 1, roi)

            return node

        return build([0], 0, len(inorder))


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
