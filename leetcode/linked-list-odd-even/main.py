# Examples:
#     List             Output
#     [1,2,3,4,5]      [1,3,5,2,4]
#     [2,1,3,5,6,4,7]  [2,3,6,7,1,5,4]

# Diagram:
#   i    0[1,2,3,4,5]
#   0    e o
#   1      e o
#   i    0[1,2,3,4,5]
#   1    ^   ^
#          ^   ^
#            ^   ^
#              ^   ^
#   5            ^   ^ <- lead is None, but lag is 4. Then lag.next = evenhead
#                         doesn't work. Need to use last

#   i    0[1,2,3,4]
#   1    ^   ^
#          ^   ^
#            ^   ^
#   4          ^   ^ <- lag ends on last odd, lead is None

#   i  0 0[1,2,3,4,5]
#      ^   ^
#        ^   ^
#          ^   ^
#            ^   ^     while lead.next: // true lead = lead.next; lag = next_lag
#              ^   ^


# Note:
#   The relative order inside
#   both the even and odd groups should
#   remain as it was in the input.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next

# 1 2 3 4
# ^ ^
#   ^ ^
#     ^ ^ <- even.next is None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        evenhead = head.next

        odd = head
        even = head.next

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = even.next.next
            even = even.next

        odd.next = evenhead

        return head


def make_node(lst):
    head = ListNode()
    node = head
    for val in lst:
        node.next = ListNode()
        node = node.next
        node.val = val

    return head.next


def print_node(head):
    node = head
    while node is not None:
        print(node.val, end=",")
        node = node.next
    print()


if __name__ == "__main__":
    cases = [
        [[1, 2, 3, 4], [1, 3, 2, 4]],
        [[1, 2, 3, 4, 5], [1, 3, 5, 2, 4]],
        [[2, 1, 3, 5, 6, 4, 7], [2, 3, 6, 7, 1, 5, 4]],
    ]
    cases = [list(map(make_node, case)) for case in cases]

    s = Solution()

    for l, ans in cases:
        node = s.oddEvenList(l)
        print_node(node)
