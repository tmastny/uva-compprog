from collections import deque


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

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
    def connect(self, root: "Node") -> "Node":
        if not root:
            return root

        queue = deque([root])

        while queue:

            level = len(queue)
            for i in range(level):
                node = queue.pop()

                if i + 1 < level:
                    node.next = queue[-1]

                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.right)

        return root


def print_next_inorder(node):
    if node is None:
        return

    print_next_inorder(node.left)

    next = node.next.val if node.next else " "
    print("{}     {}".format(node.val, next))

    print_next_inorder(node.right)


if __name__ == "__main__":
    cases = [[1, 2, 3, 4, 5, 6, 7]]

    s = Solution()
    for case in cases:
        root = s.connect(Node.from_list(case))
        print("node  next")
        print_next_inorder(root)
