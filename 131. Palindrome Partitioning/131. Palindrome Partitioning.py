from typing import List

class Solution:
    def partition(self, inp: str) -> List[List[str]]:
        start,end = 0,len(inp)
        ans = []
        def backtrack(s,e,tmp):
            if s==e:
                ans.append(tmp[:])
            for i in range(s,e):
                curr = inp[s:i+1]
                if curr==curr[::-1]:
                    tmp.append(curr)
                    backtrack(i+1,e,tmp)
                    tmp.pop() 
        
        backtrack(start,end,[])
        return ans

inp = "aab"
obj = Solution()
obj.partition(inp)