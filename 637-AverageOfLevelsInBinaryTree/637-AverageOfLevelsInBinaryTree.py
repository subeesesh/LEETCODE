# Last updated: 5/29/2026, 11:54:51 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional, List

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        res = []
        q = deque([root])

        while q:
            level = []
            size = len(q)

            for _ in range(size):
                t = q.popleft()
                level.append(t.val)

                if t.left is not None:
                    q.append(t.left)
                if t.right is not None:
                    q.append(t.right)

            res.append(sum(level)/len(level))

        return res

        