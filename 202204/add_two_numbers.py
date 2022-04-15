from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if self:
            return "{},{}".format(self.val, self.next)


class Solution:
    def listToNode(self, list_: List) -> Optional[ListNode]:
        """
        뻘짓...
        result: Optional[ListNode] = ListNode(list_[0])
        curr: Optional[ListNode] = result

        for i in range(1, len(list_)):
            curr.next = ListNode(list_[i])
            curr = result.next
        """
        result: Optional[ListNode]= None
        while list_:
            result = ListNode(list_.pop(), result)
        return result

    def nodeToList(self, node: Optional[ListNode]) -> List:
        result: List = []
        while node is not None:
            result.append(node.val)
            node = node.next
        return result

    def reverse_listnode(self, list_node: Optional[ListNode]) -> Optional[ListNode]:
        temp: List = []
        while list_node is not None:
            temp.insert(0, list_node.val)
            list_node = list_node.next
        return self.listToNode(temp)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_lst: List = self.nodeToList(self.reverse_listnode(l1))
        l2_lst: List = self.nodeToList(self.reverse_listnode(l2))
        sum_int = int("".join(map(str, l1_lst))) + int("".join(map(str, l2_lst)))

        return self.reverse_listnode(self.listToNode([int(i) for i in str(sum_int)]))


if __name__ == '__main__':
    n1 = Solution().listToNode([9, 9, 9, 8, 7, 9, 9])
    n2 = Solution().listToNode([9, 9, 9, 9])
    print(Solution().addTwoNumbers(n1, n2))
