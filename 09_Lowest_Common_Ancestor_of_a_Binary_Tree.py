# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # Base case
        if not root or root == p or root == q:
            return root
        
        # Search in both subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If p is in one subtree and q in another → LCA found
        if left and right:
            return root
        
        # Otherwise return the non-null side
        return left if left else right
