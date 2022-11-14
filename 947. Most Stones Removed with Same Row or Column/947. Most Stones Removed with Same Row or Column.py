from collections import defaultdict
from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        """
        It's like a number of island problem and below we are doing the same finding how many unique or seperated island is there.
        And the end from total stones we subtract the number of island to get an answer.
        
        instead of removing the visited array from stones, I stored it in set as removing the element from stones list would have 
        taken lot of time.    
        """
        n = len(stones)
        count = 0
        discarded = set() # to record the visited array 
        row,col = defaultdict(list),defaultdict(list)

        def dfs(i,j):
            discarded.add((i,j))
            for c in row[i]:
                if (i,c) not in discarded:
                    dfs(i,c)

            for r in col[j]:
                if (r,j) not in discarded:
                    dfs(r,j)

        for i,j in stones:
            row[i].append(j)
            col[j].append(i)

        for i,j in stones:
            if (i,j) not in discarded:
                dfs(i,j)
                count+=1
        
        return n-count
        
stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
obj = Solution()
print(obj.removeStones(stones))