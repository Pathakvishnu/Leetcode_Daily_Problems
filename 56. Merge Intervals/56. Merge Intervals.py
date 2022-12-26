from ast import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        # print(intervals)
        min_interval = intervals[0][0]
        max_interval = intervals[0][1]
        merge = []
        for i in range(1,len(intervals)):
            flag = True
            if min_interval<=intervals[i][0]<=max_interval:
                min_interval = min(min_interval,intervals[i][0])
                max_interval = max(max_interval,intervals[i][1])
                flag = False
            
            if flag:
                merge.append([min_interval,max_interval])
                min_interval = intervals[i][0]
                max_interval = intervals[i][1]
        merge.append([min_interval,max_interval])
        # print(merge)
        return merge

intervals = [[1,3],[2,6],[8,10],[15,18]]
obj = Solution()
obj.merge(intervals)