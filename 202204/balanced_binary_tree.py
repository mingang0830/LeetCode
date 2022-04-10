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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def comparison(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0

            left: int = comparison(root.left)
            right: int = comparison(root.right)

            # -1 이 한번이라도 리턴되면 계속 -1로 나오게 됨
            if left == -1 or right == -1 or abs(left-right) >= 2:
                return -1

            return max(left, right) + 1

        if comparison(root) == -1:
            return False
        else:
            return True


if __name__ == "__main__":
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(3)
    root1.right.right = TreeNode(3)
    root1.right.right.left = TreeNode(4)
    root1.right.right.left.right = TreeNode(4)
    print(Solution().isBalanced(root1))

