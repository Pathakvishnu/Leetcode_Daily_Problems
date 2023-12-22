class Solution:
    def maxScore(self, s: str) -> int:
        
        # let's count number of ones in the string -> one pass O(n)
        one_count = 0
        for digit in s:
            if digit=='1':
                one_count+=1
        
        # one last pass for calculating max score
        ans = 0
        one_till_now = 0
        zero_till_now = 0
        for i in range(len(s)-1):
            if s[i]=='1':
                one_till_now+=1
            if s[i]=='0':
                zero_till_now+=1
            
            ans = max(ans, one_count-one_till_now+zero_till_now)
        
        return ans
