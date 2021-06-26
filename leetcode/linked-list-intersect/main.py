# Examples:
# Input                        Output
# [4,1,8,4,5], [5,6,1,8,4,5]   [8,4,5]

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        return headA


def make_node(lst):
    head = ListNode(0)
    node = head
    for val in lst:
        node.next = ListNode(0)
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
        [[4,1,8,4,5], [5,6,1,8,4,5]],
    ]
    cases = [list(map(make_node, case)) for case in cases]

    s = Solution()

    for l1, l2 in cases:
        node = s.getIntersectionNode(l1, l2)
        print_node(node)
