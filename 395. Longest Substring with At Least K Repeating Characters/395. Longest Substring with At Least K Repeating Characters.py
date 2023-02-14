class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        slen = len(s)
        max_unique = 0
        take = dict()

        for i in range(slen):
            if take.get(s[i],0)==0:
                take[s[i]]=1
                max_unique+=1
        res = 0
        for curunq in range(1,max_unique+1):
            count = [0]*26
            unique = 0
            st,end=0,0
            count_k=0
            idx=0
            while end<slen:
                if unique<=curunq:
                    idx=ord(s[end])-ord('a')
                    if count[idx]==0:
                        unique+=1
                    count[idx]+=1
                    if count[idx]==k:
                        count_k+=1
                    end+=1
                else:
                    idx=ord(s[st])-ord('a')
                    if count[idx]==k:
                        count_k-=1
                    count[idx]-=1
                    if count[idx]==0:
                        unique-=1
                    st+=1
                
                if unique==curunq and unique==count_k:
                    res = max(end-st,res)

        return res


s = "ababbc"
k = 2
obj = Solution()
obj.longestSubstring(s,k)

