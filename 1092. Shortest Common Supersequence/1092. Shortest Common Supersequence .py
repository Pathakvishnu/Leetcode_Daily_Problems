class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m,n = len(str1),len(str2)
        prev = [""]*(n+1)

        for i in range(m):
            cur = [""]*(n+1)
            for j in range(n):
                if str1[i]==str2[j]:
                    cur[j] = prev[j-1] + str1[i]
                else:
                    cur[j] = max(prev[j],cur[j-1],key=len)
            prev = cur
        lcs = cur[n-1]
        
        ans,i,j = "",0,0
        for ch in lcs:
            while str1[i]!=ch:
                ans+=str1[i]
                i+=1
            while str2[j]!=ch:
                ans+=str2[j]
                j+=1
        
            ans+=ch
            i+=1
            j+=1
        
        return ans+str1[i:]+str2[j:]

str1 = "abac"
str2 = "cab"

obj = Solution()
obj.shortestCommonSupersequence(str1,str2)
