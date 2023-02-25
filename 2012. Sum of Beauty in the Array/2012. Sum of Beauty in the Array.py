from pyparsing import List

class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        N=len(nums)
        
        # for each index we have to check if all element before it is smaller than this
        min_till_now=[None for _ in range(N)]
        min_now=float('-inf')
        for i in range(N):
            min_till_now[i]=min_now
            min_now=max(nums[i],min_now)
                
        # for each index we have to check if all element after it is bigger than this       
        max_till_now=[None for _ in range(N)]
        max_now=float('inf')
        for i in range(N-1,-1,-1):
            max_till_now[i]=max_now
            max_now=min(max_now,nums[i])

        ans=0
        for i in range(1,N-1):
            if min_till_now[i]<nums[i]<max_till_now[i]:
                ans+=2
            elif nums[i-1]<nums[i]<nums[i+1]:
                ans+=1
        return ans
    
nums = [2,4,6,4]
obj = Solution()
obj.sumOfBeauties(nums)