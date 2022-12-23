from ast import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = prices[0]

        for i in range(1,len(prices)):
            if prices[i]-min_buy>max_profit:
                max_profit = prices[i]-min_buy
            min_buy = min(min_buy,prices[i])

        return max_profit

prices = [7,1,5,3,6,4]
obj = Solution()
print(obj.maxProfit(prices))