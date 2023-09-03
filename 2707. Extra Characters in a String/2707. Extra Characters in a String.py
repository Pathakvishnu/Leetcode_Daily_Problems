class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dictionary = set(dictionary)
        dp = [0] *(n+1)

        for st in range(n-1,-1,-1):
            dp[st] = dp[st+1] + 1
            for end in range(st,n):
                if s[st:end+1] in dictionary:
                    dp[st] = min(dp[st],dp[end+1])
        
        return dp[0]
        
s = "leetscode", dictionary = ["leet","code","leetcode"]
