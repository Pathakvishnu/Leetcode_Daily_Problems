class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        """
        Solution 1: sort the matrices and return the top weakest rows.
        Note: here, we don't actually need to count the number of 1's or soldier
        as the rows will be automatically sorted based on row which has highest number of 1's.
        """

        # return sorted(range(len(mat)),key=lambda k:(mat[k],k))[:k]

        """
        Solution 2: Count the number of 1's and maintain the min-heap to extract out k weakest 
        rows.
        """
        min_heap = []
        for idx, row_data in enumerate(mat):
            power = sum(row_data)
            heapq.heappush(min_heap,(-power,-idx))
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        
        return [-i for _,i in sorted(min_heap,reverse=True)]
        
