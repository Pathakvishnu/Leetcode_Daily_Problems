class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_freq = [0]*26
        t_freq = [0]*26

        for ch in s:
            s_freq[ord(ch)-ord('a')]+=1
        for ch in t:
            t_freq[ord(ch)-ord('a')]+=1

        changes = 0
        for i in range(26):
            if s_freq[i]>t_freq[i]:
                changes+=s_freq[i]-t_freq[i]
            
        return changes
