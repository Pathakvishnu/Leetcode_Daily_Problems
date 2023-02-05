from collections import Counter
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(comb, target, curr, cand, ans):
            if target==0:
                ans.append(list(comb))
                return
            elif target<0:
                return 
            
            for next_curr in range(curr,len(cand)):
                num,freq = cand[next_curr]
                if freq<=0:
                    continue
                comb.append(num)
                cand[next_curr] = (num,freq-1)
                backtrack(comb, target-num, next_curr, cand, ans)

                cand[next_curr] = (num,freq)
                comb.pop()
        
        cand_count = Counter(candidates)  
        cand = [(k,v) for k,v in cand_count.items()]
        ans,comb = [],[]
        backtrack(comb,target,0,cand,ans)
        return ans

candidates = [10,1,2,7,6,1,5]
target = 8
obj = Solution()
obj.combinationSum2(candidates,target)