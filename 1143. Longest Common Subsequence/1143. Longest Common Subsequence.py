class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        TC -> O(mn)
        SC -> O(mn)
        """
        m,n = len(text1),len(text2)
        if n>m:
            text1,text2 = text2,text1
            m,n = n,m
        
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                if text1[i]==text2[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])

        return dp[i][j]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        TC -> O(mn)
        SC -> O(n)
        """
        m,n = len(text1),len(text2)
        if n>m:
            text1,text2 = text2,text1
            m,n = n,m
        
        prev_dp = [0 for _ in range(n+1)]

        for i in range(m):
            curr_dp = [0 for _ in range(n+1)]
            for j in range(n):
                if text1[i]==text2[j]:
                    curr_dp[j] = 1 + prev_dp[j-1]
                else:
                    curr_dp[j] = max(prev_dp[j],curr_dp[j-1])
            prev_dp = curr_dp  
        
        return curr_dp[-2]

            