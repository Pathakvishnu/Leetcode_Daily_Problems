class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        max_freq = 1
        curr = 0

        for rgt in range(len(nums)):
            target = nums[rgt]
            curr+=target

            while (rgt-left+1)*target - curr>k:
                curr-=nums[left]
                left+=1
            
            max_freq = max(max_freq,rgt-left+1)
        
        return max_freq
            
        
