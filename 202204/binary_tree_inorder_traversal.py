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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result: List[int] = []
        """
        recursion!
        
        def inorder_traversal(node: Optional[TreeNode]):
            if node is None:
                pass
            else:
                inorder_traversal(node.left)
                result.append(node.val)
                inorder_traversal(node.right)

        inorder_traversal(root)
        """
        cur: Optional[TreeNode] = root
        stack: List[TreeNode] = []  # 부모 노드 저장
        while True:
            if cur:
                stack.append(cur)
                cur = cur.left
            elif stack:
                cur = stack.pop()
                result.append(cur.val)
                cur = cur.right
            else:
                break
        return result


if __name__ == "__main__":
    root1 = TreeNode(2)
    root1.left = TreeNode(3)
    root1.left.left = TreeNode(1)

    print(Solution().inorderTraversal(root1))
