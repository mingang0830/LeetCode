from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy: Optional[ListNode] = head
        while dummy:
            if dummy.next is not None and dummy.val == dummy.next.val:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next

        return head


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(1)
    l1.next.next = ListNode(1)

    print(Solution().deleteDuplicates(l1))
