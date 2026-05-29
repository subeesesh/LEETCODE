# Last updated: 5/29/2026, 11:59:06 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(n1,n2):
            if n1 is None and n2 is None:
                return True
            if n1 is None or n2 is None :
                return False
            return n1.val==n2.val and helper(n1.left,n2.right) and helper(n1.right,n2.left)
        return helper(root.left,root.right)
        