class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def __repr__(self):
        if self:
            return "{}".format(self.val)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left ,p, q)
        
        return root

if __name__ == "__main__":
    t1 = TreeNode(6)
    t1.left = TreeNode(2)
    t1.right = TreeNode(8)
    t1.left.left = TreeNode(0)
    t1.left.right = TreeNode(4)
    print(Solution().lowestCommonAncestor(t1, t1.left, t1.left.right))