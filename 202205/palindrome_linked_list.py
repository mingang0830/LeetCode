from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = None 

        while node:
            swap = node.next
            node.next = prev
            prev = node
            node = swap
        
        return prev  
    """
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        reversed_list :Optional[ListNode] = self.reverseList(head)
        
        while head:
            if reversed_list.val != head.val:
                return False
            else:
                head = head.next
                reversed_list = reversed_list.next
        
        return True
        """
        temp :List[int]= []
        while head:
            temp.append(head.val)
            head = head.next
        
        return temp == temp[::-1]

if __name__ == "__main__":
    from remove_linked_list_elements import listToNode
    l1 = listToNode([1,1,2,1])
    print(Solution().isPalindrome(l1))
