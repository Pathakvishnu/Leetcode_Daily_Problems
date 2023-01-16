from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_l,new_h = newInterval
        left_res,rgt_res = [],[]
        n = len(intervals)
        idx = 0
        while idx<n:
            l,h = intervals[idx][0],intervals[idx][1]
            if h<new_l:
                left_res.append([l,h])
            elif l>new_h:
                rgt_res.append([l,h])
            else:
                new_l = min(l,new_l)
                new_h = max(h,new_h)
            idx+=1
        return left_res+[[new_l,new_h]]+rgt_res
            
intervals = [[1,3],[6,9]]
newInterval = [2,5]
obj = Solution()
obj.insert(intervals,newInterval)