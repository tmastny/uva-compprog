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


# Option 1: git hash 55cc931
#   convert to number using first as msd, then reverse the
#   digit, sum, and return a list of that number.
#   The problem is that there is some complexity getting
#   the conversion right.

# Option 2:
#   implement ripple-carry adder for these linked lists

class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        node = head
        carry = 0

        while l1 is not None or l2 is not None or carry:
            val1 = 0 if l1 is None else l1.val
            val2 = 0 if l2 is None else l2.val

            sum = val1 + val2 + carry
            node.val = sum % 10
            carry = sum // 10

            l1 = None if l1 is None else l1.next
            l1 = None if l2 is None else l2.next

            if l1 or l2 or carry:
                node.next = ListNode()
                node = node.next

        return head


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
        print(node.val, end=",")
        node = node.next
    print()


if __name__ == "__main__":
    cases = [
        # [[2, 4, 3], [5, 6, 4], [7, 0, 8]],
        # [[0], [0], [0]],
        # [[9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], []],
        [[0, 8, 6, 5, 6, 8, 3, 5, 7], [6, 7, 8, 0, 8, 5, 8, 9, 7], []],
    ]
    cases = [list(map(make_node, case)) for case in cases]

    s = Solution()

    for l1, l2, ans in cases:
        node = s.addTwoNumbers(l1, l2)
        print_node(node)
