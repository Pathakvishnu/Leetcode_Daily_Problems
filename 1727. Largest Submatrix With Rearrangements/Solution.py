class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        # first calculate number of consecutive ones in each column and then sort the 
        # column in descending order.

        row = len(matrix)
        col = len(matrix[0])
        prev_row = [0]*col
        ans = 0

        for r in range(row):
            curr_row = matrix[r][:]
            for c in range(col):
                if curr_row[c]==1 and r>0:
                    curr_row[c]+=prev_row[c]

            sorted_row = sorted(curr_row,reverse=True)
            for i in range(col):
                ans = max(ans, sorted_row[i]*(i+1))
            prev_row = curr_row
        return ans
