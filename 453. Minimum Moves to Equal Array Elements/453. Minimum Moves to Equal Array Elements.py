from ast import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        curr_min = nums[0]
        tot_sum = nums[0]
        n = len(nums)
        for idx in range(1,n):
            tot_sum+=nums[idx]
            if nums[idx]<curr_min:
                curr_min = nums[idx]
        
        return tot_sum - curr_min*n

nums = [1,2,3]
obj = Solution()
print(obj.minMoves(nums))