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
    def hasPathSum(self, root: Optional[TreeNode], target_sum: int) -> bool:
        if root is None:
            return False

        if root.left is None and root.right is None and target_sum == root.val:
            # leaf value == target_sum
            return True

        target_sum -= root.val

        return self.hasPathSum(root.left, target_sum) or self.hasPathSum(root.right, target_sum)


if __name__ == "__main__":
    n1 = TreeNode(5)
    n1.right = TreeNode(8)
    n1.right.right = TreeNode(4)
    n1.right.right.right = TreeNode(1)
    n1.right.left = TreeNode(13)
    n1.left = TreeNode(4)
    n1.left.left = TreeNode(11)
    n1.left.left.left = TreeNode(7)
    n1.left.left.right = TreeNode(2)
    print(Solution().hasPathSum(n1, 22))