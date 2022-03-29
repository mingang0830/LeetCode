from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cursor: ListNode = ListNode()
        dummy: ListNode = cursor  # reference
        while list1 and list2:
            if list1.val < list2.val:
                cursor.next = list1  # 같은 값을 참조하기 때문에 dummy에도 next값이 추가(dummy.next.next...)
                list1 = list1.next  # list1을 다음 노드로 update
            else:
                cursor.next = list2
                list2 = list2.next

            # dummy의 포인터로 cur를 next로 옮김
            # dummy.next와 cursor가 같은 값을 참조
            cursor = cursor.next

        if list1 is not None:
            cursor.next = list1
        else:
            cursor.next = list2

        return dummy.next  # 처음에 생성할때 만들어지는 val값 0을 제외한 next들의 값


l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(6)

l2 = ListNode(3)
l2.next = ListNode(5)

print(Solution().mergeTwoLists(l1, l2))


