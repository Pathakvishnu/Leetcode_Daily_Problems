class Solution:
    def smallestValue(self, n: int) -> int:

        def getPrimeFactors(n):
            div = 2
            ans = 0
            while n>1:
                if not n%div:
                    ans+=div
                    n = n//div
                else:
                    div+=1
            return ans

        while True:
            ans = getPrimeFactors(n)
            if ans==n:
                break
            n = ans
            
        return ans