# Last updated: 5/29/2026, 11:57:30 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        if root is None :
            return res
        q=deque()
        q.append(root)
        while q:
            n=len(q)
            for i in range(n):
                x=q.popleft()
                if i==n-1:
                    res.append(x.val)
                if x.left is not None:
                    q.append(x.left)
                if x.right is not None:
                    q.append(x.right)
        return res
