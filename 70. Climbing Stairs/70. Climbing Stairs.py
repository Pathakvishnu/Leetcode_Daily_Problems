class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=3:
            return n
        dp = [2,3]
        for _ in range(n-3):
            dp[0],dp[1] = dp[1],dp[0]+dp[1]
        return dp[1]


obj = Solution()
obj.climbStairs(6)