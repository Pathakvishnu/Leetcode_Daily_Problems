from ast import List
import math


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        """
        TC -> O(nlogn) + O(n) -> sorting + iteration
        SC -> O(n) -> storing result
        """
        nums = sorted(nums) 
        store = dict()
        max_streak = -1
        for ele in nums:
            if not store.get(math.sqrt(ele),0):
                store[ele]=1
            else:
                store[ele] = store.get(math.sqrt(ele)) + 1
                max_streak = max(max_streak,store[ele])
        
        return max_streak


nums = [4,3,6,16,8,2]
obj = Solution()
print(obj.longestSquareStreak(nums))