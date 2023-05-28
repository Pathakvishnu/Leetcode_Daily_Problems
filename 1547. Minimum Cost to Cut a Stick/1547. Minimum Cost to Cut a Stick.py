class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        dp = {}
        cuts = [0] + sorted(cuts) + [n]

        def cost(left,right):
            if dp.get((left,right),-1)!=-1:
                return dp[(left,right)]
            if right-left==1: # since we can't make any cut
                return 0
            ans = min(cuts[right]-cuts[left] + cost(left,mid) + cost(mid,right) for mid in range(left+1,right))
            
            dp[(left,right)] = ans

            return ans

        return cost(0,len(cuts)-1)
      
n = 7, cuts = [1,3,4,5]
