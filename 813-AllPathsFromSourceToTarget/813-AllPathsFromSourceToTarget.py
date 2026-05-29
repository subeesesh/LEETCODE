# Last updated: 5/29/2026, 11:54:22 AM
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res=[]
        path=[]
        def dfs(node):
            path.append(node)
            if node==len(graph)-1:
                res.append(path.copy())
            for n1 in graph[node]:
                dfs(n1)
            path.pop()
        dfs(0)
        return res