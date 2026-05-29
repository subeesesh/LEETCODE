# Last updated: 5/29/2026, 11:58:48 AM
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int):
        result = []

        def dfs(node, current_sum, path):
            if not node:
                return

            current_sum += node.val
            path.append(node.val)

            # Check if leaf node
            if not node.left and not node.right:
                if current_sum == targetSum:
                    result.append(path.copy())

            dfs(node.left, current_sum, path)
            dfs(node.right, current_sum, path)

            # Backtrack
            path.pop()

        dfs(root, 0, [])
        return result
