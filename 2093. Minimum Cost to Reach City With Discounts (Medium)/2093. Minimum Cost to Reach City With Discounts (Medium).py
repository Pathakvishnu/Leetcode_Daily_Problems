from collections import defaultdict
from heapq import heappop,heappush
from typing import List

class Solution:
    def minCost(self,n:int,highways:List,discount:int):
        graph = defaultdict(dict)

        for u,v,d in highways:
            graph[u][v] = d
            graph[v][u] = d

        dist_mat = [[1e9 for _ in range(n)] for _ in range(discount+1)]

        for i in range(discount):
            dist_mat[i][0] = 0
        
        pq = [(0,0,discount)] # dist,src,discount

        while pq:
            cost, src, d = heappop(pq)
            if src==n-1:
                return cost
            if cost>dist_mat[d][src]:
                continue
            
            for dst,w in graph[src].items():
                if dist_mat[d][dst]>cost+w:
                    dist_mat[d][dst]=cost+w
                    heappush(pq,(dist_mat[d][dst],dst,d))
                if d>0 and dist_mat[d-1][dst]>cost+(w//2):
                    dist_mat[d-1][dst]=cost+(w//2)
                    heappush(pq,(dist_mat[d-1][dst],dst,d-1))

        return -1

n = 4
highways = [[1,3,17],[1,2,7],[3,2,5],[0,1,6],[3,0,20]]
discounts = 20

obj = Solution()
print(obj.minCost(n,highways,discounts))


