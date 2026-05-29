# Last updated: 5/29/2026, 11:52:14 AM
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph={}
        for u,v in edges:
            if u not in graph:
                graph[u]=[]
            if v not in graph:
                graph[v]=[]
            graph[u].append(v)
            graph[v].append(u)
        res=[]
        visited=[False]*n
        def dfs(node,level):
            visited[node]=True
            level.append(node)
            for n1 in graph.get(node,[]):
                if not visited[n1]:
                    dfs(n1,level)
        for i in range(n):
            if not visited[i]:           
                level=[]
                dfs(i,level)
                res.append(level)
        rem=n
        count=0
        for i in res:
            rem-=len(i)
            count+=(len(i)*rem)
        return count