# Last updated: 5/29/2026, 11:55:00 AM
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph={}
        for i in range(len(isConnected)):
            graph[i]=[]
            for j in range(len(isConnected)):
                if isConnected[i][j]==1:
                    graph[i].append(j)
        visited=set()
        count=0
        def dfs(node):
            visited.add(node)
            for n1 in graph[node]:
                if n1 not in visited:
                    dfs(n1)
        for i in range(len(graph)):
            if i not in visited:
                count+=1
                dfs(i)
        return count
            