import heapq
from typing import List

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        heap = []
        tot_sum = 0
        heapq.heapify(heap)
        for ele in nums:
            tot_sum+=ele
            heapq.heappush(heap,-1*ele)
        
        halve = tot_sum/2
        count=0
        while tot_sum>halve:
            max_ele = -1*heapq.heappop(heap)
            tot_sum-=(max_ele/2)
            heapq.heappush(heap,-1*(max_ele/2))
            count+=1
        
        return count

nums = [5,19,8,1]
obj = Solution()
print(obj.halveArray(nums))