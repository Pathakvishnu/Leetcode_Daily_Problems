class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n = n & (n-1) # remove the rightmost bits
            count+=1
        return count
