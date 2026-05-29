# Last updated: 5/29/2026, 11:54:34 AM
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n + 1)}
        for u,v,x in times:
            graph[u].append([v,x])
        dist=[float('inf')]*(n+1)
        dist[k]=0
        pq=[(0,k)]
        while pq:
            curr,node=heapq.heappop(pq)
            if curr>dist[node]:
                continue
            for n1,w in graph[node]:
                new=curr+w
                if new<dist[n1]:
                    dist[n1]=new
                    heapq.heappush(pq,(new,n1))
        max_time=max(dist[1:])
        return max_time if max_time!=float('inf') else -1