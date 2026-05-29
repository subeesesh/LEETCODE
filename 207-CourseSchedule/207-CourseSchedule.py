# Last updated: 5/29/2026, 11:57:17 AM
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for u, v in prerequisites:
            graph[u].append(v)
        visited = set()
        recStack = set()
        def dfs(node):
            visited.add(node)
            recStack.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    if dfs(nei):
                        return True
                elif nei in recStack:
                    return True
            recStack.remove(node)
            return False
        for i in range(numCourses):
            if i not in visited:
                if dfs(i):
                    return False   
        return True              
