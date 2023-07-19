class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals,key=lambda k:k[1])
        min_x = intervals[0][0]
        max_y = intervals[0][1]

        overlapping = 0
        for i in range(1,len(intervals)):
            if intervals[i][0]<max_y:
                overlapping+=1
            else:
                max_y = max(max_y,intervals[i][1])
            
        return overlapping

intervals = [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]
obj = Solution()
obj.eraseOverlapIntervals(intervals)
