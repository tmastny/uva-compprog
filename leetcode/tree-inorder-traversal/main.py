# Example:
#   Tree Array      Output
#   [1,null,2,3]    [1,3,2]   <- shouldn't the input be [1,null,2,null,null,3]
#         1
#           2
#         3

from typing import List


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
    def _recursive_traversal(self, node: TreeNode, vals: List[int]):
        if not node:
            return

        self._recursive_traversal(node.left, vals)

        vals.append(node.val)

        self._recursive_traversal(node.right, vals)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        vals = []
        self._recursive_traversal(root, vals)

        return vals

    def _add_to_leftstack(self, node, stack):
        while node:
            stack.append(node)
            node = node.left

        stack.append(node)

    def _iterative_traversal(self, root: TreeNode) -> List[int]:
        vals = []
        leftstack = []
        self._add_to_leftstack(root, leftstack)

        while leftstack:
            node = leftstack.pop()
            if node is None:
                continue

            vals.append(node.val)
            self._add_to_leftstack(node.right, leftstack)

        return vals

    def _clean_iterative(self, root: TreeNode):
        # the trick here is to pop after the left search.
        # I was always trying to pop before the left search, which made it
        # much more complicated.
        vals = []
        stack = []
        node = root
        while node and len(stack):
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            vals.append(node.val)

            node = node.right

        return vals

    def _morris(self, root: TreeNode) -> List[int]:
        """
        Morris traversal is an inorder traversal algorithm that is done
        in O(n) time and O(1) memory, compared to the O(n) memory of other
        solutions.

        The key idea is that the predecessor to the current node
        (root for example) makes the current node it's right child.
        """
        vals = []
        node = root
        while node:
            if node.left is None:
                vals.append(node.val)
                node = node.right
            else:
                predecessor = node.left
                while predecessor.right and predecessor.right != node:
                    predecessor = predecessor.right

                if predecessor.right == node:
                    predecessor.right = None
                    vals.append(node.val)
                    node = node.right
                else:
                    predecessor.right = node
                    node = node.left

        return vals


if __name__ == "__main__":
    cases = [
        [1, None, 2, None, None, 3],
        [],
        [1],
        [1, 2],
        [1, None, 2],
        [0, 1, 2, 3, 4, 5, 6],
    ]
    cases = [TreeNode.from_list(case) for case in cases]

    s = Solution()
    for case in cases:
        print(s._morris(case))
