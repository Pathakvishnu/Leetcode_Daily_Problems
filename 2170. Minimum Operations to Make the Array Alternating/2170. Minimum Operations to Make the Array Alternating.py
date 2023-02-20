from ast import List
from collections import defaultdict


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        even = defaultdict(int)
        odd = defaultdict(int)

        n = len(nums)

        for i in range(n):
            if i%2:
                odd[nums[i]]+=1
            else:
                even[nums[i]]+=1

        firstEven,secondEven = (None,0),(None,0)
        firstOdd,secondOdd = (None,0),(None,0)
        for k,v in even.items():
            if v>firstEven[1]:
                firstEven,secondEven = (k,v),firstEven
            elif v>secondEven[1]:
                secondEven = (k,v)

        for k,v in odd.items():
            if v>firstOdd[1]:
                firstOdd,secondOdd = (k,v),firstOdd
            elif v>secondOdd[1]:
                secondOdd = (k,v)
        
        if firstEven[0]!=firstOdd[0]:
            return n-(firstEven[1]+firstOdd[1])
        else:
            return n-max(firstEven[1]+secondOdd[1],secondEven[1]+firstOdd[1])
        
nums = [3,1,3,2,4,3]
obj = Solution()
obj.minimumOperations(nums)