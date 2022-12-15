class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        prev = [0]*(n+1)
        for i in range(n-1,-1,-1):
            cur = [0]*(n+1)
            for j in range(n):
                if s[i]==s[j]:
                    cur[j] = prev[j-1] + 1
                else:
                    cur[j] = max(prev[j],cur[j-1])
            prev = cur
        # print(cur)
        return cur[n-1]

s = "bbbab"
obj = Solution()
print(obj.longestPalindromeSubseq(s))
