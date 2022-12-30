from ast import List
from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        """
        To avoid the TLE we use priority queue instead of stacks since it avoid unnecessary processing. And
        process the path with high probability first.
        """
        graph = defaultdict(list)
        for idx,(s,d) in enumerate(edges):
            graph[s].append([d,succProb[idx]])
            graph[d].append([s,succProb[idx]])

        visited = [0]*n
        heap = [(-1,start)] # node,probability

        while heap:
            pr,n = heappop(heap)
            if n==end:
                return -pr        

            for ngh, edge_pr in graph[n]:
                if not visited[ngh]:
                    heappush(heap,(pr*edge_pr,ngh))
            visited[n]=1
        return 0


n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
start = 0
end = 2