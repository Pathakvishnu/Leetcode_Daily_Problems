from ast import List

class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        n = len(nums)
        mid = n//2
        i = 0
        nums = sorted(nums)
        for j in range(n-mid,n):
            i+= 2*nums[i]<=nums[j]

        return i*2
    
nums = [9,2,5,4]
obj = Solution()
obj.maxNumOfMarkedIndices(nums)