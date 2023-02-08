from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def dfs(nums, path):
            if not nums:
                res.append(path)
                # return # backtracking
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], path+[nums[i]])

        dfs(nums,[])
        return res
    
nums = [1,2,3]
obj = Solution()
obj.permute(nums)