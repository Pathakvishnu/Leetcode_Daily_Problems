class Solution:
    def partitionString(self, s: str) -> int:
        st=end=0
        slen = len(s)
        count = [0]*26
        partitions = 0
        while end<slen:
            idx = ord(s[end])-ord('a')
            if count[idx]==0:
                count[idx]+=1
            elif count[idx]>0:
                partitions+=1
                count = [0]*26 # reset
                st = end
                end-=1
            end+=1
        
        return partitions+1

s = "abacaba"
obj = Solution()
obj.partitionString(s)