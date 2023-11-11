class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.num_node = n
        self.adj = [[] for _ in range(n)]
        for src,dst,cost in edges:
            self.adj[src].append((cost, dst))
        
    def addEdge(self, edge: List[int]) -> None:
        self.adj[edge[0]].append((edge[2],edge[1]))

    def shortestPath(self, node1: int, node2: int) -> int:
        pq = [(0,node1)] # distance, starting node
        cost_array = [1e9]*(self.num_node)
        cost_array[node1] = 0

        while pq:
            curr_cost, curr_node = heappop(pq)
            if curr_cost>cost_array[curr_node]:
                continue
            if curr_node==node2:
                return curr_cost
            
            for cost, ngh in self.adj[curr_node]:
                tot_cost = cost + curr_cost
                if tot_cost < cost_array[ngh]:
                    cost_array[ngh] = tot_cost
                    heappush(pq,(tot_cost,ngh))

        return -1
            

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
