class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
                
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        dsu = UnionFind(n)
        for u, v in edges:
            dsu.union(u, v) 
        C = Counter([dsu.find(i) for i in range(n)])
        groupCounts = list(C.values())
        ans = 0
        firstGroupCount = groupCounts[0]
        for i in range(1, len(groupCounts)):
            ans += firstGroupCount * groupCounts[i]
            firstGroupCount += groupCounts[i]  
        return ans
      
n = 3
edges = [[0,1],[0,2],[1,2]]

obj = Solution()
obj.countPairs(n,edges)
