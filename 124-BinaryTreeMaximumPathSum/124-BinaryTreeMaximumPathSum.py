# Last updated: 5/29/2026, 11:58:34 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res=float('-inf')
        def height(node):
            if node is None:
                return 0
            left=max(0,height(node.left))
            right=max(0,height(node.right))
            self.res=max(self.res,node.val+left+right)
            return node.val+max(left,right)
        height(root)
        return self.res