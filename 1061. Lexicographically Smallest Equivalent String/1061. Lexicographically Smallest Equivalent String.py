from collections import defaultdict

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        adj = defaultdict(set) # set to avoid duplication
        for a,b in zip(s1,s2):
            adj[a].add(b)
            adj[b].add(a)

        memo = {} # avoid recalculation of same state

        # traverse each component and return lexicographically smallest string 
        def bfs(ch):
            if ch in memo:
                return memo[ch]
            seen = set()
            res = ch
            queue = [ch]

            while queue:
                c = queue.pop()
                if c in seen:
                    continue
                seen.add(c)
                res = min(res,c)
                queue.extend(list(adj[c]))

            for node in seen:
                memo[node] = res
            
            return res
        
        ans = ""
        for ch in baseStr:
            ans+=bfs(ch)
        
        return ans

s1 = "parker"
s2 = "morris"
baseStr = "parser"

obj = Solution()
obj.smallestEquivalentString(s1,s2,baseStr)