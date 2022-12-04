from typing import List

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        cum_sum = list()
        tot = 0
        n = 0 # total elements
        for val in nums:
            tot+=val
            cum_sum.append(tot)
            n+=1
            
        idx = 0
        min_avg = 1e9
        min_idx = None
        while idx<n:
            avg1 = cum_sum[idx]//(idx+1)
            avg2 = 0
            if n-idx-1>0:
                avg2 = (tot-cum_sum[idx])//(n-idx-1)
            if abs(avg1-avg2)<min_avg:
                min_avg = abs(avg1-avg2)
                min_idx = idx
            idx+=1
        
        return min_idx

nums = [2,5,3,9,5,3]
obj = Solution()
print(obj.minimumAverageDifference(nums))