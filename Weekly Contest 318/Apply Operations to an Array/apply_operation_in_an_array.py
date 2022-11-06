from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        for i in range(n-1):
            if nums[i]==0:
                continue
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
                
        zero_idx = 0
        non_zero_idx = 1
        
        while non_zero_idx<n:
            if nums[zero_idx]==0 and nums[non_zero_idx]!=0 and non_zero_idx>zero_idx:
                nums[zero_idx],nums[non_zero_idx] = nums[non_zero_idx],nums[zero_idx]
            elif non_zero_idx<zero_idx:
                non_zero_idx=zero_idx+1
                
            if nums[zero_idx]!=0:
                zero_idx+=1
            if nums[non_zero_idx]==0:
                non_zero_idx+=1
            
        
        return nums
                        
nums = [1,2,2,1,1,0]
obj = Solution()
print(obj.applyOperations(nums))