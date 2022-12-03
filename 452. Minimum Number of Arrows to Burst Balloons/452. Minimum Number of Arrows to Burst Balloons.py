from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        points = sorted(points, key = lambda x:x[1])
        curMax, arrowNum = points[0][1], 1
        for balloon in points:
            if balloon[0] > curMax:
                curMax = balloon[1]
                arrowNum += 1
        return arrowNum

points = [[1,9],[2,7],[8,9]]
obj = Solution()
print(obj.findMinArrowShots(points))