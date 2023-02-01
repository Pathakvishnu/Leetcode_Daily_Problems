class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if they have non-zero GCD string.
        if str1 + str2 != str2 + str1:
            return ""

        def gcd(a,b):
            if a<b:
                a,b = b,a
            if b==0:
                return a
            return gcd(b,a%b)
            
        # Get the GCD of the two lengths.
        max_length = gcd(len(str1), len(str2))
        return str1[:max_length]

str1 = "ABCABC"
str2 = "ABC"

obj = Solution()
obj.gcdOfStrings(str1,str2)