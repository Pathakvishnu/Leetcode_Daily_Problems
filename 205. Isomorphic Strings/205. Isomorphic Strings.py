class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sdict = {}
        tdict = {}

        for ch1,ch2 in zip(s,t):
            if not sdict.get(ch1,0) and not tdict.get(ch2,0):
                sdict[ch1] = ch2
                tdict[ch2] = ch1
            elif sdict.get(ch1)!=ch2 or tdict.get(ch2)!=ch1:
                return False
        
        return True
