# Last updated: 5/29/2026, 11:52:59 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        q=deque([root])
        row=0
        # res=[]
        while q:
            level_size=len(q)
            level=deque()
            before=None
            for _ in range(level_size):
                node=q.popleft()
                if row%2==0:
                    if node.val%2==0 or (before is not None and before>=node.val):
                        return False
                if row%2!=0:
                    if node.val%2!=0 or (before is not None and before<=node.val):
                        return False
                before=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            row+=1
        return True