class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        memo = [[0]*(n+1) for _ in range(n+1)]

        for i in range(n):
            for j in range(n):
                # ~i = -i-1
                if s[i]==s[~j]:
                    memo[i+1][j+1] = memo[i][j] + 1
                else:
                    memo[i+1][j+1] = max(memo[i+1][j],memo[i][j+1])
        
        return n - memo[n][n]
      
s = "aazaa"

obj = Solution()
obj.minInsertions(s)
