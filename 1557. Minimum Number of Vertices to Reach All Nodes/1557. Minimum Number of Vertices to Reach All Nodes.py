class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        If a vertice or node has an incoming edge then definitely that node won't be included in
        the answer set. 

        If a vertice or node has no incoming edge then that node will be included in the answer
        set reason being since there is no incoming edge on that node, so to cover all nodes in
        graph these nodes has to be included.

        Solution is very simple..
        """

        has_incoming_edges = set()
        for i,(src,dst) in enumerate(edges):
            has_incoming_edges.add(dst)
        
        return set(range(n)) - has_incoming_edges
        
n = 6
edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]

obj = Solution()
obj.findSmallestSetOfVertices(n,edges)
