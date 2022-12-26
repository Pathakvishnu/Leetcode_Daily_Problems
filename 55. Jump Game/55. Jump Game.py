from ast import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if nums[0]==0 and n>1:
            return False
        if n==1:
            return True
        max_jump_idx = 0
        for i in range(n):
            # if we stand at an index which is greater than max_jump_idx then we return False
            # because that's not possible 
            if i>max_jump_idx:
                return False
            max_jump_idx = max(max_jump_idx,i+nums[i])
        
        return True

nums = [2,3,1,1,4]
obj = Solution()
print(obj.canJump(nums))