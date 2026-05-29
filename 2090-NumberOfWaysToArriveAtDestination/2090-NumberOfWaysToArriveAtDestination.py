# Last updated: 5/29/2026, 11:52:28 AM
class Solution:
    MOD = 10**9 + 7

    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # Build adjacency list
        graph = {i: [] for i in range(n)}
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        # Distance and ways arrays
        dist = [float('inf')] * n
        ways = [0] * n

        dist[0] = 0
        ways[0] = 1

        # Min-heap: (distance, node)
        pq = [(0, 0)]

        while pq:
            curr_dist, u = heapq.heappop(pq)

            if curr_dist > dist[u]:
                continue

            for v, w in graph[u]:
                new_dist = curr_dist + w

                if new_dist < dist[v]:
                    dist[v] = new_dist
                    ways[v] = ways[u]
                    heapq.heappush(pq, (new_dist, v))

                elif new_dist == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % self.MOD

        return ways[n - 1]