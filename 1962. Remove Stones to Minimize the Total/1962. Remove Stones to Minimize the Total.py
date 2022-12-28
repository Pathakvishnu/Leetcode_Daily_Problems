from ast import List
import heapq


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        tot_stones = 0
        heapq.heapify(heap)
        for stones in piles:
            tot_stones+=stones
            heapq.heappush(heap,-1*stones)
        
        while k:
            ele = -1*heapq.heappop(heap)
            left = ele-(ele//2)
            tot_stones-=(ele//2)
            heapq.heappush(heap,-1*left)
            k-=1
        return tot_stones

piles = [5,4,9]
k = 2
obj = Solution()
obj.minStoneSum(piles,k)