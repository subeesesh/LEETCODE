# Last updated: 5/29/2026, 11:54:18 AM
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=set()
        def dfs(node):
            visited.add(node)
            for n1 in rooms[node]:
                if n1 not in visited:
                    dfs(n1)
        dfs(0)
        return len(visited)==len(rooms)