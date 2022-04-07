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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def subtree_comparison(left: Optional[TreeNode], right: Optional[TreeNode]):
            if not left and not right:
                return True
            elif not left or not right:
                return False
            else:
                return left.val == right.val and subtree_comparison(left.left, right.right) \
                       and subtree_comparison(left.right, right.left)

        return subtree_comparison(root.left, root.right)


if __name__ == "__main__":
    n1 = TreeNode(1)
    n1.left = TreeNode(2)
    n1.left.left = TreeNode(2)
    n1.right = TreeNode(2)
    n1.right.left = TreeNode(2)
    print(Solution().isSymmetric(n1))