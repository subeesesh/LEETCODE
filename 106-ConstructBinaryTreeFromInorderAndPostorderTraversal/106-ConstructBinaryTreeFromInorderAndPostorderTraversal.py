# Last updated: 5/29/2026, 11:58:59 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        map={val:i for i,val in enumerate(inorder)}
        self.x=len(postorder)-1
        def help(left,right):
            if left>right:
                return None
            root_val=postorder[self.x]
            self.x-=1
            root=TreeNode(root_val)
            mid=map[root_val]
            root.right=help(mid+1,right)
            root.left=help(left,mid-1)
            return root
        return help(0,len(postorder)-1)