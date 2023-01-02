class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        """
        Without using any function like isupper(),islower(),istitle() etc.
        """
        count = 0
        capital = {'A':1,'B':1,'C':1,'D':1,'E':1,'F':1,'G':1,'H':1,'I':1,'J':1,'K':1,'L':1
        ,'M':1,'N':1,'O':1,'P':1,'Q':1,'R':1,'S':1,'T':1,'U':1,'V':1,'W':1,'X':1,
        'Y':1,'Z':1}

        for alphabet in word:
            if capital.get(alphabet,0):
                count+=1
        
        if count==0 or (count==1 and capital.get(word[0])) or count==len(word):
            return True
    
word = "USA"
obj = Solution()
print(obj.detectCapitalUse(word))