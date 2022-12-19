from typing import List


class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        """
        q is query length
        TC -> O(q*log(n))
        SC -> O(q)
        """
        ans = list()

        for x,y in queries:
            step = 0
            while x!=y:
                if x>y:
                    x//=2
                elif y>x:
                    y//=2
                step+=1
            ans.append(step+1)
        
        return ans

n = 3
queries = [[5,3],[4,7],[2,3]]

obj = Solution()
obj.cycleLengthQueries(n,queries)