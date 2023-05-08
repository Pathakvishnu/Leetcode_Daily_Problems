class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)

        visited = set()
        
        total_sum = 0
        i=0
        while i<n:    
            visited.add((i,i))
            total_sum+=mat[i][i]
            i+=1
        
        r = n-1
        c = 0
        while c<n and r>=0:
            if (r,c) not in visited:
                total_sum+=mat[r][c]
            
            r-=1
            c+=1
        
        return total_sum
       
mat = [[1,2,3],
        [4,5,6],
        [7,8,9]]

obj = Solution()
obj.diagonalSum(mat)
