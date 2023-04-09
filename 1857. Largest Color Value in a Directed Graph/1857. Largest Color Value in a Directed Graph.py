class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        # calculate indegree for each node
        num_nodes = len(colors)
        indegree = [0]*num_nodes
        graph = defaultdict(list)
        for s,d in edges:
            indegree[d]+=1
            graph[s].append(d)

        queue = list()
        for node,degree in enumerate(indegree):
            if degree==0:
                queue.append(node)

        ans = 0
        node_visited = 0
        color_count = [[0]*26 for _ in range(num_nodes)]

        while queue:
            node = queue.pop(0)
            color_count[node][ord(colors[node])-ord('a')]+=1
            ans = max(ans,color_count[node][ord(colors[node])-ord('a')])
            node_visited+=1

            for ngh in graph[node]:
                for i in range(26):
                    color_count[ngh][i] = max(color_count[ngh][i],color_count[node][i])

                indegree[ngh]-=1
                if indegree[ngh]==0:
                    queue.append(ngh)
        
        return -1 if node_visited<num_nodes else ans
      
colors = "abaca"
edges = [[0,1],[0,2],[2,3],[3,4]]
