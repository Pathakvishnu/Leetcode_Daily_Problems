class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        partition = 0
        i,j=0,0
        n = len(s)
        while i<n:
            flag = False
            while j<=n and int(s[i:j+1])<=k:
                j+=1
                flag=True
            if not flag and int(s[j])>k:
                return -1
            if flag:
                partition+=1
            i=j
        return partition
            

s = "165462"
k=60
obj = Solution()
print(obj.minimumPartition(s,k))