class Solution:
    def reorganizeString(self, s: str) -> str:
        char_count = {}
        max_count, letter = 0,''
        for ch in s:
            if char_count.get(ch,0):
                char_count[ch]+=1
            else:
                char_count[ch]=1

            if char_count[ch]>max_count:
                max_count=char_count[ch]
                letter = ch
        
        if max_count>(len(s)+1)//2:
            return ""
        
        ans = [''] * len(s)
        st = 0
        while char_count[letter]!=0:
            ans[st] = letter
            st+=2
            char_count[letter]-=1
        
        for ch,freq in char_count.items():
            while freq>0:
                if st>=len(s):
                    st=1
                ans[st] = ch
                st+=2
                freq-=1
            
        return ''.join(ans)

