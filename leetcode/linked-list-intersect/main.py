# Examples:
# Input                        Output
# [4,1,8,4,5], [5,6,1,8,4,5]   [8,4,5]

# [4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5]   [8, 4, 5]
#  4  5 13 17 22    5 11 12 20 24 29     8 12 17
# 18 17  9  5  0   24 18 17  9  5  0

# 29 - 22 = 7 <- no, this doesn't work: we aren't checking
#                the values (1 is a false positive), but pointers


# Note:
#   The intersection is *not* the point at which the remaining
#   values are equal: then the output of example 1 would be
#   [1, 8, 4, 5]. Rather, at some point, the two lists
#   point at the *same list in memory*, which in this case
#   starts at 8.

# Brute force: O(n^2)
#   Go to the end and check if the last values are the same
#   node. If no, there is not intersection. Else, loop
#   through until the second to last element. Continue
#   until you reach the elements aren't shared. Then the
#   previous one is the start of the intersection.

# Binary search: O(nlog n)
#   Seek ahead in the list by powers of two. Eventually
#   you will find an intersection (or not).
#   Then seek half way between the powers of two until
#   you find the intersection point.

# Loop detection: O(n)
#   Connect the head and tail of list A. Then if the lists intersect,
#   list B is a list with a cycle.
#   If we can find the cycle point in O(n), that is the solution.
#   Problem:
#       the standard loop detection algo is O(n), but it doesn't return the
#       node that starts the loop. Rather, the "fast" pointer
#       eventually overtakes the slow pointer, proving a loop exists.

# Stack: time O(n), space O(n)
#   Add nodes from a to stack_a and b to stack_b. After we reach
#   the end of both lists, pop nodes from stack a and b until they
#   aren't equal. Then the previous popped node is the intersection
#   point.
#   Note:
#       It's true that this solution has O(n) memory, but the stacks
#       would be pointers to the objects, not copies of the objects
#       themselves. So the memory footprint would be much smaller
#       than 2 * size of nodes. A typical pointer is 8 bytes, or
#       64 bits, which is larger than a typical int (32 bits).


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == headB:
            return headA

        on = {"a": "a", "b": "b"}
        swap = {"a": "b", "b": "a"}
        to = {"a": headB, "b": headA}
        nodeA = headA
        nodeB = headB

        while True:
            if nodeA is nodeB:
                return nodeA

            nodeA = nodeA.next
            nodeB = nodeB.next

            if not nodeA:
                nodeA = to[on["a"]]
                on["a"] = swap[on["a"]]

            if not nodeB:
                nodeB = to[on["b"]]
                on["b"] = swap[on["b"]]

            if nodeA is headA and on["a"] == "a":
                break

        return None


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
        [[4, 1, 8, 4, 5], [5, 6, 1]],
    ]
    cases = [list(map(make_node, case)) for case in cases]

    node3 = ListNode(3)
    node2 = ListNode(2)
    node2.next = node3
    cases.append([node3, node2])

    s = Solution()

    i = 1
    for l1, l2 in cases:
        if i == 1:
            node1 = l1
            while node1.val != 8:
                node1 = node1.next

            node2 = l2
            while node2.next:
                node2 = node2.next

            node2.next = node1
            i += 1

        node = s.getIntersectionNode(l1, l2)
        print_node(node)

    cases2 = [[[4, 1, 8, 4, 5], [5, 6, 1]], [[4], [5]]]

    cases2 = [list(map(make_node, case)) for case in cases2]

    for l1, l2 in cases2:
        # print_node(l1)
        # print_node(l2)
        node = s.getIntersectionNode(l1, l2)
        print_node(node)
