from collections import defaultdict
from typing import List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        """n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]"""
        res = 1e9
        adj = defaultdict(set)
        for s, d, dst in roads:
            adj[s].add((d, dst))
            adj[d].add((s, dst))
        """
        {1: [(2, 9), (4, 7)], 2: [(3, 6), (4, 5)]}
        """
        def DFS(adj, i):
            for j, d in adj[i]:
                if j not in visited:
                    visited.add(j)
                    DFS(adj, j)
                
        visited = {1}
        DFS(adj, 1)
    
        for s, d, dst in roads:
            if s in visited and d in visited:
                res = min(res, dst)
        return res
        
        
n = 4
roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]

obj = Solution()
print(obj.minScore(n,roads))