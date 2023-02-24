from heapq import heappop, heappush
from pyparsing import List


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        queue = [] # priority queue
        res = 1e9
        for ele in nums:
            heappush(queue,-ele*2 if ele%2 else -ele)
        min_ele = -max(queue)

        while len(queue)==len(nums):
            ele = -heappop(queue)
            res = min(res,ele-min_ele)
            if not ele%2:
                min_ele = min(min_ele,ele//2)
                heappush(queue,-ele//2)
        return res

nums = [2,10,8]
obj = Solution()
obj.minimumDeviation(nums)