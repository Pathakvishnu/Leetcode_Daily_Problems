class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        modulo = 10**9+7
        
        # initialize dp array
        dp = [[-1 for _ in range(n+1)] for _ in range(goal+1)]

        def create_playlist(i,j):
            # i : goal, j: unique number of songs
            # base cases
            if i==0 and j==0:
                return 1
            
            if i==0 or j==0:
                return 0

            if dp[i][j]!=-1:
                return dp[i][j]

            dp[i][j] = (create_playlist(i-1,j-1)*(n-j+1))%modulo

            if j>k:
                dp[i][j]+=(create_playlist(i-1,j)*(j-k))%modulo
                dp[i][j]%=modulo
            return dp[i][j]

        return create_playlist(goal,n)
