from ast import List
import math


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if left==1 and right>=3:
            return [2,3]
        min_diff = 1e7
        a=b=None
        best_pair=None
        for num in range(left,right+1):
            if self.is_prime(num):
                if not a and not b:
                    a=num
                elif a and not b:
                    b=num
                    if b-a<min_diff:
                        min_diff = b-a
                        best_pair = [a,b]
                    a = b
                    b = None
            if min_diff<3:
                return best_pair
        if not best_pair:
            return [-1,-1]
        return best_pair

    def is_prime(self,num):
        if num==1:
            return False
        if num%2==0:
            return False
        
        for i in range(3,int(math.sqrt(num))+1):
            if num%i==0:
                return False
        
        return True

left = 1
right = 1000
obj = Solution()
print(obj.closestPrimes(left,right))