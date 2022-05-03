from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        if self:
            return "{},{}".format(self.val, self.next)


def listToNode(list_: List) -> Optional[ListNode]:
        result: Optional[ListNode]= None
        while list_:
            result = ListNode(list_.pop(), result)
        return result


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy: Optional[ListNode] = head
        
        while dummy and head :
            if head.val == val: # head 의 첫번째 val이 param val 과 같을 경우 요소 제거 
                head = head.next
                dummy = head
            elif dummy.next:
                if dummy.next.val == val:
                    dummy.next = dummy.next.next # val 요소 제거
                else:
                    dummy = dummy.next
            else:
                break        
        return head
        

if __name__ == "__main__":
    print(Solution().removeElements(listToNode([6,1,2,6,3,4,5,6]), 6))