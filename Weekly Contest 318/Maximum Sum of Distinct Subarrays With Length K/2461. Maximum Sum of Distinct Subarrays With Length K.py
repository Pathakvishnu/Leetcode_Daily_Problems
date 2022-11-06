from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        record = dict()
        count = 0
        total = 0
        max_sum = 0
        l=0
        r=0
        while r<n:
            count+=1
            while record.get(nums[r],0)!=0:
                del record[nums[l]]
                total-=nums[l]
                l+=1
                count-=1
            
            record[nums[r]]=1
                
            total+=nums[r]

            if count==k:
                if total>max_sum:
                    max_sum=total
                del record[nums[l]]
                total-=nums[l]
                l+=1
                count-=1
            
            r+=1
        
        return max_sum

nums = [1,4,5,4,2,2,9,2]
k = 3
obj = Solution()
print(obj.maximumSubarraySum(nums,k))