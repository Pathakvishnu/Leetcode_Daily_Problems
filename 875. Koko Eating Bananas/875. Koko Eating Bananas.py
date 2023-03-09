import math

class Solution:
    def minEatingSpeed(self, piles, H):
        def feasible(speed) -> bool:
            return sum(math.ceil(pile / speed) for pile in piles) <= H        

        left, right = 1, max(piles)
        while left < right:
            mid = left  + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
    
piles = [3,6,7,11]
h = 8
obj = Solution()
obj.minEatingSpeed(piles,h)