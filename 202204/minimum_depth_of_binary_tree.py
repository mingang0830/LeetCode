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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1

        left: int = self.minDepth(root.left) + 1
        right: int = self.minDepth(root.right) + 1

        if root.left is None:
            return right
        if root.right is None:
            return left

        return min(left, right)


if __name__ == "__main__":
    n1 = TreeNode(2)
    n1.right = TreeNode(3)
    n1.right.right = TreeNode(4)
    n1.right.right.right = TreeNode(5)
    n1.right.right.right.right = TreeNode(6)
    print(Solution().minDepth(n1))