from typing import List


class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        adj = [set() for _ in range(n)]

        for s,d in edges:
            adj[s-1].add(d-1)
            adj[d-1].add(s-1)

        odd_degree = [i for i in range(n) if len(adj[i])%2]

        def check(s,d):
            return s not in adj[d]

        if len(odd_degree)==0:
            return True
        if len(odd_degree)>4:
            return False
        if len(odd_degree)==2:
            node1,node2 = odd_degree
            return any(check(node1,i) and check(node2,i) for i in range(n))
        
        if len(odd_degree)==4:
            node1,node2,node3,node4 = odd_degree
            return check(node1,node2) and check(node3,node4) or check(node1,node3) and check(node2,node4) or check(node1,node4) and check(node3,node2)

        return False

n = 5
edges = [[1,2],[2,3],[3,4],[4,2],[1,4],[2,5]]

obj = Solution()
obj.isPossible(n,edges)


