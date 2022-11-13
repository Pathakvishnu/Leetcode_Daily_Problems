from math import lcm
from typing import List


class Solution:
    def get_gcd(self,a,b):
        while b:
            a,b = b,a%b
        return a
    def get_lcm(self,a,b):
        return (a*b)//self.get_gcd(a,b)

    def subarrayLCM(self, nums: List[int], k: int) -> int:
        count=0
        n = len(nums)
        for i in range(n):
            lcm_num= 1
            for j in range(i,n):
                lcm_num = self.get_lcm(lcm_num, nums[j])
                if lcm_num==k:
                    count+=1
                if lcm_num>k:
                    break
        return count
            
nums = [3,6,2,7,1]
k = 6

obj = Solution()
print(obj.subarrayLCM(nums,k))


