class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        i = 31
        while n:
            last_bit = n & 1 
            last_bit = last_bit<<i
            res = res | last_bit
            n=n>>1
            i-=1
        return res
