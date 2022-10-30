from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        prev_dp = [1]
        res = []
        for i in range(1,numRows):
            # print(res)
            curr_dp = [0]*(i+1)
            for j in range(i+1):
                a=0
                b=0
                if j<=i-1:
                    a = prev_dp[j]
                if j-1>=0:
                    b = prev_dp[j-1]
                    
                curr_dp[j] = a+b
            res.append(prev_dp)
            prev_dp = curr_dp
        res.append(prev_dp)
        return res

numRows = 5
obj = Solution()
print(obj.generate(numRows))