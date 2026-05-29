# Last updated: 5/29/2026, 11:52:15 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return root.val==root.left.val+root.right.val