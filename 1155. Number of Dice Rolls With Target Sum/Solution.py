class Solution:
    def numRollsToTarget(self, n: int, K: int, target: int) -> int:
        # mod = 1e9+7
        # dp = [[0 for _ in range(target+1)] for _ in range(n+1)]
        # dp[0][0] = 1
        # for i in range(1,n+1):
        #     for j in range(1,target+1):
        #         for k in range(1,K+1):
        #             if k<=j:
        #                 dp[i][j] = (dp[i][j] + dp[i-1][j-k])%mod                

        # return int(dp[n][target])

        MOD = 10**9 + 7
        store = {}
        def get_possibility(d, target):
            if d==0:
                return 0 if target>0 else 1
            
            if (d, target) in store:
                return store[(d,target)]
            
            score = 0
            for k in range(max(0, target-K),target):
                score+=get_possibility(d-1,k)
            
            store[(d,target)] = score

            return score
        
        return get_possibility(n, target) % MOD

