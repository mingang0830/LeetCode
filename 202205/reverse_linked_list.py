from platform import node
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = None # 이전 노드를 담음

        while node:
            swap = node.next
            node.next = prev
            prev = node
            node = swap
        
        return prev


if __name__ == "__main__":
    from remove_linked_list_elements import listToNode

    node1 = listToNode([1,2,3])
    print(node1)
    print(Solution().reverseList(node1))
    print(node1)
    