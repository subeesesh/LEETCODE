# Last updated: 5/29/2026, 11:55:17 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res=[]
        q=deque()
        q.append(root)
        while q:
            n=len(q)
            level=deque()
            for _ in range(n):
                node=q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(list(level))
        ans=[]
        for i in res:
            ans.append(max(i))
        return ans