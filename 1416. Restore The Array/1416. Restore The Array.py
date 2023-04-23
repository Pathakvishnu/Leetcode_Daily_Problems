class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        m = len(str(k))
        dp = [0]*(n+1)
        def dfs(i):
            if i==n:
                return 1
            if s[i]=='0':
                return 0
            if dp[i]:
                return dp[i]

            count = 0
            for j in range(i,n):
                num = s[i:j+1]
                if int(num)>k:
                    break
                count+=dfs(j+1)

            dp[i] = count%(10**9+7)
            return count

        return dfs(0)%(10**9+7)
