from collections import defaultdict
from typing import List

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n<=1:
            return 0
        keep_index = defaultdict(list)
        for i in range(n):
            keep_index[arr[i]].append(i)
            
        queue = [0]
        visited = set()
        step = 0
        while queue:
            nex = []
            for node in queue:
                if node==n-1:
                    return step
                
                for arr_idx in keep_index[arr[node]]:
                    if arr_idx not in visited:
                        visited.add(arr_idx)
                        nex.append(arr_idx)
                        
                # to avoid repetitive search 
                # don't use pop it will generate keyerror
                keep_index[arr[node]].clear() 
                    
                l = node-1
                r = node+1
                if l>=0 and l not in visited:
                    nex.append(l)
                    visited.add(l)
                if r<=n-1 and r not in visited:
                    nex.append(r)
                    visited.add(r)
                
            queue = nex
            step+=1
            
        return -1
            
arr = [100,-23,-23,404,100,23,23,23,3,404]
obj = Solution()
print(obj.minJumps(arr))