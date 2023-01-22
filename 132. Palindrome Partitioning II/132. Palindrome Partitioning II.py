from functools import lru_cache

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        
        @lru_cache(None)
        def front_partition(i):  # s[i..n-1]
            if i == n:
                return 0
            ans = n # we are keeping max paritition as length of string because no partition can be greater than the length of string.
            for j in range(i, n):
                cur = s[i:j+1]
                if cur==cur[::-1]:
                    ans = min(ans, front_partition(j+1) + 1)
            return ans
        
        return front_partition(0) - 1

inp = "aab"
obj = Solution()
obj.minCut(inp)