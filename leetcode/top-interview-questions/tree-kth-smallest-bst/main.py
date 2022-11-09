class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
        return cls._add_to_list(ls, 0)


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        kth = [0, 0]

        def kth_smallest(kth, node):
            if node is None or kth[0] == k:
                return

            kth_smallest(kth, node.left)

            if kth[0] == k:
                return

            kth[0] += 1
            kth[1] = node.val

            if kth[0] == k:
                return

            kth_smallest(kth, node.right)

        kth_smallest(kth, root)

        return kth[1]


def print_inorder(node):
    if node is None:
        return

    print_inorder(node.left)

    print(node.val, end=",")

    print_inorder(node.right)


if __name__ == "__main__":
    cases = [([3, 1, 4, None, 2], 1), ([5, 3, 6, 2, 4, None, None, 1], 3)]

    s = Solution()
    for tree, k in cases:
        root = TreeNode.from_list(tree)
        print_inorder(root)
        print()
        print(s.kthSmallest(root, k))
