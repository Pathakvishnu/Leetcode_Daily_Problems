from collections import Counter
from typing import List

class Solution:
    """
    We have used union find algorithm to find a good path.
    Now, good path is defined as:

    1. The starting node and the ending node have the same value.
    2. All nodes between the starting node and the ending node have values less than or equal to the starting node 
    (i.e. the starting node's value should be the maximum value along the path).

    Initially we treat each individual node as an component. Now, while merging a two component we will keep following things in mind
    1. Keep the record of max value in each component
    2. While merging if max value of both component is same we multiply the frequency of those max value in both component let's say
    Ci and Cj. And add this multiple to the result.
    3. If frequency of max value in a component is zero then added value to the result will also be zero since one Ci and Cj will be zero.
    4. Once, done add component Cj to Ci and make changes in max value for component Ci.
    4. We iterate over each edge and follow above steps from 1 to 4
    """
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        res = n = len(vals)
        f = list(range(n))
        count = [Counter({vals[i]: 1}) for i in range(n)]
        
        edges = sorted([max(vals[i], vals[j]),i,j] for i,j in edges)
        
        def find(x):
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        for v,i,j in edges:
            fi, fj = find(i), find(j)
            cj, ci = count[fi][v], count[fj][v]
            res += ci * cj
            f[fj] = fi
            count[fi] = Counter({v: ci + cj})
        return res

vals = [4,1,5,3,4,2,4,5]
edges = [[0,1],[0,2],[2,5],[1,3],[1,4],[3,6],[3,7]]

obj = Solution()
obj.numberOfGoodPaths(vals,edges)