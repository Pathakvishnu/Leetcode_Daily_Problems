

from typing import List
import math
class Solution:
    def solve(self, N : int, K : int, arr : List[int]) -> int:
        # code here
        prefix_sum = [0]*N
        prefix_sum[0] = arr[0]
        for i in range(1,N):
            prefix_sum[i] = prefix_sum[i-1]+arr[i]
        factor = [1]
        for i in range(2,int(math.sqrt(prefix_sum[-1]))+1):
            if prefix_sum[-1]%i==0:
                factor.append(i)
                if i!=prefix_sum[-1]//i:
                    factor.append(prefix_sum[-1]//i)
                    
        if K==1:
            return prefix_sum[-1]
        
        ans = 1
        factor
        for f in reversed(sorted(factor)):
            partition = 0
            for i in range(N):
                if prefix_sum[i]%f==0:
                    partition+=1

                if partition>=K:
                    return f
        return ans


#{ 
 # Driver Code Starts


class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        
        K = int(input())
        
        
        arr=IntArray().Input(N)
        
        obj = Solution()
        res = obj.solve(N, K, arr)
        
        print(res)
        

# } Driver Code Ends