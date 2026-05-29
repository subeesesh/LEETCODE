# Last updated: 5/29/2026, 11:59:03 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res=[]
        q=deque([root])
        i=0
        while q:
            n=len(q)
            level=deque()
            for _ in range(n):
                node=q.popleft()
                if i%2==0:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                if node.left :
                    q.append(node.left)
                if node.right :
                    q.append(node.right)
            res.append(list(level))
            i+=1
        return res
            
            
            