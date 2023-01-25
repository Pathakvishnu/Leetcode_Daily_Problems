from ast import List

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        num_nodes = len(edges)
        dist1 = [1e7]*num_nodes
        dist2 = [1e7]*num_nodes

        def bfs(st_node,dist):
            queue = []
            queue.append(st_node)
            visited = [False]*num_nodes

            dist[st_node]=0

            while queue:
                node = queue.pop()
                if visited[node]:
                    continue
                visited[node]=True
                ngh = edges[node]
                if ngh!=-1 and not visited[ngh]:
                    queue.append(ngh)
                    dist[ngh] = dist[node]+1

            return dist

        dist1 = bfs(node1,dist1)
        dist2 = bfs(node2,dist2)

        min_dst_node = -1 
        min_dist_till = 1e7

        for node in range(num_nodes):
            if min_dist_till>max(dist1[node],dist2[node]):
                min_dst_node = node
                min_dist_till = max(dist1[node],dist2[node])
        return min_dst_node

edges = [2,2,3,-1]
node1 = 0
node2 = 1

obj = Solution()
obj.closestMeetingNode(edges,node1,node2)