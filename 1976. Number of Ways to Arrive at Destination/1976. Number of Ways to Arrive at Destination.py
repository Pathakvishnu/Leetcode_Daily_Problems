from ast import List
from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)

        for s,d,dist in roads:
            g[s].append([d,dist])
            g[d].append([s,dist])

        dist = [float('inf')] * n
        dist[0]=0
        cnt = [0]*n
        cnt[0]=1
        stack = [(0,0)]

        while stack:
            min_dist,node = heappop(stack)
            for ngh,w in g[node]:
                cand = w + min_dist
                if cand==dist[ngh]:
                    cnt[ngh]+=cnt[node]
                elif cand<dist[ngh]:
                    dist[ngh]=cand
                    heappush(stack,(w + min_dist,ngh))
                    cnt[ngh] = cnt[node]
            # print(f"node={node} cnt={cnt} stack={stack}")

        return cnt[-1]%(10**9+7)

n = 7
roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
obj = Solution()
print(obj.countPaths(n,roads))

