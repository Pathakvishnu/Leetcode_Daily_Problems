from functools import lru_cache


class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        n = len(s)
        MOD = 10**9+7

        def isPrime(num):
            if num in ['2','3','5','7']:
                return True
            return False
        @lru_cache(None)
        def partition(i,k):
            if k==0 and i<=n:
                return 1
            if i>=n:
                return 0

            ans = partition(i+1,k)

            if isPrime(s[i]) and not isPrime(s[i-1]):
                ans+=partition(i+minLength,k-1)
            
            return ans%MOD
        
        if not isPrime(s[0]) or isPrime(s[-1]): return 0
        
        return partition(minLength,k-1)
    
s = "23542185131"
k = 3
minLength = 2

obj = Solution()
obj.beautifulPartitions(s,k,minLength)