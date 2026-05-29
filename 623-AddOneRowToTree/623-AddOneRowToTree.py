# Last updated: 5/29/2026, 11:54:54 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        q = deque([root])
        current_depth = 1
        while q:
            size = len(q)
            if current_depth == depth - 1:
                for _ in range(size):
                    node = q.popleft()
                    left = node.left
                    right = node.right
                    node.left = TreeNode(val)
                    node.left.left = left
                    node.right = TreeNode(val)
                    node.right.right = right
                break
            for _ in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            current_depth += 1
        return root