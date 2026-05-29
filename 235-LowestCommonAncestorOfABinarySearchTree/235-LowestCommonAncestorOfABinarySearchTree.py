# Last updated: 5/29/2026, 11:56:54 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        x=max(p.val,q.val)
        y=min(p.val,q.val)
        if y<=root.val<=x:
            return root
        if root.val>y:
            return self.lowestCommonAncestor(root.left,p,q)
        if root.val<x:
            return self.lowestCommonAncestor(root.right,p,q)