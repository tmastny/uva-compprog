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
    def _make_num(self, node: ListNode):
        if node.next is None:
            return node.val

        num = 0
        if node.val == 0:
            num = 10
            node = node.next

        while node is not None:
            num = num * 10 + node.val
            node = node.next

        return self._reverse_num(num)

    def _reverse_num(self, num):
        rnum = 0

        last_num = num
        while num >= 0 and last_num >= 10:
            rnum = rnum * 10 + (num % 10)

            last_num = num
            num //= 10

        return rnum

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum = self._make_num(l1) + self._make_num(l2)
        print(f"sum: {self._make_num(l1)} + {self._make_num(l2)} = {sum}")

        head = ListNode()
        node = head

        last_sum = sum
        while sum >= 0 and last_sum >= 10:
            node.val = sum % 10
            last_sum = sum
            sum //= 10

            if sum != 0:
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
