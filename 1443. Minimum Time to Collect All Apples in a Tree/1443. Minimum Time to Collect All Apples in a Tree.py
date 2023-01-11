from ast import List
from collections import defaultdict

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = defaultdict(list)
        for s,d in edges:
            adj[s].append(d)
            adj[d].append(s)
        
        def dfs(node,par):
            total_time, child_time = 0,0
            for child in adj[node]:
                if child==par:
                    continue
                child_time = dfs(child,node)

                if child_time or hasApple[child]:
                    total_time +=child_time+2
            
            return total_time

        return dfs(0,-1)

n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple = [False,False,True,False,True,True,False]

obj = Solution()
obj.minTime(n,edges,hasApple)