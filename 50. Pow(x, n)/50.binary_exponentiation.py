class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1

        if n<0:
            n = -1*n
            x = 1.0/x

        # apply binary exponentiation technique
        """
        if n is odd -> x * (x^2)**n//2
        if n is even -> (x^2)**n//2
        """
        result = 1
        while n!=0:
            if n%2:
                result = result * x
                n-=1
            
            x = x*x
            n = n//2
        return result

    
x = 2.10000
n = 4
obj = Solution()
obj.myPow(x,n)
