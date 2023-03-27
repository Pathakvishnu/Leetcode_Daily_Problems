class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row,col = len(grid), len(grid[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]

        ## method 1

        for r in range(row):
            for c in range(col):
                if r==0 and c==0:
                    dp[r][c] = grid[r][c]
                else:
                    up,left = 1e6,1e6
                    if r>0:
                        up = grid[r][c] + dp[r-1][c]
                    if c>0:
                        left = grid[r][c] + dp[r][c-1]
                    dp[r][c] = min(up,left)

        return dp[row-1][col-1]

        # method 2

        # def dfs(r,c):
        #     if r==row-1 and c==col-1:
        #         return grid[r][c]

        #     if r<0 or r>=row or c<0 or c>=col:
        #         return 1e6

        #     if dp[r][c]!=-1:
        #         return dp[r][c]

        #     down = grid[r][c] + dfs(r+1,c)
        #     right = grid[r][c] + dfs(r,c+1)

        #     dp[r][c]  = min(down,right)
        #     return dp[r][c]
        
        # return dfs(0,0)
        
grid = [[1,3,1],[1,5,1],[4,2,1]]
obj = Solution()
obj.minPathSum(grid)
