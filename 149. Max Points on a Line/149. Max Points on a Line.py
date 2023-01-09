import math
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        MAX_SLOPE=1e5
        result = 0
        n = len(points)

        def get_slope(y2, y1, x2, x1):
            y_diff = (y2-y1)
            x_diff = (x2-x1)
            g = math.gcd(y_diff, x_diff)
            y_diff = y_diff / g
            x_diff = x_diff / g
            return (y_diff, x_diff)

        for i in range(n):
            x1,y1 = points[i][0],points[i][1]
            slope_count = {}
            for j in range(n):
                if j!=i:
                    x2,y2 = points[j][0],points[j][1]
                    if x1==x2:
                        slope_count[MAX_SLOPE] = slope_count.get(MAX_SLOPE,0)+1
                    else:
                        slope = get_slope(y2,y1,x2,x1)
                        slope_count[slope] = slope_count.get(slope,0)+1

            local_max = 0
            for k,v in slope_count.items():
                local_max = max(local_max,v)

            result = max(result,local_max+1)
        return result
    
points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
obj = Solution()
print(obj.maxPoints(points))