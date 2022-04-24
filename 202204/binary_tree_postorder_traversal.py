from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        if self:
            return "{}".format(self.val)


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result: List[int] = []
        """
        recursion!
        def postorder_traversal(node: Optional[TreeNode]):
            if node is not None:
                if node.left:
                    postorder_traversal(node.left)
                if node.right:
                    postorder_traversal(node.right)
                result.append(node.val)

        postorder_traversal(root)
        """
        if root is None:
            return result

        stack: List[TreeNode] = [root]
        while stack:
            cur = stack.pop()
            result.insert(0, cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)

        return result


if __name__ == "__main__":
    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    root1.right.left = TreeNode(3)

    print(Solution().postorderTraversal(root1))

