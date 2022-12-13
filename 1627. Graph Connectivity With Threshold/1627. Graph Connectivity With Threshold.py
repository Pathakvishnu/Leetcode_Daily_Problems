from ast import List

class UnionFind:
    """
    Union by size
    """
    def __init__(self,num_nodes):
        self.par = list(range(num_nodes))
        self.size = [1]*num_nodes

    def find(self,node):
        if self.par[node]!=node:
            self.par[node] = self.find(self.par[node]) # compression
        return self.par[node]
    
    def union(self,src,dst):
        par_src,par_dst = self.find(src),self.find(dst)
        if par_src==par_dst:
            return False
        if self.size[par_src]<self.size[par_dst]:
            par_src,par_dst = par_dst,par_src

        self.par[par_dst] = par_src
        self.size[par_src]+=self.size[par_dst]
        self.size[par_dst] = self.size[par_src]
        return True

    def getSize(self,node):
        return self.size[self.find(node)]
        
class Solution:        

    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        if threshold==0:
            return [True]*(len(queries))
        
        uf = UnionFind(n+1)
        for i in range(threshold+1,n+1):
            j = i<<1
            while j<=n:
                uf.union(i,j)
                j+=i
        ans = []
        for s,d in queries:
            ans.append(uf.find(s)==uf.find(d))
        
        return ans

n = 6
threshold = 2
queries = [[1,4],[2,5],[3,6]]

obj = Solution()
print(obj.areConnected(n,threshold,queries))

        

        