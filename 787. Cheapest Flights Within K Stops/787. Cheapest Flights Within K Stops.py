import collections
import heapq
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append([v, w])
            
        pq, seen = [(0, src, k + 1)], dict()
        while pq:
            d, u, s = heapq.heappop(pq)
            if u == dst:
                return d
            
            if u in seen and seen[u] >= s:
                continue
            seen[u] = s
            
            if s:
                for v, w in graph[u]:
                    heapq.heappush(pq, (d + w, v, s - 1))        
        return -1

n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1

obj = Solution()
obj.findCheapestPrice(n,flights,src,dst,k)