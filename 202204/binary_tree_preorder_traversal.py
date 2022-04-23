from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result: List[int] = []

        """
        recursion
        
        def preorder_traversal(node: Optional[TreeNode]):
            if node is not None:
                result.append(node.val)
                if node.left:
                    preorder_traversal(node.left)
                if node.right:
                    preorder_traversal(node.right)

        preorder_traversal(root)
        """

        cur: Optional[TreeNode] = root
        stack: List[TreeNode] = []
        while stack or cur:
            if cur:
                result.append(cur.val)
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                cur = cur.right

        return result
