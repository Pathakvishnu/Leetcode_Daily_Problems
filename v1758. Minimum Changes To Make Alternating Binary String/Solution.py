class Solution:
    def minOperations(self, s: str) -> int:
        operation = 0

        for i in range(len(s)):
            if i%2==0:
                if s[i]=='1':
                    operation+=1
            else:
                if s[i]=='0':
                    operation+=1
                
        return min(operation,len(s)-operation) 
