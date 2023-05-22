class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        direction = [(0,-1),(0,1),(1,0),(-1,0)]
        # get starting point
        def getFirstIsland():
            for i in range(m):
                for j in range(n):
                    if grid[i][j]==1:
                        return i,j

        # get boundary of island
        boundary=set()
        def dfs(i,j):
            grid[i][j]=-1
            for dx,dy in direction:
                x=i+dx
                y=j+dy
                if 0<=x<m and 0<=y<n:
                    if grid[x][y]==0:
                        boundary.add((x,y))
                    if grid[x][y]==1:
                        dfs(x,y)

        x,y = getFirstIsland()
        dfs(x,y)
        # get shortest distance from 2nd island
        steps=0

        while boundary:
            newBound = set()
            for i,j in boundary:
                for dx,dy in direction:
                    x = i + dx
                    y = j + dy
                    if 0<=x<m and 0<=y<n:
                        if grid[x][y]==0:
                            newBound.add((x,y))
                            grid[x][y]=-1
                        if grid[x][y]==1:
                            return steps+1
            steps+=1
            boundary=newBound
