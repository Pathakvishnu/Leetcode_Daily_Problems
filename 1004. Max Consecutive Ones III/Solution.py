class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        no_of_zeros = 0
        max_ones = 0

        while right<len(nums):
            if nums[right]==0:
                no_of_zeros+=1
            if no_of_zeros>k:
                if nums[left]==0:
                    no_of_zeros-=1
                left+=1
            
            if no_of_zeros<=k:
                max_ones = max(max_ones, right-left+1)

            right+=1
        
        return max_ones
