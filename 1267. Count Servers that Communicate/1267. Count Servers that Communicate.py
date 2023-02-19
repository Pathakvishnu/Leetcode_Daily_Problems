from pyparsing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row,col = len(grid),len(grid[0])
        row_servers = [0]*row
        col_servers = [0]*col
        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    row_servers[i]+=1
                    col_servers[j]+=1
        count=0
        for i in range(row):
            for j in range(col):
                if grid[i][j] and (row_servers[i]>1 or col_servers[j]>1):
                    count+=1
            
        return count

        
grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
obj = Solution()
obj.countServers(grid)