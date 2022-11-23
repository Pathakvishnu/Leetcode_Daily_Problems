from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        # here we are marking the each index with some tags 
        # if element is repeated then two tags might appear same 
        # and true length of tag won't be same as length of set tag
        
        for i in range(9):
            for j in range(9):
                ele = board[i][j]
                if ele != '.':
                    a = f'{ele} + in row {i}'
                    b = f'{ele} + in column {j}'
                    c = f'{ele} + in block {i//3}-{j//3}'

                    if a in seen or b in seen or c in seen:
                        return False
                    
                    seen.add(a)
                    seen.add(b)
                    seen.add(c) 

        return True
    
board = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

obj = Solution()
print(obj.isValidSudoku(board))