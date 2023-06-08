class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def bin(row):
            low, high = 0, len(row)-1
            while low<=high:
                mid = (low + high) // 2
                if row[mid]<0:
                    high = mid-1
                else:
                    low = mid+1
            return len(row)- low

        count = 0
        for row in grid:
            count += bin(row)
        return(count)
      
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
