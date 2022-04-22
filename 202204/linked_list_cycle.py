from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        if not head.next:
            return False

        first = head
        second = head
        while first is not None and first.next is not None:
            first = first.next.next
            second = second.next
            if first == second:
                return True
        return False


if __name__ == "__main__":
    n1 = ListNode(3)
    n1.next = ListNode(2)
    n1.next.next = ListNode(0)
    n1.next.next.next = ListNode(-4)
    n1.next.next.next.next = n1.next
    print(Solution().hasCycle(n1))
