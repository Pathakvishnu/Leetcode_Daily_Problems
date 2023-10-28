class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 1e9 + 7
        dp = [[0]*5 for _ in range(n+1)] # for storing number permutation upto that vowel for a particular words of length n given the constraints

        # for word of length 1, each vowel can start and end on itself
        for i in range(5):
            dp[1][i] = 1 # 1 here is word length

        for i in range(1,n):
            # below summation is based on graph dependency and a directed graph has been formed using the rules.

            # a
            dp[i+1][0] = (dp[i][1] + dp[i][2] + dp[i][4]) % MOD

            # e
            dp[i+1][1] = (dp[i][0]+dp[i][2]) % MOD

            #i
            dp[i+1][2] = (dp[i][1] + dp[i][3]) % MOD

            #o
            dp[i+1][3] = dp[i][2]

            #u
            dp[i+1][4] = (dp[i][2] + dp[i][3]) % MOD

        res = 0
        for i in range(5):
            res = (res + dp[n][i]) % MOD

        return int(res)


        
