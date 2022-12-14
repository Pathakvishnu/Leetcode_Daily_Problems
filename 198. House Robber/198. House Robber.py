from ast import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums)
        
        cur,prev,prev2 = 0,0,0

        for i in range(len(nums)):
            curr = max(nums[i]+prev2,prev)
            prev2 = prev
            prev = curr
        
        return curr

    