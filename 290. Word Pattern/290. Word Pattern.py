class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern)!=len(words):
            return False
        if len(set(pattern))!=len(set(words)):
            return False
        word_to_pattern = dict()
        for i,w in enumerate(words):
            if word_to_pattern.get(w,0)==0:
                word_to_pattern[w]=pattern[i]
            elif word_to_pattern[w]!=pattern[i]:
                return False
        
        return True

pattern = "abba"
s = "dog cat cat dog"
obj = Solution()
obj.wordPattern(pattern,s)