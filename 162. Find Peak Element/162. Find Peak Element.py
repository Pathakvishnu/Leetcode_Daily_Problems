from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        if n==1:
            return 0

        l=0 # left pointer 
        r=n-1 # right pointer

        if nums[0]>nums[1]:
            return 0

        if nums[n-1]>nums[n-2]:
            return n-1
            
        while l<=r:
            mid = l+(r-l)//2
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid-1]>nums[mid]:
                r = mid-1
            elif nums[mid+1]>nums[mid]:
                l = mid+1
        return -1

nums = [1,2,1,3,5,6,4]
obj = Solution()
print(obj.findPeakElement(nums))