class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]*n
        for i in range(n):
            for word in wordDict:
                if i<len(word)-1:
                    continue
                if i==len(word)-1 or dp[i-len(word)]:
                    if s[i-len(word)+1:i+1]==word:
                        dp[i] = True
                        break
        
        return dp[-1]

s = "leetcode"
wordDict = ["leet","code"]
obj = Solution()
obj.wordBreak(s, wordDict)
