class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        res, num_one = 0,0
        for d in s:
            if d=="0":
                res = min(res+1,num_one)
            else:
                num_one+=1  
        return res

s = "0101011"
obj = Solution()
obj.minFlipsMonoIncr(s)