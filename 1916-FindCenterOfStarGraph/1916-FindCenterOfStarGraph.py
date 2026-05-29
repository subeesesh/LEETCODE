# Last updated: 5/29/2026, 11:52:42 AM
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph={}
        for u,v in edges:
            if u not in graph:
                graph[u]=[]
            if v not in graph:
                graph[v]=[]
            graph[u].append(v)
            graph[v].append(u)
        for i in graph:
            if len(graph.get(i))>1:
                return i
        return 0