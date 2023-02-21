from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        first occurence of each element is at even index (0,2,..)
        second occurence of each element is at odd index (1,3,..)
        """
        low = 0
        high = len(nums)-1

        while low<high:
            mid = low +(high-low)//2
            if nums[mid]==nums[mid^1]:
                low = mid+1
            else:
                high = mid
            
        return nums[low]
        
nums = [1,1,2,3,3,4,4,5,5,6,6]
obj = Solution()
obj.singleNonDuplicate(nums)