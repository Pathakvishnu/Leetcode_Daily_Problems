from typing import List

class Solution:
    def satisfy(self,weights,days,capacity):
        days_need = 1
        curr_load = 0
        for i in range(len(weights)):
            curr_load+=weights[i]
            if curr_load>capacity:
                days_need+=1
                curr_load = weights[i]
        
        return days_need<=days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total_load = 0
        max_load = 0

        for i in range(len(weights)):
            total_load+=weights[i]
            max_load = max(max_load,weights[i])

        l = max_load
        r = total_load

        while l<r:
            mid = (l+r)//2
            if self.satisfy(weights,days,mid):
                r = mid
            else:
                l = mid+1
        
        return l

weights = [3,2,2,4,1,4]
days = 3
obj = Solution()
obj.shipWithinDays(weights,days)        