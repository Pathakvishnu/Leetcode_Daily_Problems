from ast import List

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for idx,row in enumerate(grid):
            grid[idx] = sorted(row,reverse=True)

        ans = 0
        for j in range(len(grid[0])):
            temp = 0
            for i in range(len(grid)):
                temp = max(temp,grid[i][j])
            ans+=temp
        
        return ans

grid = [[1,2,4],[3,3,1]]
