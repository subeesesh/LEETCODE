# Last updated: 5/29/2026, 11:58:30 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def nums(arr):
            num=0
            for i in arr:
                num=(num*10)+i
            return num
        res=[]
        def dfs(node,path):
            if not node:
                return 
            path.append(node.val)
            if not node.left and not node.right:
                res.append(path.copy())
            else:
                dfs(node.left,path)
                dfs(node.right,path)
            path.pop()
        dfs(root,[])
        ans=[]
        for i in res:
            ans.append(nums(i))
        return sum(ans)