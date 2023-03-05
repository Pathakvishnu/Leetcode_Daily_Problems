from typing import List

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        num_node = len(arr)
        if num_node<=1:
            return 0

        graph = dict()
        for i in range(num_node):
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]

        curr = [0]
        visited = {0}
        step = 0

        while curr:
            next_layer = []

            for node in curr:
                if node==num_node-1:
                    return step
                
                for child in graph[arr[node]]:
                    if child not in visited:
                        visited.add(child)
                        next_layer.append(child)
                    
                graph[arr[node]].clear() # to aovid redundant search

                for child in [node-1,node+1]:
                    if 0<=child<num_node and child not in visited:
                        visited.add(child)
                        next_layer.append(child)

            curr = next_layer
            step+=1

        return -1
    
arr = [100,-23,-23,404,100,23,23,23,3,404]
obj = Solution()
obj.minJumps(arr)