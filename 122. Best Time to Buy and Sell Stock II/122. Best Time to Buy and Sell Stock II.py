from ast import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        num_days = len(prices)
        # dp = [[0]*2 for _ in range(num_days+1)]

        # dp[num_days][0]=dp[num_days][1]=0

        next_day = [0,0]

        for i in range(num_days-1,-1,-1):
            curr_day = [0,0]
            for state in range(0,2):
                if state:
                    profit = max(-prices[i]+next_day[0],0+next_day[1])
                else:
                    profit = max(prices[i]+next_day[1],0+next_day[0])
                curr_day[state]=profit
            
            next_day = curr_day
        
        # we return 1st index because it represent we are at state buy and that means initial
        # sell is completed i.e. Buy-Sell process has been completed.
        return next_day[1] 

prices = [7,1,5,3,6,4]
obj = Solution()
print(obj.maxProfit(prices))