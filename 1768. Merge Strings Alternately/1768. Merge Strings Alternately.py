class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_len = len(word1)
        word2_len = len(word2)

        i=0
        j=0
        s = ""
        while i<word1_len and j<word2_len:
            s+=word1[i]
            s+=word2[j]

            i+=1
            j+=1
        
        while i<word1_len:
            s+=word1[i]
            i+=1
        while j<word2_len:
            s+=word2[j]
            j+=1
        
        return s
      
word1 = "abc"
word2 = "pqr"

obj = Solution()
obj.mergeAlternately(word1,word2)
