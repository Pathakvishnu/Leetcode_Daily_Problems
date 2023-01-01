from ast import List
import math


class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        unq_prime_factors = set()

        for ele in nums:
            factors =self.prime_factors(ele)
            unq_prime_factors.update(factors)

        return len(unq_prime_factors)

    def prime_factors(self,ele):
        fac = set()

        while ele%2==0:
            fac.add(2)
            ele=ele//2
        
        for div in range(3,int(math.sqrt(ele)+1)):
            while ele%div==0:
                fac.add(div)
                ele=ele//div
        if ele>2:
            fac.add(ele)

        return fac

nums = [2,4,3,7,10,6]
obj = Solution()
print(obj.distinctPrimeFactors(nums))
