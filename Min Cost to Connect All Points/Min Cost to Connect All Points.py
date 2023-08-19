class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        class UnionFind:
            def __init__(self, n):
                self.parent = list(range(n))
                self.size = [1] * n
                self.max_size = 1

            def find(self, x):
                # Finds the root of x
                if x != self.parent[x]:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y):
                # Connects x and y
                root_x = self.find(x)
                root_y = self.find(y)
                if root_x != root_y:
                    if self.size[root_x] < self.size[root_y]:
                        root_x, root_y = root_y, root_x
                    self.parent[root_y] = root_x
                    self.size[root_x] += self.size[root_y]
                    self.max_size = max(self.max_size, self.size[root_x])
                    return True
                return False

        # first lets create a dense graph with all node connected to each other
        graph = []
        n = len(points)
        for i in range(n):
            for j in range(i+1,n):
                node_a = points[i]
                node_b = points[j]
                wgt = abs(node_a[0]-node_b[0])+abs(node_a[1]-node_b[1])
                graph.append((i,j,wgt))
        
        graph = sorted(graph,key=lambda k:k[2])
        uf = UnionFind(n)

        total_cost = 0
        count = 0
        for u,v,cost in graph:
            # since we got all the edges for MST
            if count==n-1:
                break

            if uf.union(u,v):
                total_cost+=cost
                count+=1
            
        return total_cost
                
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
