from typing import List


class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        self.res = []
        path = []
        self.dfs(path,num,0)
        return self.res

    def checkValidity(self,path,num):
        n = len(path)
        return n<2 or (n>=2 and num==path[n-1]+path[n-2]) 
        
    def dfs(self,path,inp,st_idx):
        if self.res:
            return
        str_len = len(inp)
        if st_idx==str_len:
            if len(path)>=3:
                self.res = path[:] # don't use self.res=path it point to same location whereas : create a copy of the data
                return

        val = 0
        for i in range(st_idx,str_len):
            val = 10*val + int(inp[i])
            if val>2147483647:
                return
            if self.checkValidity(path,val):
                path.append(val)
                self.dfs(path,inp,i+1)
                path.pop()

            if val==0:
                return
                    
n = "1101111"     
obj = Solution()
print(obj.splitIntoFibonacci(n))