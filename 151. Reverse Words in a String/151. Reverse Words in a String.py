class Solution:
    def reverseWords(self, s: str) -> str:
        slen = len(s)
        l = slen-1
        r = slen-1
        res = list()
        while l>=0:
            while s[l]==' ' and s[r]==' ':
                l-=1
                r-=1
            while s[l]!=' ' and l>=0:
                l-=1
            if s[l+1:r+1]!="":
                res.append(s[l+1:r+1])
            r = l 
        return " ".join(res)
            
s = "the sky is blue"          
obj = Solution()
print(obj.reverseWords(s))