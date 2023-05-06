class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        nums = sorted(nums)
        mod = 10**9+7
        left = 0
        rgt = n-1
        ans = 0
        while left<=rgt:
            if nums[left]+nums[rgt]<=target:
                ans = ans + (pow(2,rgt-left,mod) % mod)
                left+=1
            else:
                rgt-=1

        return ans % mod

nums = [3,5,6,7]
target = 9

obj = Solution()
obj.numSubseq(nums,target)
