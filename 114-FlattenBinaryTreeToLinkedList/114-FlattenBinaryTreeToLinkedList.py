# Last updated: 5/29/2026, 11:58:47 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.curr=None
        self._flatten(root)
        """
        Do not return anything, modify root in-place instead.
        """
    def _flatten(self,root):
        if root is None:
            return
        self._flatten(root.right)
        self._flatten(root.left)
        root.right=self.curr
        root.left=None
        self.curr=root