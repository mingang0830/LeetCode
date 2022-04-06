from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        if self:
            return "{}".format(self.val)


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False

        if p.val == q.val:
            """
            return 의 and, or 연산
            1) A and B
            - A,B 둘 다 참이면 B 를 출력
            - A,B 둘 다 거짓이면 A 를 출력
            - A, B 둘 중에 하나만 참이면 거짓인 값을 출력

            2) A or B
            - A,B 둘 다 참이면 A 를 출력
            - A,B 둘 다 거짓이면 B 를 출력
            - A, B 둘 중에 하나만 참이면 참인 값을 출력            
            """
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        return False


if __name__ == "__main__":
    node1 = TreeNode(1)
    node1.left = TreeNode(2)
    node1.right = TreeNode(1)
    node2 = TreeNode(1)
    node2.left = TreeNode(1)
    node2.right = TreeNode(2)

    print(Solution().isSameTree(node1, node2))
