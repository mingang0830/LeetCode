from typing import Optional, List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} - {}".format(self.val, self.next)


class Solution:

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curA: ListNode = headA
        curB: ListNode = headB
        while curA != curB:
            if curA:
                curA = curA.next
            else:
                curA = headB
            if curB:
                curB = curB.next
            else:
                curB = headA

        return curA


if __name__ == "__main__":
    its = ListNode(8)
    its.next = ListNode(4)
    its.next.next = ListNode(5)

    l1 = ListNode(4)
    l1.next = ListNode(1)
    l1.next.next = its

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(1)
    l2.next.next.next = its

    print(Solution().getIntersectionNode(l1, l2))