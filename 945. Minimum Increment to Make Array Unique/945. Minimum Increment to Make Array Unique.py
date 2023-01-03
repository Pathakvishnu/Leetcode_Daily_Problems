from ast import List
import collections


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        max_val = max(nums)
        count = collections.Counter(nums)
        taken = []
        
        moves = 0
        for x in range(len(nums) + max_val):
            if count[x] >= 2:
                taken.extend([x] * (count[x] - 1))
            elif taken and count[x] == 0:
                moves += x - taken.pop()
                
        return moves

nums = [3,2,1,2,1,7]
obj = Solution()
print(obj.minIncrementForUnique(nums))