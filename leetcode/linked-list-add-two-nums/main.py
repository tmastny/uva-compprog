# Example 1:
#     List            Number
#     l1 = [2,4,3]    342
#     l2 = [5,6,4]    465
# output = [7,0,8]    807


from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        return l1

def make_node(lst):
    head = ListNode()
    node = head
    for i, val in enumerate(lst):
        node.val = val
        if i + 1 < len(lst):
            node.next = ListNode()
            node = node.next

    return head


def print_node(head):
    node = head
    while node is not None:
        print(node.val)
        node = node.next


if __name__ == "__main__":
    cases = [
        [[2,4,3], [5,6,4], [7,0,8]],
    ]
    cases = [list(map(make_node, case)) for case in cases]

    s = Solution()

    for l1, l2, ans in cases:
        node = s.addTwoNumbers(l1, l2)
        print_node(node)
