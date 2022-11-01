from typing import List

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        row = len(grid)
        col = len(grid[0])
        
        def dfs(i,j):
            if i==row:
                return j
            """
            If cell and it's next cell in same row has opposite value then the ball is going to stuck
            """
            if grid[i][j]==1:
                if j+1>=col or grid[i][j+1]==-1:
                    return -1
                else:
                    return dfs(i+1,j+1)
            if grid[i][j]==-1:
                if j-1<0 or grid[i][j-1]==1:
                    return -1
                else:
                    return dfs(i+1,j-1)
       
        res = []
        for c in range(col):
            res.append(dfs(0,c))
        
        return res

grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
obj = Solution()
print(obj.findBall(grid))