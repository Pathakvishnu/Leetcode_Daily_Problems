class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        arrLen = min(steps, arrLen) # this is needed to avoid unncessary memory consumption
        dp = [[-1]*(steps+1) for _ in range(arrLen)]

        def calculate(curr_pos, remain_steps,dp):
            if remain_steps==0 and curr_pos==0:
                return 1
            if remain_steps==0 and curr_pos!=0:
                return 0

            if dp[curr_pos][remain_steps]!=-1:
                return dp[curr_pos][remain_steps]

            ans = calculate(curr_pos, remain_steps-1,dp) # for stay 

            if curr_pos>0:
                ans = (ans+ calculate(curr_pos-1,remain_steps-1,dp))%MOD # for left
            if curr_pos<arrLen-1:
                ans = (ans+ calculate(curr_pos+1,remain_steps-1,dp))%MOD # for right

            dp[curr_pos][remain_steps] = ans

            return ans

        return calculate(0,steps,dp)        
                
steps, arrLen = 438, 315977

obj = Solution()
obj.numWays(steps,arrLen)
