from collections import defaultdict
from typing import List


class Solution:

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        if n==1 and not dislikes:
            return True

        NOT_KNOWN,BLUE,RED = 0,1,-1

        dislike_person = defaultdict( list )
        color_person = defaultdict(int)
        
        for p1, p2 in dislikes:
            dislike_person[p1].append(p2)
            dislike_person[p2].append(p1)

        def dfs(p,color):
            color_person[p]=color
            for other_p in dislike_person[p]:
                if color_person[other_p]==color:
                    return False
                if not color_person[other_p] and not dfs(other_p,-color):
                    return False
            return True
        for p in range(1,n+1):
            if not color_person[p] and not dfs(p,BLUE):
                return False
        return True

n = 5
dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]],
obj = Solution()
obj.possibleBipartition(n,dislikes)