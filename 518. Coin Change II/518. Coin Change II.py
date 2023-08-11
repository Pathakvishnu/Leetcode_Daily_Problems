class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        @cache
        def minCoin(idx,target):
            if idx==0:
                if target%coins[idx]==0:
                    return 1
                return 0
            pick=0
            if coins[idx]<=target:
                pick = minCoin(idx,target-coins[idx])
            notpick =  minCoin(idx-1,target)
            
            return pick+notpick
        
        return minCoin(n-1,amount)
            
            
