class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        def getCount(word):
            wc = dict()
            for w in word:
                if not wc.get(w,0):
                    wc[w]=1
                else:
                    wc[w]+=1
            return wc

        wc1 = sorted(getCount(word1).values())
        wc2 = sorted(getCount(word2).values())

        wset1 = set(word1)
        wset2 = set(word2)

        return wset1==wset2 and wc1==wc2
        

word1 = "cabbba"
word2 = "abbccc"  
obj = Solution()
print(obj.closeStrings(word1,word2))
