from heapq import heappop,heappush
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row,col = len(heights),len(heights[0])
        dist = [[1e7]*col for _ in range(row)]
        dist[0][0] = 0
        minHeap = [(0, 0, 0)] # distance, row, col
        direct = [(1,0),(0,1),(-1,0),(0,-1)]

        while minHeap:
            d,r,c  = heappop(minHeap)
            if r==row-1 and c==col-1:
                return d
            for x,y in direct:
                new_r = r + x
                new_c = c + y

                if 0<=new_r<row and 0<=new_c<col:
                    maxDist = max(d,abs(heights[new_r][new_c]-heights[r][c]))
                    if dist[new_r][new_c]>maxDist:
                        dist[new_r][new_c]=maxDist
                        heappush(minHeap,(dist[new_r][new_c],new_r,new_c))
            
heights = [[1,2,2],[3,8,2],[5,3,5]]
obj = Solution()
obj.minimumEffortPath(heights)