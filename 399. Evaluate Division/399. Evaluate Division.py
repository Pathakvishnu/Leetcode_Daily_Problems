class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (src,dst),val in zip(equations,values):
            graph[src][dst] = val
            graph[dst][src] = 1/val

        answer = []
        self.seen = set()
        def evaluate(curr_var:str, dst_var:str,value:float):
            if curr_var==dst_var:
                return value

            for adj_node, adj_value in graph[curr_var].items():
                if adj_node not in self.seen:
                    self.seen.add(adj_node)
                    result = evaluate(adj_node,dst_var,value*adj_value)
                    if result!=-1:
                        return result
                    self.seen.remove(adj_node)
            return -1
        
        for src, dst in queries:
            answer.append(evaluate(src,dst,1) if src in graph else -1)  
            self.seen.clear()

        return answer
     
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

obj = Solution()
obj.calcEquation(equations,values,queries)
