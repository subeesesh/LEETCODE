# Last updated: 5/29/2026, 11:52:22 AM
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph={}
        for u,v in edges:
            if u not in graph:
                graph[u]=[]
            if v not in graph:
                graph[v]=[]
            graph[u].append(v)
            graph[v].append(u)
        visited=set()
        def dfs(node):
            if node==destination:
                return True
            visited.add(node)
            for n1 in graph[node]:
                if n1 not in visited:
                    if dfs(n1):
                        return True
            return False
        return dfs(source)