from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n==1:
            return True
        graph = [set() for _ in range(n)]
        visited = [False]*n
        for s,d in edges:
            graph[s].add(d)
            graph[d].add(s)

        # print(graph)
        stack = list()
        stack.append(source)

        while stack:
            node = stack.pop()
            visited[node]=True
            for neg in graph[node]:
                if neg==destination:
                    return True
                if not visited[neg]:
                    stack.append(neg)
        return False


n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2

obj = Solution()
obj.validPath(n,edges,source,destination)