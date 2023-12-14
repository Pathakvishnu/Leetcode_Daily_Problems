class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        # store the number of zeros and ones for each row and col
        row = [0]*m
        col = [0]*n

        for i in range(m):
            for j in range(n):
                col[j]+=grid[i][j]
                row[i]+=grid[i][j]
                
        ans = []
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(row[i] + col[j] - (n - row[i]) - (m - col[j]))
            ans.append(temp)
        return ans
