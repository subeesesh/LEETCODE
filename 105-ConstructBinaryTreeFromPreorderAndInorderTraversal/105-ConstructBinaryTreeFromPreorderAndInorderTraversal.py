# Last updated: 5/29/2026, 11:59:00 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        map={val:i for i,val in enumerate(inorder)}
        self.x=0
        def help(left,right):
            if left>right:
                return None
            root_val=preorder[self.x]
            self.x+=1
            root=TreeNode(root_val)
            mid=map[root_val]
            root.left=help(left,mid-1)
            root.right=help(mid+1,right)
            return root
        return help(0,len(preorder)-1)