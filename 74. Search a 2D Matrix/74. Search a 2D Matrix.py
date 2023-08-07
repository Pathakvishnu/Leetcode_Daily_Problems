class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        l,r = 0, row*col

        while l<r:
            print("enter")
            mid = (l+r-1)>>1
            if matrix[mid//col][mid%col]==target:
                return True
            elif matrix[mid//col][mid%col] < target:
                l = mid+1
            else:
                r = mid
        
        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
