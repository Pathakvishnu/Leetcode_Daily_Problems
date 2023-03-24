
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)

        for s,d in connections:
            adj[s].append((d,1)) # original edge
            adj[d].append((s,0)) # artificial edge
        
        count=0
        
        def dfs(node,parent,adj):
            nonlocal count
            for child,n_type in adj[node]:
                if child!=parent:
                    count+=n_type
                    dfs(child,node,adj)
        
        dfs(0,-1,adj)

        return count
      
      
n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
obj = Solution()
obj.minReorder(n,connections)
