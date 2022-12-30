from ast import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        end_node = len(graph)-1
        stack = [(0,[0])] # node, path
        res = []
        while stack:
            node,path = stack.pop()
            if node==end_node:
                res.append(path)
            
            for neig in graph[node]:
                stack.append((neig,path+[neig]))
        return res


graph = [[4,3,1],[3,2,4],[3],[4],[]]
obj = Solution()
print(obj.allPathsSourceTarget(graph))