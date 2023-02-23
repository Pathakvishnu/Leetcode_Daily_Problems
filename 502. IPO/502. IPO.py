from heapq import heappop, heappush
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        num_projects = len(capital)
        projects = list(zip(capital,profits))

        projects = sorted(projects)

        queue = list()
        ptr = 0

        for i in range(k):  
            while ptr<num_projects and projects[ptr][0]<=w:
                heappush(queue,-projects[ptr][1])
                ptr+=1
            
            if not queue:
                break

            w+=(-heappop(queue))
        return w
    
k = 2
w = 0
profits = [1,2,3]
capital = [0,1,1]
obj = Solution()
obj.findMaximizedCapital(k,w,profits,capital)