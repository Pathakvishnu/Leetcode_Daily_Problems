class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        """
        [1,3,0,0,2,0,0,4]
        [0,0,1,2,0,1,2,0] # counter for consecutive zeros if not seen at index i reset counter
        """
        ans = 0
        count = 0
        for ele in nums:
            if ele==0:
                count+=1
            else:
                count=0
            ans+=count

        return ans
      
nums = [1,3,0,0,2,0,0,4]
obj = Solution()
obj.zeroFilledSubarray(nums)
