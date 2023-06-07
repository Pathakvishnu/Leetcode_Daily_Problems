class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        while a or b or c:
            if c & 1: # i.e we want atleast a or b to be 1
                ans+= 0 if ((a&1) or (b&1)) else 1
            else: # i.e. we want both a and b to be 0
                ans+= (a&1) + (b&1)
            
            a>>=1
            c>>=1
            b>>=1

        return ans

a = 2
b = 6
c = 5

obj = Solution()
obj.minFlips(a,b,c)
