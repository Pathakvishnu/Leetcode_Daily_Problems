from collections import defaultdict
from typing import List

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adj = defaultdict(list)
        for s,d in edges:
            adj[s].append(d)
            adj[d].append(s)
        
        ans = [0]*n
        def dfs(node,parent):
            node_vec = [0]*26
            node_vec[ord(labels[node])-ord('a')]=1
            for child in adj[node]:
                if child==parent:
                    continue
                child_vec = dfs(child,node)
                for i in range(26):
                    node_vec[i]+=child_vec[i]

            ans[node] = node_vec[ord(labels[node])-ord('a')]
            return node_vec
        vector = dfs(0,-1)
        # print(vector)
        return ans

n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
labels = "abaedcd"

obj = Solution()
obj.countSubTrees(n,edges,labels)