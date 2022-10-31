from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        
        for r in range(1,row):
            for c in range(1,col):
                if matrix[r][c]!=matrix[r-1][c-1]:
                    return False
        return True

matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
obj = Solution()
print(obj.isToeplitzMatrix(matrix))