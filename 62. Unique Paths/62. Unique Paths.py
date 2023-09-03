class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        m: represent number of row
        n: represent number of column

        starting point is always (0,0) and ending point is always (m-1,n-1) i.e. a fixed starting point and fixed ending point problem.
        
        """
        def findPaths(i,j):
            if (i==m-1) and (j==n-1):
                return 1
            if i>=m or j>=n:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]

            dp[i][j] = findPaths(i+1,j)+findPaths(i,j+1)
            return dp[i][j]
        
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return findPaths(0,0)
