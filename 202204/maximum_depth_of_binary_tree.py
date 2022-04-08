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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            left: int = 0
            right: int = 0

            if root.left is not None:
                left = self.maxDepth(root.left)

            if root.right is not None:
                right = self.maxDepth(root.right)

            return 1 + max(left, right)


if __name__ == "__main__":
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.left.left = TreeNode(20)
    root1.right = TreeNode(15)
    root1.right = TreeNode(7)

    print(Solution().maxDepth(root1))
