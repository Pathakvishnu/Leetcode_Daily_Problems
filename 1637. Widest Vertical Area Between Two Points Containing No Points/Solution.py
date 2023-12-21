class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # points = sorted(points,key = lambda k:k[0]) # will sort based on x-axis -> this will create new instance of sorted list, therefore consume more space.
        points.sort() # do in-place sorting, doesn't create a new list hence less memory consumption.
        ans = 0
        for i in range(1,len(points)):
            ans = max(ans, points[i][0]-points[i-1][0])
        
        return ans
