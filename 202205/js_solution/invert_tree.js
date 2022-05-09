function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
 }

 var invertTree = function(root) {
    if (!root) return root;
    var left = root.left;
    var right = root.right;
    root.left = invertTree(right);
    root.right = invertTree(left);
    
    return root;
};