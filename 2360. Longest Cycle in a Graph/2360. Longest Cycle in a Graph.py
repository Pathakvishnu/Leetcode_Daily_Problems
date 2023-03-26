class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        num_nodes = len(edges)
        visited = [0]*num_nodes
        answer = -1

        def dfs(cur_node, dist):
            nonlocal answer
            visited[cur_node]=True
            ngh = edges[cur_node]

            if ngh!=-1 and not visited[ngh]:
                dist[ngh] = dist[cur_node] + 1
                dfs(ngh, dist)
            elif ngh!=-1 and dist.get(ngh,0):
                answer = max(answer, dist[cur_node]-dist[ngh]+1)

        for n in range(num_nodes):
            if not visited[n]:
                dist = dict()
                dist[n]=1
                dfs(n,dist)

        return answer
      
edges = [3,3,4,2,3]
obj = Solution()
obj.longestCycle(edges)
