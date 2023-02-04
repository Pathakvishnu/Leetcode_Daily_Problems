from ast import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt = Counter(p)
        permute_len = len(p)
        l = 0
        ans = []
        for r, c in enumerate(s):
            cnt[c] -= 1
            while cnt[c] < 0:  
                cnt[s[l]] += 1
                l += 1
            if r - l + 1 == permute_len: 
                ans.append(l)
            
        return ans
    
s = "cbaebabacd"
p = "abc"
obj = Solution()
obj.findAnagrams(s,p)