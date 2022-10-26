from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem_seen = {0:0} # to store if reminder has been seen earlier or not
        
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum+=nums[i]
            if prefix_sum%k not in rem_seen: # if reminder not seen
                rem_seen[prefix_sum%k]=i+1
            elif rem_seen[prefix_sum%k]<i: # if seen we check if it's not the same index
                return True
        return False

nums = [23,2,4,6,7]
k = 6
obj = Solution()
print(obj.checkSubarraySum(nums,k))