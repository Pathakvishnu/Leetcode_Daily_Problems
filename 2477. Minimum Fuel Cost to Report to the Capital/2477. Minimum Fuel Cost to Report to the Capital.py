from collections import defaultdict
from math import ceil
from typing import List


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = defaultdict(list)
        for s,d in roads:
            graph[s].append(d)
            graph[d].append(s)

        def dfs(node,parent):
            cand = 1
            for ngh in graph[node]:
                if ngh==parent: continue
                cand+=dfs(ngh,node)
            
            if node!=0:
                self.total_fuel+=ceil(cand/seats)
            return cand

        self.total_fuel = 0
        dfs(0,-1)

        return self.total_fuel

roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]]
seats = 2
obj = Solution()
obj.minimumFuelCost(roads,seats)