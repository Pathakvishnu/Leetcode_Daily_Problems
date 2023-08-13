class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {-1:True}

        def valid_prefix(idx):
            if memo.get(idx,"no_key")!="no_key":
                return memo[idx]
            
            ans = False

            if idx>0 and nums[idx]==nums[idx-1]:
                ans = ans or valid_prefix(idx-2)
            if idx>1 and nums[idx]==nums[idx-1]==nums[idx-2]:
                ans = ans or valid_prefix(idx-3)
            if idx>1 and nums[idx]==nums[idx-1]+1==nums[idx-2]+2:
                ans = ans or valid_prefix(idx-3)

            memo[idx] = ans

            return ans
        
        return valid_prefix(n-1)

nums = [4,4,4,5,6]
obj = Solution()
obj.validPartition(nums)
