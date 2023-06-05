class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        def deltaY(a,b):
            return a[1] - b[1]
        
        def deltaX(a,b):
            return a[0] - b[0]

        delta_Y_cord = deltaY(coordinates[1],coordinates[0])
        delta_X_cord = deltaX(coordinates[1],coordinates[0])

        for i in range(2,len(coordinates)):
            if (delta_Y_cord*deltaX(coordinates[i],coordinates[0])!=delta_X_cord*deltaY(coordinates[i],coordinates[0])):
                return False

        return True

coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
obj = Solution()
obj.checkStraightLine(coordinates)
