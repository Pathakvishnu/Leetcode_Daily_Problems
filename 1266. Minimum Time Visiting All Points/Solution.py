class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        i = 0
        ans = 0
        while i<len(points)-1:
            j = i+1
            x_cord = abs(points[j][0]-points[i][0])
            y_cord = abs(points[j][1]-points[i][1])
            ans += max(x_cord,y_cord)

            i+=1
        
        return ans
            
