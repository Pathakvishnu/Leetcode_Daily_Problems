class Solution:
    def isCircularSentence(self, s: str) -> bool:   
        if s[0]!=s[-1]:
            return False
        
        idx = 1
        n = len(s)
        while idx<n:
            if s[idx]==" ":
                if s[idx-1]!=s[idx+1]:
                    return False
            idx+=1
        
        return True

sentence = "leetcode exercises sound delightful"
obj = Solution()
print(obj.isCircularSentence(sentence))