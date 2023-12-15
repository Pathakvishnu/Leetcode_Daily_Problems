class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        graph = {}
        start_node = None
        for a,b in paths:
            graph[a] = b
            start_node = a

        def dfs(node):
            # print(node)
            if not graph.get(node,0):
                return node
            return dfs(graph[node])

        return dfs(start_node)
        
