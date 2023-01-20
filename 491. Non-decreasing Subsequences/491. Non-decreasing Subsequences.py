from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        """
        Constraints:
            1 <= nums.length <= 15
            -100 <= nums[i] <= 100

        since, constraint is low we can go with the backtracking approach 
        TC = O(2^n)
        SC = O(n)
        """
        res = []
        seen = dict()
        n = len(nums)
        def fn(idx,temp):
            if idx==n:
                if len(temp)>=2 and not seen.get(tuple(temp),0):
                    res.append(temp)
                    seen[tuple(temp)]=1
                return
            if not temp or nums[idx]>=temp[-1]:
                fn(idx+1,temp+[nums[idx]])
            fn(idx+1,temp)

            if len(temp)>=2 and not seen.get(tuple(temp),0):
                res.append(temp)
                seen[tuple(temp)]=1
        fn(0,[])
        return res

nums = [4,4,3,1,2,5]
obj = Solution()
obj.findSubsequences(nums)