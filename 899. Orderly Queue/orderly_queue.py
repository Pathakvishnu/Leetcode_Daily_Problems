class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        """
        For k==1, we can generate total of len(s) states and out of that lexicographically smallest we have to chose. Because n+1 state 
        will be same as 1st state.

        For k>1, let's consider k=3
        In this also we can rotate whole string but here we have a choice out k characters which one to append at the end
        inp = "aabca"
        *abca -> *bcaa -> *caab -> *aabc 
        a*bca -> *bcaa -> we reach same state as first one. And hence next states will be same
        aa*ca -> a*caa -> *caaa -> and so on

        so you see we can fix one index out of k and revolve the rest. But at the end you will see we always get 
        sorted(original string)

        """
        if k==1:
            return min(s[i:]+s[:i] for i in range(len(s)))
        else:
            return "".join(sorted(s))

inp = "aabca"
k = 3
obj = Solution()
print(obj.orderlyQueue(inp,k))
